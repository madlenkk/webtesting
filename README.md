# Web testing using Python

*a workshop by Magdalena Kabátová for PyCon CZ 2017*

*Write and run automated tests of web applications in few hours and let it work for you since then. First brief introduction to web testing will be given. Then we will use pytest and Selenium frameworks to create automated tests of a demo web page.*

*Basic knowledge of Python is required (suitable for PyLadies). Basic knowledge of html and css (DOM and selectors) is advantage.*


## Potřebné technologie

Před zahájením workshopu potřebujete mít:

* nainstalovaný [Python 3](http://python.org) - postup instalace na [Nauč se Python!](http://naucse.python.cz/lessons/beginners/install/)
* nainstalovaný webový prohlížeč [Chrome](https://www.google.com/chrome/browser/desktop/index.html)
* nainstalovaný [git](https://git-scm.com/) - postup instalace na [Nauč se Python!](http://nau2cse.python.cz/lessons/git/install)
* účet na [github](https://github.com/)

Ostatní nainstalujeme během workshopu.


## Obsah workshopu

* Zahájení
* Úvod do testování SW
* Příprava na testování
* Automatické testování


## Úvod do testování SW

* [Přednáška](https://www.youtube.com/watch?v=3YekbncInhU) na PyCon CZ 2016


## Příprava na testování

* Testovací eshop: http://testshop.pyladies.cz

* Testovací scénáře: https://goo.gl/8bXLte

**Úkol:** Zaregistrujte se na [testovacím eshopu](http://testshop.pyladies.cz/accounts/login/). Email může být smyšlený, ale zapamatujte si ho.


## Automatické testování

### Použité technologie:

* [Python 3](http://python.org)
* [virtualenv](https://virtualenv.pypa.io/en/stable/) - nástroj pro tvorbu izolovaných Python prostředí
* [pytest](http://pytest.org/) - testovací framework pro Python (alternativou je Python unittest modul)
* [Selenium](http://www.seleniumhq.org/) - nástroj pro automatické testování webových aplikací, dokumentace [Selenium with Python](http://selenium-python.readthedocs.io/locating-elements.html)
* [pytest-selenium](http://pytest-selenium.readthedocs.io) - selenium plugin pro pytest
* webový prohlížeč [Chrome](https://www.google.com/chrome/browser/desktop/index.html)
  Proč Chrome? [Proto!](http://www.zive.cz/clanky/valka-prohlizecu-v-roce-2016-ie-mizi-ze-sceny-a-vsechno-bere-chrome/sc-3-a-185443/default.aspx)
* [Google Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) - ovladač webového prohlížeče Chrome
* verzovací systém [git](https://git-scm.com/) a webová služba [github](https://github.com/)


### Instalace

1. Otevřete https://github.com/madlenkk/webtesting, přihlašte se a proveďte fork na svůj github (tlačítko vpravo nahoře).

2. Otevřete konzoli a vstupte do vámi zvolené složky:
  ```
  cd my_projects
  ```

3. Naklonujte si repozitář `webtesting` z vašeho githubu a vstupte do složky `webtesting`:
  ```
  git clone https://github.com/[your_name]/webtesting.git
  cd webtesting
  ```

4. Vytvořte virtuální prostředí:
  ```
  virtualenv -p python3 venv-tests
  ```

5. Spusťte virtuální prostředí:

  * Windows:
  ```
  > venv-tests\Scripts\activate.bat
  ```
   *Pozn.: V případě potíží, restartujte bash.*

  * Linux/macOS:
  ```
  $ source venv-tests/bin/activate
  ```

6. Do vitruálního prostředí nainstalujte potřebné balíky uvedené v souboru [`requirements.txt`](requirements.txt) pomocí `pip`:
  ```
  pip install -r requirements.txt
  ```
  Úspěšnost této instalace můžete ověřit například pomocí příkazu:
  ```
  pytest --version
  ```
  Pokud se instalace nezdařila, pravděpodobně budete muset nainstalovat `pip` pro python3. Vygooglete si, jak na to na vašem OS.

7. Proveďte instalaci a nastavení webového ovladače:

  * [Windows](installation/install_windows.md)
  * [Linux](installation/install_linux.md)
  * [macOS](installation/install_macos.md)

  Stáhněte a nainstalujte [Google Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads).
  Přidejte `chromedriver` do adresáře `$PATH`:
    * Windows: Exportujte zip, uložte soubor chromedriver.exe a přidejte cestu k souboru do Environment Variables (PATH).
    * Linux: Exportujte zip do `/usr/local/bin/`.

8. Správné nastavení webdriveru ověřte spuštěním zkušební testu [`installation.py`](installation/test_installation.py), který se nachází ve složce `installation`:
  ```
  python installation/test_installation.py
  ```
  Pokud je vše v pořádku, spustí se prohlížeč, provede se test, prohlížeč se opět vypne a v konzoli se vypíše výsledek testu. 
  Sledujte, co se děje v prohlížeči a následně proveďte úkon, který test vypsal do vaší konzole.


### Spuštění testů

Všechny testy jsou uloženy ve složce [`tests`](tests) a rozděleny do podsložek podle testovacích scénářů (suites). 

Před spuštěním testů, je potřeba:
* mít aktivované virtuální prostředí `venv-tests`
* být ve složce `tests`

Vaše konzole by tedy měla vypisovat zhruba toto: `(venv-tests) username: ~/webtesting/tests $` (Linux).

Všechny testy ve složce `tests` můžete spustit pomocí příkazu:
```
pytest
```

Pytest spouští automaticky všechny soubory a funkce začínající slovem `test`, které najde v akutální složce a jejích podsložkách. I ty musejí začínat slovem `test`.

Pokud chcete spouštět testy jednotlivě, přidejte cestu k souboru s daným testem - např.:
```
pytest test_suite_02_login/test_case_02_invalid_login.py
```

Probíhající test můžete přerušit zavřením prohlížeče, ve kterém test probíhá, nebo v konzoli pomocí `CTRL + C` (Linux).


### Konfigurace testů

Rozmanitá konfigurace je uložena v souboru [`pytest.ini`](tests/pytest.ini), díky kterému není potřeba vypisovat parametry do konzole. Nicméně vypsáním parametrů do konzole lze výchozí konfiguraci přebýt nebo doplnit.
```
pytest --html=reports/another_report.html
```

Více o jednotlivých parametrech se dozvíte pomocí:
```
pytest --help
```
nebo v dokumentaci k [pytest](https://docs.pytest.org/en/latest/customize.html).


### Proměnné

V jednotlivých testech jsou použity proměnné, které jsou odděleny od kódu a najdete je v souboru [`variables.json`](tests/variables.json).

**Úkol:** Otevřete soubor `variables.json` v textovém editoru a přepište hodnoty proměnných na vaše vlastní - `username` a `password` se musí shodovat s údaji, které jste vyplnili při registraci do testovacího eshopu. 
Spusťte test pro **validní** přihlášení a html report nechte vypsat do souboru `reports/01_valid_login.html`.


### Psaní testů

* v každém testu je nejprve nutné naimportovat moduly ze selenia a pytest
* název hlavní funkce musí začínat slovem `test`
* elementy na stránce se lokalizují pomocí: `find_element(By.[metoda])`
  * ID
  * CLASS_NAME
  * CSS_SELECTOR
  * XPATH
  * ... - více v dokumentaci [Selenium with Python](http://selenium-python.readthedocs.io/locating-elements.html)
* ověření se provádí pomocí `assert` - více v dokumentaci k [pytest](https://docs.pytest.org/en/latest/assert.html)


### Inspektor (DevTools)

* `F12` nebo  `CTRL + SHIFT + I` - zapne/vypne inspektor
* jednotlivé elementy stránky lze prozkoumávat pomocí: `CTRL + SHIFT + C` v inspektoru + levé tlačítko myši na element na stránce nebo: pravé tlačítko myši na element na stránce + Prozkoumat
* vyhledávat elementy v inspektoru lze pomocí: `CTRL + F`
* `F8` v inspektoru - zamrazí/rozmrazí webový prohlížeč


### Reporty

Pytest umí generovat přehledné html reporty včetně screenshotů. Nastavují se pomocí parametru `--html` v souboru `pytest.ini` nebo přímo v konzoli při spouštění `pytest`.
Více v dokumentaci k [pytest-selenium](http://pytest-selenium.readthedocs.io/en/latest/user_guide.html#html-report).


## Úkoly

1. Napište test na odhlášení z testovacího eshopu - podle testovacího scénáře 06_logout.
  * soubor uložte do složky pro příslušný test suite: `test_suite_06_logout` a pojmenujte ho: `test_case_01_logout_**[vase_jmeno]**.py`
  * využijte v něm už hotové funkce  - např. `test_case_01_valid_login.py`
  * uložte a spusťte test
  * pokud test prošel, vypublikujte ho na váš github
  ```git add test_suite_06_logout/test_case_01_logout_**[vase_jmeno]**.py
     git commit --all --message "Ading my test for logout"
     git push
  ```
  * jděte na váš github a proveďte pull request (tlačítko `new-pull-request-btn` vyhledejte na stránce pomocí inspektoru)
 
 2. Vyberte si libovolnou webovou stránku a vymyslete a naprogramujte jednoduchý test této stránky.
  * sepiště si testovací scénář (a nebo ne - je to na vás)
  * ve složce `webtesting` vytvořte novou složku s názvem `tests_**[vase_jmeno]**`
  * do této složky zkopírujte soubor `tests/pytest.ini` a do parametru `base_url` vložte url vaší testované aplikace 
  * vytvořte nový soubor např. `test.py` (nemusíte řešit zařazení do podsložek - je to na vás) a naprogramujte test podle scénáře (a nebo ne - je to na vás)
  * uložte a spusťte test
  * pokud test prošel, vypublikujte ho na váš github
  ```git add tests_**[vase_jmeno]**
     git commit --all --message "Adding my own test"
     git push
  ```
  * jděte na váš github a proveďte pull request (tlačítko `new-pull-request-btn` vyhledejte na stránce pomocí inspektoru)
  
