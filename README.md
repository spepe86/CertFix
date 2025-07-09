# LDCertFix

**LDCertFix** ist ein leichtgewichtiges, portables Windows-Tool zum digitalen Signieren und Verifizieren von Dateien mithilfe vorhandener Code-Signing-Zertifikate.  
Es richtet sich an IT-Administratoren, Entwickler und DevOps-Teams, die signierte PowerShell-Skripte, EXE-Dateien oder Installationspakete bereitstellen müssen.

> 🛡️ Signieren. 🔎 Verifizieren. 📋 Protokollieren. — Schnell & transparent.

---

## 🔧 Funktionen

- ✅ Auswahl installierter Code-Signing-Zertifikate (Dropdown)
- 🗃️ Unterstützung für .ps1, .exe, .dll, .msi, .ocx, .js, .vbs, .wsf
- 🔏 Digitale Signatur mit Timestamp (konfigurierbarer Server)
- 🔍 Einzeldateiprüfung
- 📜 Ausführliches Log (Signieren & Prüfen)
- 🛠️ Komponententest für signtool, Windows SDK, PowerShell-Version
- 🖱️ Einfache, intuitive Bedienung
- 📦 Portable, kein Setup erforderlich
- 🌐 Sprachauswahl (DE, EN, PL, CZ)

---

## 🚀 Verwendung

1. Starte LDCertFix.exe  
   Oder führe im Quellcode-Ordner aus:
   
bash
   python main.py
2. Zertifikat auswählen
Im Dropdown erscheinen alle installierten Zertifikate mit privatem Schlüssel.

3. Dateien hinzufügen
Unterstützte Dateien können per Datei-Auswahl oder Drag & Drop hinzugefügt werden.

4. Signieren oder Prüfen
Signieren versieht die Dateien mit einer digitalen Signatur inkl. Timestamp

Datei prüfen erlaubt gezielte Einzelprüfung

Log anzeigen
Zeigt ein vollständiges Protokoll aller Aktionen inklusive Signaturstatus und Zertifikatsdetails.

Info-Fenster
Liefert Hinweise zu den installierten Komponenten (z. B. signtool, SDK-Version etc.) und zeigt das Programm-Icon an

## 📁 Release
Im Ordner /release befindet sich eine vorkompilierte, digital signierte .exe-Version.
Keine Installation erforderlich – einfach starten.

## 🖼️ Logo
Ein Platzhalter-Icon (logo.ico) ist im Repository enthalten.
Du kannst es durch ein eigenes quadratisches .ico ersetzen.

## 📦 Abhängigkeiten & Installation

Damit **LDCertFix** reibungslos funktioniert, müssen folgende Komponenten auf deinem System vorhanden sein:

**1. Python 3.9 oder neuer**  
*(Nur erforderlich, wenn du das Tool aus dem Quellcode ausführst.)*
- [Download Python](https://www.python.org/downloads/)
- Während der Installation **„Add Python to PATH“** aktivieren!
- Überprüfen:
bash
  python --version
  
**2. signtool.exe (Bestandteil des Windows SDK)**  
- [Windows SDK herunterladen](https://developer.microsoft.com/de-de/windows/downloads/windows-sdk/)
- Bei der Installation reichen die **Signing Tools for Desktop Apps**.
- Prüfe den Pfad:

  C:\Program Files (x86)\Windows Kits\10\bin\<SDK-Version>\x64\signtool.exe
  
**3. PowerShell ab Version 5.1**
- Prüfen:
powershell
  $PSVersionTable.PSVersion
  
- [PowerShell Download](https://learn.microsoft.com/de-de/powershell/scripting/install/installing-powershell)

**4. Zertifikat mit privatem Schlüssel im Windows-Zertifikatsspeicher**
- Zertifikate z. B. von [Certum](https://www.certum.eu/de/), [Sectigo](https://sectigo.com/), [DigiCert](https://www.digicert.com/), [GlobalSign](https://www.globalsign.com/)
- Import (Beispiel PowerShell):
powershell
  Import-PfxCertificate -FilePath "C:\Pfad\zu\deinem.pfx" -CertStoreLocation Cert:\CurrentUser\My
  
**5. Weitere Python-Abhängigkeiten (bei Quellcode-Nutzung)**
- Installation:
bash
  pip install -r requirements.txt
  
oder einzeln:
bash
  pip install pywin32
  
> **Hinweis:**  
> LDCertFix wurde bislang ausschließlich mit Code-Signing-Zertifikaten von **Certum** und dem dazugehörigen **SimplySign Desktop** getestet.  
> Die Kompatibilität mit anderen Zertifikatsanbietern wie Sectigo, DigiCert oder GlobalSign sollte grundsätzlich gegeben sein, wurde jedoch bislang nicht verifiziert.

> **Timestamp:**  
> Derzeit wird standardmäßig der Timestampserver  
> `http://timestamp.certum.pl`  
> verwendet. Der Server ist in den Einstellungen anpassbar.

---
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

```
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

**LDCertFix** is a lightweight, portable Windows tool for digitally signing and verifying files using existing code-signing certificates.  
It’s designed for IT administrators, developers, and DevOps teams who need to distribute signed PowerShell scripts, EXE files, or installation packages.

> 🛡️ Sign. 🔎 Verify. 📋 Log. — Fast & Transparent.

---

## 🔧 Features

- ✅ Select installed code-signing certificates (dropdown)
- 🗃️ Support for `.ps1`, `.exe`, `.dll`, `.msi`, `.ocx`, `.js`, `.vbs`, `.wsf`
- 🔏 Digital signing with timestamp (configurable server)
- 🔍 Single file verification
- 📜 Detailed logs (signing & verification)
- 🛠️ Component check for `signtool`, Windows SDK, PowerShell version
- 🖱️ Simple, intuitive UI
- 📦 Portable, no installation required
- 🌐 Language selection (EN, DE, PL, CZ)

---

## 🚀 Usage

1. Launch `LDCertFix.exe`  
   Or run from source directory:
   ```bash
   python main.py
   ```

2. Select Certificate  
   All installed certificates with private key appear in the dropdown.

3. Add Files  
   Supported files can be added via file picker or drag & drop.

4. Sign or Verify  
   Signing adds a digital signature with timestamp.  
   Verification checks individual files and displays result.

5. Show Log  
   Displays a full record of all actions including signature status and certificate info.

6. Info Window  
   Provides component status (e.g. signtool, SDK version) and program icon.

---

## 📁 Release

A precompiled, digitally signed `.exe` version is located in the `/release` folder.  
No installation required – just launch it.

## 🖼️ Logo

A placeholder icon (`logo.ico`) is included.  
You can replace it with your own square `.ico` file.

---

## 📦 Requirements & Installation

To run **LDCertFix** properly, ensure the following components are available on your system:

**1. Python 3.9 or later**  
*(Only needed when running from source)*  
- [Download Python](https://www.python.org/downloads/)  
- During install, enable **“Add Python to PATH”**  
- Check installation:
  ```bash
  python --version
  ```

**2. signtool.exe (part of Windows SDK)**  
- [Download Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/)  
- "Signing Tools for Desktop Apps" is sufficient during setup  
- Verify path:
  ```
  C:\Program Files (x86)\Windows Kits\10\bin\<SDK-Version>\x64\signtool.exe
  ```

**3. PowerShell 5.1 or later**  
- Check:
  ```powershell
  $PSVersionTable.PSVersion
  ```  
- [Download PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell)

**4. Certificate with private key in Windows Certificate Store**  
- Example import via PowerShell:
  ```powershell
  Import-PfxCertificate -FilePath "C:\Path\to\your.pfx" -CertStoreLocation Cert:\CurrentUser\My
  ```

**5. Python Dependencies (for source use)**  
- Install:
  ```bash
  pip install -r requirements.txt
  ```
  or manually:
  ```bash
  pip install pywin32
  ```

> **Note:**  
> LDCertFix has so far been tested primarily with **Certum** code signing certificates and **SimplySign Desktop**.  
> Compatibility with other providers like Sectigo, DigiCert, or GlobalSign should work in principle but hasn’t been verified.

> **Timestamp:**  
> Default timestamp server is:  
> `http://timestamp.certum.pl`  
> Configurable in settings.

---

## 📜 License

This project is licensed under the MIT License – free to use, modify, and distribute commercially.  
➡️ See LICENSE

## 👤 Author

© 2024–2025 Let's Do. – Owner: Peter Seidl  
Contact: pseidl@lets-do.media

## ❤️ Contribute

Pull requests, improvements, and feedback are always welcome!

---

## 📄 LICENSE (MIT)

```
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

**LDCertFix** to lekkie, przenośne narzędzie Windows do podpisywania cyfrowego i weryfikacji plików za pomocą istniejących certyfikatów Code Signing.  
Skierowane do administratorów IT, programistów i zespołów DevOps, którzy potrzebują podpisanych skryptów PowerShell, plików EXE lub pakietów instalacyjnych.

> 🛡️ Podpisuj. 🔎 Weryfikuj. 📋 Loguj. — Szybko i przejrzyście.

---

## 🔧 Funkcje

- ✅ Wybór zainstalowanych certyfikatów Code Signing (lista rozwijana)
- 🗃️ Obsługa plików `.ps1`, `.exe`, `.dll`, `.msi`, `.ocx`, `.js`, `.vbs`, `.wsf`
- 🔏 Podpis cyfrowy z timestampem (konfigurowalny serwer)
- 🔍 Weryfikacja pojedynczego pliku
- 📜 Szczegółowy log (podpisywanie i weryfikacja)
- 🛠️ Test komponentów (`signtool`, Windows SDK, wersja PowerShell)
- 🖱️ Intuicyjny, prosty interfejs
- 📦 Przenośne, bez instalacji
- 🌐 Wybór języka (PL, DE, EN, CZ)

---

## 🚀 Użytkowanie

1. Uruchom `LDCertFix.exe`  
   lub z katalogu źródłowego:
   ```bash
   python main.py
   ```

2. Wybierz certyfikat  
   Wszystkie zainstalowane certyfikaty z kluczem prywatnym będą widoczne na liście.

3. Dodaj pliki  
   Obsługiwane pliki można dodać przez wybór lub przeciągnij i upuść.

4. Podpisz lub zweryfikuj  
   Podpisuje pliki z użyciem cyfrowego podpisu i timestampu.  
   Weryfikacja sprawdza pojedyncze pliki.

5. Zobacz log  
   Pokazuje wszystkie wykonane operacje wraz ze statusem podpisu i danymi certyfikatu.

6. Informacje  
   Pokazuje status komponentów (np. signtool, SDK) i ikonę programu.

---

## 📁 Wersja gotowa

W folderze `/release` znajduje się skompilowana, podpisana wersja `.exe`.  
Nie wymaga instalacji – wystarczy uruchomić.

## 🖼️ Logo

Dołączony jest plik `logo.ico` – możesz go zastąpić własnym kwadratowym `.ico`.

---

### 📦 Wymagania

Aby **LDCertFix** działał poprawnie, na systemie muszą być obecne:

**1. Python 3.9 lub nowszy**  
*(Tylko przy uruchamianiu z kodu źródłowego)*  
- [Pobierz Pythona](https://www.python.org/downloads/)  
- Zaznacz „Add Python to PATH”  
- Sprawdź instalację:
  ```bash
  python --version
  ```

**2. signtool.exe (część Windows SDK)**  
- [Pobierz Windows SDK](https://developer.microsoft.com/pl-pl/windows/downloads/windows-sdk/)  
- Wystarczy „Signing Tools for Desktop Apps”  
- Ścieżka:
  ```
  C:\Program Files (x86)\Windows Kits\10\bin\<SDK-Version>\x64\signtool.exe
  ```

**3. PowerShell 5.1 lub nowszy**  
- Sprawdź:
  ```powershell
  $PSVersionTable.PSVersion
  ```  
- [Pobierz PowerShell](https://learn.microsoft.com/pl-pl/powershell/scripting/install/installing-powershell)

**4. Certyfikat z kluczem prywatnym w magazynie certyfikatów Windows**  
- Import przykładowy (PowerShell):
  ```powershell
  Import-PfxCertificate -FilePath "C:\Ścieżka\do\twojego.pfx" -CertStoreLocation Cert:\CurrentUser\My
  ```

**5. Biblioteki Pythona (przy wersji źródłowej)**  
- Instalacja:
  ```bash
  pip install -r requirements.txt
  ```
  lub:
  ```bash
  pip install pywin32
  ```

> **Uwaga:**  
> LDCertFix był testowany głównie z certyfikatami **Certum** i aplikacją **SimplySign Desktop**.  
> Kompatybilność z innymi dostawcami (Sectigo, DigiCert, GlobalSign) powinna być możliwa, ale nie została przetestowana.

> **Timestamp:**  
> Domyślny serwer timestamp:  
> `http://timestamp.certum.pl`  
> Możliwy do zmiany w ustawieniach.

---

## 📜 Licencja

Projekt na licencji MIT – darmowy, możliwy do modyfikacji i użycia komercyjnego.  
➡️ Zobacz LICENSE

## 👤 Autor

© 2024–2025 Let's Do. – Właściciel: Peter Seidl  
Kontakt: pseidl@lets-do.media

## ❤️ Współpraca

Pull requesty, sugestie i opinie mile widziane!

---

## 📄 LICENCJA (MIT)

```
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

**LDCertFix** je lehký, přenosný nástroj pro Windows k digitálnímu podepisování a ověřování souborů pomocí stávajících certifikátů pro podepisování kódu.  
Je určen pro IT administrátory, vývojáře a DevOps týmy, které potřebují distribuovat podepsané PowerShell skripty, EXE soubory nebo instalační balíčky.

> 🛡️ Podepiš. 🔎 Ověř. 📋 Protokoluj. — Rychle a přehledně.

---

## 🔧 Funkce

- ✅ Výběr nainstalovaných certifikátů pro podepisování kódu (rozbalovací nabídka)
- 🗃️ Podpora pro `.ps1`, `.exe`, `.dll`, `.msi`, `.ocx`, `.js`, `.vbs`, `.wsf`
- 🔏 Digitální podpis s časovým razítkem (nastavitelný server)
- 🔍 Ověření jednotlivých souborů
- 📜 Podrobný log (podepisování a ověřování)
- 🛠️ Kontrola komponent (`signtool`, Windows SDK, verze PowerShell)
- 🖱️ Jednoduché, intuitivní ovládání
- 📦 Přenosná aplikace, není nutná instalace
- 🌐 Volba jazyka (CZ, DE, EN, PL)

---

## 🚀 Použití

1. Spusť `LDCertFix.exe`  
   Nebo spusť ze složky se zdrojovým kódem:
   ```bash
   python main.py
   ```

2. Vyber certifikát  
   Zobrazí se všechny nainstalované certifikáty s privátním klíčem.

3. Přidej soubory  
   Podporované soubory lze přidat výběrem nebo přetažením.

4. Podepiš nebo ověř  
   Podepsání přidá digitální podpis s časovým razítkem.  
   Ověření zkontroluje jednotlivé soubory a zobrazí výsledek.

5. Zobrazit log  
   Ukazuje úplný záznam všech akcí včetně stavu podpisu a informací o certifikátu.

6. Informační okno  
   Zobrazuje informace o komponentách (např. signtool, SDK verze) a ikonu programu.

---

## 📁 Vydání

V adresáři `/release` se nachází předkompilovaná, digitálně podepsaná verze `.exe`.  
Instalace není nutná – stačí spustit.

## 🖼️ Logo

Součástí je zástupné logo (`logo.ico`) – můžeš ho nahradit vlastním čtvercovým `.ico`.

---

### 📦 Požadavky

Aby **LDCertFix** správně fungoval, musí být v systému dostupné následující komponenty:

**1. Python 3.9 nebo novější**  
*(Pouze při spouštění ze zdrojového kódu)*  
- [Stáhnout Python](https://www.python.org/downloads/)  
- Během instalace zaškrtněte **„Add Python to PATH“**  
- Ověření:
  ```bash
  python --version
  ```

**2. signtool.exe (součást Windows SDK)**  
- [Stáhnout Windows SDK](https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/)  
- Při instalaci stačí vybrat „Signing Tools for Desktop Apps“  
- Cesta:
  ```
  C:\Program Files (x86)\Windows Kits\10\bin\<SDK-Verze>\x64\signtool.exe
  ```

**3. PowerShell 5.1 nebo novější**  
- Ověření:
  ```powershell
  $PSVersionTable.PSVersion
  ```  
- [Stáhnout PowerShell](https://learn.microsoft.com/cs-cz/powershell/scripting/install/installing-powershell)

**4. Certifikát s privátním klíčem ve Windows Certificate Store**  
- Import (PowerShell příklad):
  ```powershell
  Import-PfxCertificate -FilePath "C:\Cesta\k\tvemu.pfx" -CertStoreLocation Cert:\CurrentUser\My
  ```

**5. Python knihovny (pro použití ze zdrojového kódu)**  
- Instalace:
  ```bash
  pip install -r requirements.txt
  ```
  nebo jednotlivě:
  ```bash
  pip install pywin32
  ```

> **Poznámka:**  
> LDCertFix byl testován převážně s certifikáty od **Certum** a aplikací **SimplySign Desktop**.  
> Kompatibilita s jinými poskytovateli (např. Sectigo, DigiCert, GlobalSign) by měla být obecně zajištěna, ale nebyla zatím ověřena.

> **Timestamp:**  
> Výchozí timestamp server:  
> `http://timestamp.certum.pl`  
> Lze změnit v nastavení.

---

## 📜 Licence

Projekt je licencován pod MIT licencí – volně použitelný, upravitelný a použitelný i komerčně.  
➡️ Viz LICENSE

## 👤 Autor

© 2024–2025 Let's Do. – Autor: Peter Seidl  
Kontakt: pseidl@lets-do.media

## ❤️ Přispěj

Pull requesty, návrhy a zpětná vazba jsou vítány!

---

## 📄 LICENCE (MIT)

```
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
