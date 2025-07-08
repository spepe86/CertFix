# LDCertFix

**LDCertFix** ist ein leichtgewichtiges, portables Windows-Tool zum digitalen Signieren und Verifizieren von Dateien mithilfe vorhandener Code-Signing-Zertifikate.  
Es richtet sich an IT-Administratoren, Entwickler und DevOps-Teams, die signierte PowerShell-Skripte, EXE-Dateien oder Installationspakete bereitstellen müssen.

> 🛡️ Signieren. 🔎 Verifizieren. 📋 Protokollieren. — Schnell & transparent.

---

## 🔧 Funktionen

- ✅ Auswahl installierter Code-Signing-Zertifikate (Dropdown)
- 🗃️ Unterstützung für `.ps1`, `.exe`, `.dll`, `.msi`, `.ocx`, `.js`, `.vbs`, `.wsf`
- 🔏 Digitale Signatur mit Timestamp (konfigurierbarer Server)
- 🔍 Einzeldateiprüfung & Massenverifikation
- 📜 Ausführliches Log (Signieren & Prüfen)
- 🛠️ Komponententest für `signtool`, Windows SDK, PowerShell-Version
- 🖱️ Einfache, intuitive Bedienung
- 📦 Portable, kein Setup erforderlich

---

## 🚀 Verwendung

1. Starte `LDCertFix.exe`  
   Oder führe im Quellcode-Ordner aus:
   ```bash
   python main.py
2. Zertifikat auswählen
Im Dropdown erscheinen alle installierten Zertifikate mit privatem Schlüssel.

3. Dateien hinzufügen
Unterstützte Dateien können per Datei-Auswahl oder Drag & Drop hinzugefügt werden.

4. Signieren oder Prüfen
Signieren versieht die Dateien mit einer digitalen Signatur inkl. Timestamp

Alle prüfen überprüft alle hinzugefügten Dateien

Datei prüfen erlaubt gezielte Einzelprüfung

Log anzeigen
Zeigt ein vollständiges Protokoll aller Aktionen inklusive Signaturstatus und Zertifikatsdetails.

Info-Fenster
Liefert Hinweise zu den installierten Komponenten (z. B. signtool, SDK-Version etc.)

## 📁 Release
Im Ordner /release befindet sich eine vorkompilierte, digital signierte .exe-Version.
Keine Installation erforderlich – einfach starten.

## 🖼️ Logo
Ein Platzhalter-Icon (logo.ico) ist im Repository enthalten.
Du kannst es durch ein eigenes quadratisches .ico ersetzen.

## 📦 Abhängigkeiten
Python 3.9+ (nur bei Nutzung des Quellcodes)

signtool.exe (aus Windows SDK)

PowerShell ≥ 5.1

Zertifikat mit privatem Schlüssel im Windows-Zertifikatsspeicher

## 📜 Lizenz
Dieses Projekt steht unter der MIT-Lizenz – frei nutzbar, veränderbar und auch kommerziell einsetzbar.
➡️ Siehe LICENSE

## 👤 Autor
© 2024–2025 Let's Do. – Inh. Peter Seidl
Kontakt: pseidl@lets-do.media

## ❤️ Mitmachen
Pull Requests, Verbesserungsvorschläge und Feedback sind jederzeit willkommen!


---

## 📄 LICENSE (MIT)

```plaintext
MIT License

Copyright (c) 2025 Let's Do. – Inh. Peter Seidl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
