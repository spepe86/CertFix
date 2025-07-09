
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
- Zertifikate z. B. von [Certum](https://www.certum.eu), [Sectigo](https://sectigo.com/), [DigiCert](https://www.digicert.com/), [GlobalSign](https://www.globalsign.com/)
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
- Certificates e.g. from [Certum](https://www.certum.eu), [Sectigo](https://sectigo.com/), [DigiCert](https://www.digicert.com/), [GlobalSign](https://www.globalsign.com/)
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

# LDCertFix

---

## 🇵🇱 Polski

**LDCertFix** to lekkie, przenośne narzędzie Windows do cyfrowego podpisywania i weryfikacji plików przy użyciu istniejących certyfikatów Code Signing.  
Przeznaczone dla administratorów IT, programistów oraz zespołów DevOps, które muszą dystrybuować podpisane skrypty PowerShell, pliki EXE lub pakiety instalacyjne.

> 🛡️ Podpisz. 🔎 Zweryfikuj. 📋 Zaloguj. — Szybko i przejrzyście.

### 🔧 Funkcje

- ✅ Wybór zainstalowanych certyfikatów Code Signing (lista rozwijana)
- 🗃️ Obsługa: `.ps1`, `.exe`, `.dll`, `.msi`, `.ocx`, `.js`, `.vbs`, `.wsf`
- 🔏 Podpis cyfrowy z sygnaturą czasową (konfigurowalny serwer)
- 🔍 Weryfikacja pojedynczych plików i masowa
- 📜 Szczegółowy log (podpisywanie i weryfikacja)
- 🛠️ Test komponentów: `signtool`, Windows SDK, wersja PowerShell
- 🖱️ Prosta, intuicyjna obsługa
- 📦 Przenośny – nie wymaga instalacji

### 🚀 Użycie

1. Uruchom `LDCertFix.exe`  
   Lub w folderze źródłowym:
   ```bash
   python main.py
   ```
2. Wybierz certyfikat  
   Wszystkie zainstalowane certyfikaty z kluczem prywatnym pojawią się na liście.

3. Dodaj pliki  
   Obsługiwane pliki można dodać przez okno dialogowe lub przeciągnij i upuść.

4. Podpisz lub zweryfikuj  
   - Podpisywanie dołącza podpis cyfrowy z sygnaturą czasową.
   - „Zweryfikuj wszystko” sprawdza wszystkie dodane pliki.
   - „Zweryfikuj plik” umożliwia pojedynczą weryfikację.

5. Pokaż log  
   Wyświetla pełny log wszystkich operacji wraz ze statusem podpisu i szczegółami certyfikatu.

6. Okno informacyjne  
   Pokazuje szczegóły zainstalowanych komponentów (np. signtool, wersja SDK itp.)

---

### 📦 Wymagania i instalacja

Aby **LDCertFix** działał poprawnie, upewnij się, że na Twoim systemie są obecne następujące komponenty:

**1. Python 3.9 lub nowszy**  
*(Wymagane tylko przy uruchamianiu ze źródła.)*
- [Pobierz Python](https://www.python.org/downloads/)
- W trakcie instalacji zaznacz „Add Python to PATH”!
- Sprawdź wersję:
  ```bash
  python --version
  ```

**2. signtool.exe (część Windows SDK)**  
- [Pobierz Windows SDK](https://developer.microsoft.com/pl-pl/windows/downloads/windows-sdk/)
- Wystarczy wybrać „Signing Tools for Desktop Apps”.
- Sprawdź ścieżkę:
  ```
  C:\Program Files (x86)\Windows Kitsin\<SDK-Version>d\signtool.exe
  ```

**3. PowerShell w wersji 5.1 lub nowszej**
- Sprawdź wersję:
  ```powershell
  $PSVersionTable.PSVersion
  ```
- [Pobierz PowerShell](https://learn.microsoft.com/pl-pl/powershell/scripting/install/installing-powershell)

**4. Certyfikat z kluczem prywatnym w magazynie certyfikatów Windows**
- Certyfikaty np. od [Certum](https://www.certum.eu), [Sectigo](https://sectigo.com/), [DigiCert](https://www.digicert.com/), [GlobalSign](https://www.globalsign.com/)
- Import (przykład PowerShell):
  ```powershell
  Import-PfxCertificate -FilePath "C:\Sciezka\do	wojego.pfx" -CertStoreLocation Cert:\CurrentUser\My
  ```

**5. Dodatkowe zależności Python (przy uruchamianiu ze źródła)**
- Instalacja:
  ```bash
  pip install -r requirements.txt
  ```
  lub pojedynczo:
  ```bash
  pip install pywin32
  ```

> **Uwaga:**  
> LDCertFix był do tej pory testowany wyłącznie z certyfikatami Code Signing od **Certum** oraz aplikacją **SimplySign Desktop**.  
> Kompatybilność z innymi dostawcami certyfikatów (np. Sectigo, DigiCert, GlobalSign) jest możliwa, ale nie została jeszcze potwierdzona.

> **Serwer sygnatury czasowej:**  
> Domyślnie używany jest serwer  
> `http://timestamp.certum.pl`  
> Serwer można zmienić w ustawieniach.

---

### 🛠️ Szybki test

Po instalacji wszystkich komponentów możesz sprawdzić ich obecność w oknie informacyjnym **LDCertFix**.

---

### 📁 Wersja

W katalogu `/release` znajduje się skompilowana, cyfrowo podpisana wersja `.exe`.  
Nie wymaga instalacji – po prostu uruchom.

---

### 🖼️ Ikona

W repozytorium znajduje się plik zastępczy (`logo.ico`).  
Możesz go zastąpić własnym kwadratowym plikiem `.ico`.

---

### 📜 Licencja

Projekt dostępny na licencji MIT – do dowolnego użytku, modyfikacji i zastosowań komercyjnych.  
➡️ Patrz LICENSE

---

### 👤 Autor

© 2024–2025 Let's Do. – właściciel: Peter Seidl  
Kontakt: pseidl@lets-do.media

---

### ❤️ Współpraca

Zgłoszenia, sugestie i opinie są zawsze mile widziane!

---

### 📄 LICENCJA (MIT)

```plaintext
MIT License

Copyright (c) 2025 Let's Do. – właściciel: Peter Seidl

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

## 🇨🇿 Čeština

**LDCertFix** je lehký, přenosný nástroj pro Windows k digitálnímu podepisování a ověřování souborů pomocí existujících certifikátů Code Signing.  
Je určen IT administrátorům, vývojářům a DevOps týmům, kteří potřebují distribuovat podepsané PowerShell skripty, EXE soubory nebo instalační balíčky.

> 🛡️ Podepisuj. 🔎 Ověřuj. 📋 Loguj. — Rychle a přehledně.

### 🔧 Funkce

- ✅ Výběr nainstalovaných Code Signing certifikátů (dropdown)
- 🗃️ Podpora: `.ps1`, `.exe`, `.dll`, `.msi`, `.ocx`, `.js`, `.vbs`, `.wsf`
- 🔏 Digitální podpis s časovým razítkem (nastavitelný server)
- 🔍 Ověření jednoho i více souborů najednou
- 📜 Podrobný log (podepisování i ověřování)
- 🛠️ Test komponent: `signtool`, Windows SDK, verze PowerShell
- 🖱️ Jednoduché a intuitivní ovládání
- 📦 Přenosné – není nutná instalace

### 🚀 Použití

1. Spusťte `LDCertFix.exe`  
   Nebo spusťte ze zdrojového adresáře:
   ```bash
   python main.py
   ```
2. Vyberte certifikát  
   V seznamu se zobrazí všechny nainstalované certifikáty s privátním klíčem.

3. Přidejte soubory  
   Podporované soubory lze přidat přes dialogové okno nebo přetažením.

4. Podepište nebo ověřte  
   - Podepsání přidá digitální podpis s časovým razítkem.
   - „Ověřit vše“ zkontroluje všechny přidané soubory.
   - „Ověřit soubor“ umožňuje jednotlivé ověření.

5. Zobrazit log  
   Zobrazí kompletní záznam všech akcí včetně stavu podpisu a detailů certifikátu.

6. Informační okno  
   Zobrazí informace o nainstalovaných komponentách (např. signtool, verze SDK apod.)

---

### 📦 Závislosti a instalace

Aby **LDCertFix** fungoval správně, ujistěte se, že máte v systému následující komponenty:

**1. Python 3.9 nebo novější**  
*(Vyžadováno pouze při spouštění ze zdrojového kódu.)*
- [Stáhnout Python](https://www.python.org/downloads/)
- Během instalace zaškrtněte „Add Python to PATH“!
- Ověření verze:
  ```bash
  python --version
  ```

**2. signtool.exe (součást Windows SDK)**  
- [Stáhnout Windows SDK](https://developer.microsoft.com/cs-cz/windows/downloads/windows-sdk/)
- Stačí vybrat „Signing Tools for Desktop Apps“.
- Zkontrolujte cestu:
  ```
  C:\Program Files (x86)\Windows Kitsin\<SDK-Version>d\signtool.exe
  ```

**3. PowerShell verze 5.1 nebo novější**
- Ověření verze:
  ```powershell
  $PSVersionTable.PSVersion
  ```
- [Stáhnout PowerShell](https://learn.microsoft.com/cs-cz/powershell/scripting/install/installing-powershell)

**4. Certifikát s privátním klíčem ve Windows certifikátovém úložišti**
- Certifikáty např. od [Certum](https://www.certum.eu/cz/), [Sectigo](https://sectigo.com/), [DigiCert](https://www.digicert.com/), [GlobalSign](https://www.globalsign.com/)
- Import (PowerShell příklad):
  ```powershell
  Import-PfxCertificate -FilePath "C:\Cesta\k	vemu.pfx" -CertStoreLocation Cert:\CurrentUser\My
  ```

**5. Další Python závislosti (při použití zdrojového kódu)**
- Instalace:
  ```bash
  pip install -r requirements.txt
  ```
  nebo jednotlivě:
  ```bash
  pip install pywin32
  ```

> **Poznámka:**  
> LDCertFix byl dosud testován pouze s Code Signing certifikáty od **Certum** a aplikací **SimplySign Desktop**.  
> Kompatibilita s dalšími poskytovateli certifikátů (Sectigo, DigiCert, GlobalSign) by měla být zajištěna, ale dosud nebyla ověřena.

> **Timestamp server:**  
> Výchozí timestamp server je  
> `http://timestamp.certum.pl`  
> Server lze změnit v nastavení.

---

### 🛠️ Rychlý test

Po instalaci všech komponent můžete jejich přítomnost ověřit v informačním okně **LDCertFix**.

---

### 📁 Vydání

Ve složce `/release` je předkompilovaná, digitálně podepsaná verze `.exe`.  
Není nutná instalace – stačí spustit.

---

### 🖼️ Ikona

V repozitáři je obsažen zástupný soubor (`logo.ico`).  
Můžete jej nahradit vlastním čtvercovým `.ico` souborem.

---

### 📜 Licence

Projekt je dostupný pod licencí MIT – volné použití, úpravy i komerční využití.  
➡️ Viz LICENSE

---

### 👤 Autor

© 2024–2025 Let's Do. – vlastník: Peter Seidl  
Kontakt: pseidl@lets-do.media

---

### ❤️ Přispějte

Pull requesty, návrhy a zpětná vazba jsou vítány!

---

### 📄 LICENCE (MIT)

```plaintext
MIT License

Copyright (c) 2025 Let's Do. – vlastník: Peter Seidl

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
