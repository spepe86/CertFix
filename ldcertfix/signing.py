"""Helper functions for listing, verifying and signing with signtool."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path
from shutil import which
from typing import List

CREATE_NO_WINDOW = (
    subprocess.CREATE_NO_WINDOW
    if os.name == 'nt' and hasattr(subprocess, 'CREATE_NO_WINDOW')
    else 0
)


def _find_signtool() -> str | None:
    """Return path to signtool.exe if available, otherwise ``None``."""
    env = os.environ.get('SIGNTOOL_EXE') or os.environ.get('SIGNTOOL')
    if env and Path(env).exists():
        return env
    exe = which('signtool')
    if exe:
        return exe
    if os.name == 'nt':
        base = os.environ.get('ProgramFiles(x86)', os.environ.get('ProgramFiles'))
        if base:
            kits = Path(base) / 'Windows Kits'
            if kits.exists():
                for sub in kits.rglob('signtool.exe'):
                    return str(sub)
    return None


SIGNTOOL = _find_signtool()

# User-friendly error message if signtool.exe is unavailable
SIGNTOOL_ERROR = (
    "signtool.exe not found. Install the Windows SDK and set the "
    "SIGNTOOL_EXE environment variable or add signtool to PATH."
)


def list_certificates() -> List[tuple]:
    """Return list of tuples (subject, thumbprint) for certificates with private key."""
    cmd = [
        'powershell',
        '-Command',
        "Get-ChildItem Cert:\\CurrentUser\\My | Where-Object { $_.HasPrivateKey } | ForEach-Object { \"$($_.Subject)\t$($_.Thumbprint)\" }"
    ]
    try:
        result = subprocess.run(
            cmd,
            text=True,
            capture_output=True,
            creationflags=CREATE_NO_WINDOW,
        )
        out = result.stdout
        certs = []
        for line in out.strip().splitlines():
            if '\t' in line:
                subject, thumb = line.split('\t', 1)
                certs.append((subject.strip(), thumb.strip()))
        return certs
    except Exception:
        return []


def verify_file(path: Path) -> str:
    """Verify file signature and return output string."""
    if path.suffix.lower() in {'.exe', '.dll', '.msi', '.ocx'}:
        if SIGNTOOL is None:
            return SIGNTOOL_ERROR
        if not path.exists():
            return f'File not found: {path}'
        cmd = [SIGNTOOL, 'verify', '/pa', '/v', str(path)]
    else:
        ps_cmd = (
            f"$sig=Get-AuthenticodeSignature -FilePath '{path}';"
            "$cert=$sig.SignerCertificate;"
            "Write-Output \"Status: $($sig.Status)\";"
            "Write-Output \"Subject: $($cert.Subject)\";"
            "Write-Output \"Issuer: $($cert.Issuer)\";"
            "Write-Output \"Ausgestellt: $($cert.NotBefore)\";"
            "if($sig.Timestamp){Write-Output \"Signiert: $($sig.Timestamp)\";}"
        )
        cmd = ['powershell', '-Command', ps_cmd]
    try:
        result = subprocess.run(
            cmd,
            text=True,
            capture_output=True,
            creationflags=CREATE_NO_WINDOW,
        )
        return result.stdout or result.stderr
    except Exception as e:
        return str(e)


def sign_file(path: Path, thumbprint: str) -> str:
    """Sign ``path`` using the certificate specified by ``thumbprint``."""
    if path.suffix.lower() in {'.exe', '.dll', '.msi', '.ocx'}:
        if SIGNTOOL is None:
            return SIGNTOOL_ERROR
        if not path.exists():
            return f'File not found: {path}'
        cmd = [
            SIGNTOOL,
            'sign',
            '/sha1', thumbprint,
            '/fd', 'SHA256',
            '/tr', 'http://timestamp.certum.pl',
            '/td', 'SHA256',
            str(path),
        ]
    else:
        cmd = [
            'powershell',
            '-Command',
            (
                f"Set-AuthenticodeSignature -FilePath '{path}' "
                f"-Certificate (Get-Item Cert:\\CurrentUser\\My\\{thumbprint}) "
                f"-TimeStampServer 'http://timestamp.certum.pl'"
            )
        ]
    try:
        result = subprocess.run(
            cmd,
            text=True,
            capture_output=True,
            creationflags=CREATE_NO_WINDOW,
        )
        return result.stdout or result.stderr
    except Exception as e:
        return str(e)
