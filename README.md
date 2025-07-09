
# LDCertFix

---

## 🇩🇪 Deutsch

**LDCertFix** ist ein leichtgewichtiges, portables Windows-Tool zum digitalen Signieren und Verifizieren von Dateien mithilfe vorhandener Code-Signing-Zertifikate.  
Es richtet sich an IT-Administratoren, Entwickler und DevOps-Teams, die signierte PowerShell-Skripte, EXE-Dateien oder Installationspakete bereitstellen müssen.

> 🛡️ Signieren. 🔎 Verifizieren. 📋 Protokollieren. — Schnell & transparent.

### 🔧 Funktionen

- ✅ Auswahl installierter Code-Signing-Zertifikate (Dropdown)
- 🗃️ Unterstützung für `.ps1`, `.exe`, `.dll`, `.msi`, `.ocx`, `.js`, `.vbs`, `.wsf`
- 🔏 Digitale Signatur mit Timestamp (konfigurierbarer Server)
- 🔍 Einzeldateiprüfung & Massenverifikation
- 📜 Ausführliches Log (Signieren & Prüfen)
- 🛠️ Komponententest für `signtool`, Windows SDK, PowerShell-Version
- 🖱️ Einfache, intuitive Bedienung
- 📦 Portable, kein Setup erforderlich

### 🚀 Verwendung

1. Starte `LDCertFix.exe`  
   Oder führe im Quellcode-Ordner aus:
   ```bash
   python main.py
   ```
2. Zertifikat auswählen  
   Im Dropdown erscheinen alle installierten Zertifikate mit privatem Schlüssel.

3. Dateien hinzufügen  
   Unterstützte Dateien können per Datei-Auswahl oder Drag & Drop hinzugefügt werden.

4. Signieren oder Prüfen  
   - Signieren versieht die Dateien mit einer digitalen Signatur inkl. Timestamp.
   - „Alle prüfen“ überprüft alle hinzugefügten Dateien.
   - „Datei prüfen“ erlaubt gezielte Einzelprüfung.

5. Log anzeigen  
   Zeigt ein vollständiges Protokoll aller Aktionen inklusive Signaturstatus und Zertifikatsdetails.

6. Info-Fenster  
   Liefert Hinweise zu den installierten Komponenten (z. B. signtool, SDK-Version etc.)

---

### 📦 Abhängigkeiten & Installation

Damit **LDCertFix** reibungslos funktioniert, müssen folgende Komponenten auf deinem System vorhanden sein:

**1. Python 3.9 oder neuer**  
*(Nur erforderlich, wenn du das Tool aus dem Quellcode ausführst.)*
- [Download Python](https://www.python.org/downloads/)
- Während der Installation **„Add Python to PATH“** aktivieren!
- Überprüfen:
  ```bash
  python --version
  ```

**2. signtool.exe (Bestandteil des Windows SDK)**  
- [Windows SDK herunterladen](https://developer.microsoft.com/de-de/windows/downloads/windows-sdk/)
- Bei der Installation reichen die **Signing Tools for Desktop Apps**.
- Prüfe den Pfad:
  ```
  C:\Program Files (x86)\Windows Kits\10\bin\<SDK-Version>\x64\signtool.exe
  ```

**3. PowerShell ab Version 5.1**
- Prüfen:
  ```powershell
  $PSVersionTable.PSVersion
  ```
- [PowerShell Download](https://learn.microsoft.com/de-de/powershell/scripting/install/installing-powershell)

**4. Zertifikat mit privatem Schlüssel im Windows-Zertifikatsspeicher**
- Zertifikate z. B. von [Certum](https://www.certum.eu/de/), [Sectigo](https://sectigo.com/), [DigiCert](https://www.digicert.com/), [GlobalSign](https://www.globalsign.com/)
- Import (Beispiel PowerShell):
  ```powershell
  Import-PfxCertificate -FilePath "C:\Pfad\zu\deinem.pfx" -CertStoreLocation Cert:\CurrentUser\My
  ```

**5. Weitere Python-Abhängigkeiten (bei Quellcode-Nutzung)**
- Installation:
  ```bash
  pip install -r requirements.txt
  ```
  oder einzeln:
  ```bash
  pip install pywin32
  ```

> **Hinweis:**  
> LDCertFix wurde bislang ausschließlich mit Code-Signing-Zertifikaten von **Certum** und dem dazugehörigen **SimplySign Desktop** getestet.  
> Die Kompatibilität mit anderen Zertifikatsanbietern wie Sectigo, DigiCert oder GlobalSign sollte grundsätzlich gegeben sein, wurde jedoch bislang nicht verifiziert.

> **Timestamp:**  
> Derzeit wird standardmäßig der Timestampserver  
> `http://timestamp.certum.pl`  
> verwendet. Der Server ist in den Einstellungen anpassbar.

---

### 🛠️ Schnelltest

Nach Installation aller Komponenten kannst du im Info-Fenster von **LDCertFix** prüfen, ob alles korrekt erkannt wurde.

---

### 📁 Release

Im Ordner `/release` befindet sich eine vorkompilierte, digital signierte `.exe`-Version.  
Keine Installation erforderlich – einfach starten.

---

### 🖼️ Logo

Ein Platzhalter-Icon (`logo.ico`) ist im Repository enthalten.  
Du kannst es durch ein eigenes quadratisches `.ico` ersetzen.

---

### 📜 Lizenz

Dieses Projekt steht unter der MIT-Lizenz – frei nutzbar, veränderbar und auch kommerziell einsetzbar.  
➡️ Siehe LICENSE

---

### 👤 Autor

© 2024–2025 Let's Do. – Inh. Peter Seidl  
Kontakt: pseidl@lets-do.media

---

### ❤️ Mitmachen

Pull Requests, Verbesserungsvorschläge und Feedback sind jederzeit willkommen!

---

### 📄 LICENSE (MIT)

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
```


# LDCertFix

---

## 🇬🇧 English

**LDCertFix** is a lightweight, portable Windows tool for digitally signing and verifying files using existing code-signing certificates.  
It is designed for IT administrators, developers, and DevOps teams who need to distribute signed PowerShell scripts, EXE files, or installation packages.

> 🛡️ Sign. 🔎 Verify. 📋 Log. — Fast & transparent.

### 🔧 Features

- ✅ Selection of installed code-signing certificates (dropdown)
- 🗃️ Supports `.ps1`, `.exe`, `.dll`, `.msi`, `.ocx`, `.js`, `.vbs`, `.wsf`
- 🔏 Digital signature with timestamp (configurable server)
- 🔍 Single file check & batch verification
- 📜 Detailed log (sign & verify)
- 🛠️ Component check for `signtool`, Windows SDK, PowerShell version
- 🖱️ Simple, intuitive operation
- 📦 Portable, no installation required

### 🚀 Usage

1. Start `LDCertFix.exe`  
   Or run from the source folder:
   ```bash
   python main.py
   ```
2. Select certificate  
   All installed certificates with private keys appear in the dropdown.

3. Add files  
   Supported files can be added via file dialog or drag & drop.

4. Sign or verify  
   - Signing attaches a digital signature with timestamp.
   - "Verify all" checks all added files.
   - "Verify file" allows single checks.

5. Show log  
   Displays a complete log of all actions, including signature status and certificate details.

6. Info window  
   Provides details about installed components (e.g., signtool, SDK version, etc.)

---

### 📦 Dependencies & Installation

To ensure **LDCertFix** works smoothly, please make sure the following components are present on your system:

**1. Python 3.9 or newer**  
*(Required only when running from source.)*
- [Download Python](https://www.python.org/downloads/)
- Make sure to enable **"Add Python to PATH"** during installation!
- Check version:
  ```bash
  python --version
  ```

**2. signtool.exe (part of Windows SDK)**  
- [Download Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/)
- "Signing Tools for Desktop Apps" is sufficient during installation.
- Check path:
  ```
  C:\Program Files (x86)\Windows Kitsin\<SDK-Version>d\signtool.exe
  ```

**3. PowerShell version 5.1 or higher**
- Check version:
  ```powershell
  $PSVersionTable.PSVersion
  ```
- [Download PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell)

**4. Certificate with private key in Windows certificate store**
- Certificates e.g. from [Certum](https://www.certum.eu/en/), [Sectigo](https://sectigo.com/), [DigiCert](https://www.digicert.com/), [GlobalSign](https://www.globalsign.com/)
- Import (PowerShell example):
  ```powershell
  Import-PfxCertificate -FilePath "C:\Path	o\your.pfx" -CertStoreLocation Cert:\CurrentUser\My
  ```

**5. Additional Python dependencies (for source usage)**
- Install:
  ```bash
  pip install -r requirements.txt
  ```
  or individually:
  ```bash
  pip install pywin32
  ```

> **Note:**  
> LDCertFix has so far only been tested with code-signing certificates from **Certum** and the corresponding **SimplySign Desktop**.  
> Compatibility with other certificate providers such as Sectigo, DigiCert, or GlobalSign is expected but has not yet been verified.

> **Timestamp:**  
> By default, the timestamp server  
> `http://timestamp.certum.pl`  
> is used. The server can be configured in the settings.

---

### 🛠️ Quick Test

After installing all components, use the info window in **LDCertFix** to check if everything was detected correctly.

---

### 📁 Release

The `/release` folder contains a precompiled, digitally signed `.exe` version.  
No installation required – just start.

---

### 🖼️ Logo

A placeholder icon (`logo.ico`) is included in the repository.  
You can replace it with your own square `.ico` file.

---

### 📜 License

This project is licensed under the MIT License – free for personal, commercial, and modification use.  
➡️ See LICENSE

---

### 👤 Author

© 2024–2025 Let's Do. – Owner: Peter Seidl  
Contact: pseidl@lets-do.media

---

### ❤️ Contributing

Pull requests, suggestions and feedback are always welcome!

---

### 📄 LICENSE (MIT)

```plaintext
MIT License

Copyright (c) 2025 Let's Do. – Owner: Peter Seidl

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
```
