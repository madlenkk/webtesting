# Testování webových aplikací pomocí Pythonu

*Netrapte sebe nebo svoje kolegy rutinním manuálním proklikáváním. Testy základních funkcí webové aplikace se dají automatizovat během pár hodin a pak už ji budou proklikávat za vás - třeba každou hodinu.*

Co se dozvíte:
* základy testování webových aplikací
* jaké technologie se dají použít pro automatizaci testování webových aplikací v kombinaci s Pythonem a jak je nakonfigurovat

Co si vyzkoušíte:
* společně napíšeme pár testů webové aplikace
* pokud zbyde čas vytvoříte si jednoduchý test vámi zvolené webové aplikace

Co je nutné umět:
* Python na úrovni [začátečnického kurzu](http://naucse.python.cz/course/pyladies/)

Co se hodí umět:
* základy html a css (DOM a selektory)

Materiály:
* https://github.com/madlenkk/webtesting/
* [Prezentace: Web testing using Python](https://docs.google.com/presentation/d/1VgCRlBgvpNuKko2EgmjucdfsCkeyvoPvPqdhGUuDhdY/edit?usp=sharing)
* [Tabulka: Test cases](https://docs.google.com/spreadsheets/d/1uaAEmRhaNE7bwm2cp1tixQ_jNn-wTA5CChBtGvipb8E/edit?usp=sharing)

Co mít připraveno:
* **účet na [github.com](https://github.com/)**
* **editor** [např. Atom](https://atom.io/): viz postup instalace na [Nauč se Python!](https://naucse.python.cz/course/pyladies/beginners/install-editor/)
* **nainstalovaný [Python](http://python.org)** 3.6 nebo vyšší: viz postup instalace na [Nauč se Python!](http://naucse.python.cz/lessons/beginners/install/)
* **nainstalovaný [git](https://git-scm.com/)**: viz postup instalace na [Nauč se Python!](http://naucse.python.cz/lessons/git/install)
* **nainstalovaný webový prohlížeč [Chrome](https://www.google.com/chrome/browser/desktop/index.html).**
  (Případně **Chromium**, máš-li už nainstalovaný ten.)
* **stažený webový ovladač** Google Chrome Driver:
  * Zjistěte svou verzi prohlížeče (viz menu prohlížeče `⋮`, *Nápověda*/*Help*, *O prohlížeči Google Chrome*/*About Google Chrome*).
  * Stáhněte si [archiv s ovladačem](https://sites.google.com/a/chromium.org/chromedriver/downloads) podle své verze prohlížeče. Později archiv rozbalíme na správné místo.


## Použité technologie

* [Python 3](https://python.org)
* [pytest](https://pytest.org/)
* [selenium](https://www.seleniumhq.org/)
* [pytest-selenium](http://pytest-selenium.readthedocs.io/en/latest/)
* [virtualenv](https://virtualenv.pypa.io/en/stable/)
* [Google Chrome](https://www.google.com/chrome/browser/desktop/index.html)
* [chrome webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)


## Příprava prostředí

Vytvořte si na dnešní workshop adresář.
V příkazové řádce se do něj přepněte (pomocí příkazu `cd`).

### Naklonování repozitáře

Naklonujte si repozitář `webtesting` do vašeho počítače a vstupte do adresáře:
```
$ git clone https://github.com/madlenkk/webtesting.git
$ cd webtesting
```

> [note]
> Znak `$` do příkazové řádky nepište – tím jen ukazujeme, že jde o příkazovou řádku.
> (Výzva příkazové řádky končí právě znakem `$`, nebo `>` na Windows.)
> Zadejte tedy jen `git clone https://github.com/madlenkk/webtesting.git` a  `cd webtesting`.

### Vytvoření a aktivace virtuálního prostředí

Následujícími příkazy si vytvořte a aktivujte virtuální prostředí pro tento workshop.

na Linux/macOS:
```
$ python3 -m venv venv-testing
$ source venv-testing/bin/activate
```

na Windows:
```
> py -3 -m venv venv-testing
> venv-testing\Scripts\activate
```

První příkaz (ten s `-m venv`) vytvoří virtuální prostředí. Ten je potřeba zadat jen jednou.

Druhý příkaz (ten s `activate`) prostředí aktivuje; ten je potřeba zadat vždy, když otevřete novou příkazovou řádku a budete v ní chtít začínat testovat. (Je potřeba ho zavolat z aktivního adresáře `webtesting`.)

Aktivované virtuální prostředí poznáš tak, že na začátku příkazové řádky svítí jeho jméno v závorkách: `(venv-testing)`.

**NOTE:** Prostředí může být deaktivováno pomocí příkazu `deactivate` (nebo zavřením příkazové řádky).


### Instalace balíčků pro Python

Ve virtuálním prostředí několik věcí nastavit.
Stačí to udělat jednou (dokud virtuální prostředí nesmažete).

První je aktualizace nástroje `pip`:

```
(venv-testing)$ python -m pip install --upgrade pip
```

> [note]
> Ono `(venv-testing)$` opět do příkazové řádky nepište – tím jen ukazujeme, že má být aktivované virtuální prostředí.
> Zadejte tedy jen `python -m pip install --upgrade pip`.

Druhý je instalace potřebných knihoven pro Python (jejich seznam je v souboru `requirements.txt`):

```
(venv-testing)$ python -m pip install -r requirements.txt
```

### Instalace webového ovladače

Další krok je nastavení webového ovladače.

Archiv s ovladačem, který jste si stáhli výše, si rozbalte do adresáře (`webtesting`).
Přímo v adresáři `webtesting` by tedy teď měl být soubor `chromedriver` (nebo `chromedriver.exe`).

Ten následujícím příkazem zkopírujte na správné místo:

na Linux/macOS:
```
(venv-testing)$ cp chromedriver venv-testing/bin/
```

na Windows:
```
(venv-testing)$ copy chromedriver.exe venv-testing\Scripts\
```

Pro kontrolu zkuste ovladač spustit:
```
(venv-testing)$ chromedriver
```
Odpověď by měla být:
```
Starting ChromeDriver ...
Only local connections are allowed.
```

Ovladač ukončete pomocí <kbd>Ctrl</kbd>+<kbd>C</kbd>.


### Vyzkoušení

Tím je příprava hotová.
Ověřte ještě, že všechno funguje: přejděte do adresáře `my_testing` a spusťte příkaz `pytest`:

```
(venv-testing)$ cd my_testing
(venv-testing)$ pytest
```

Odpověď by měla být zhruba následující:
```pytest
======================================== test session starts ========================================
platform linux -- Python 3.6.5, pytest-4.0.1, py-1.7.0, pluggy-0.8.0
sensitiveurl: .*
rootdir: /home/magdalena/dev/webtesting, inifile:
plugins: variables-1.7.1, selenium-1.14.0, metadata-1.7.0, html-1.19.0, base-url-1.4.1
collected 0 items                                                                                   

=================================== no tests ran in 0.01 seconds ====================================
```


## Struktura projektu

V adresáři `webtesting` se nacházejí dva podadresáře:
* `mapotic_testing` - adresář, který obsahuje kompletní funkční testy aplikace Mapotic (vaše nápověda)
* `my_testing` - váš adresář na hraní

V adresáři `my_testing` pak je:

* `test.py` - file with main functions to run the tests - calls another test scripts from directory `tests`
* `conftest.py` - global setting of all tests
* `pytest.ini` - default options and markers
* `variables.json` - variables used in tests
* `tests` - directory with test scripts


## Spouštění testů

Vše potřebné je nainstalováno a virtuální prostředí je aktivováno?
V adresáři `my_testing` spusťte připravený soubor `test.py`:
```
pytest test.py -k test_setup
```

Pytest by měl otevřít webový prohlížeč, provést krátký test a zase ho zavřít.
V konzoli by mělo být asi toto:
```
======================================== test session starts ========================================
platform linux -- Python 3.6.5, pytest-4.0.1, py-1.7.0, pluggy-0.8.0
driver: Chrome
sensitiveurl: none
baseurl: https://www.mapotic.com?utm_source=testworkshops&utm_medium=workshop&utm_campaign=magdatests
rootdir: /home/magdalena/dev/webtesting/mapotic_testing, inifile: pytest.ini
plugins: variables-1.7.1, selenium-1.14.0, metadata-1.7.0, html-1.19.0, base-url-1.4.1
collected 2 items / 1 deselected                                                                    

test.py .                                                                                     [100%]

------ generated html file: /home/magdalena/dev/webtesting/mapotic_testing/reports/report.html ------
============================== 1 passed, 1 deselected in 5.12 seconds ===============================
```

### Options

Default options are defined in `pytest.ini`.

* `test.py`
* `--base-url` - set url of tested application (default is defined in `pytest.ini`)
* `--html` - set filename of output log (default is defined in `pytest.ini`)
* `--driver` - set browser used for testing (default is defined in `pytest.ini`)
* `--variables` - set path to variables file (default is defined in `pytest.ini`)
* `-v`, `-vv`, `-vvv` - verbose - use to increase verbosity of test log
* `--stop` - use if you don't want browser to be closed in case of test failure
* `-k` - specify tests to be run
* `-m` - specify a Test Suite to be run (available markers are defined in `pytest.ini`)

**NOTE:** Pytest v daném adresáři vyhledá a spustí sám od sebe vše, co začíná slovem test, pokud mu pomocí options `-k` nebo -`m` nespecifikujeme, co pustit chceme.

e.g.:
```
pytest test.py -vvv --stop -m complex
```

To learn more about `pytest` and its options, use:

```
pytest --help
```
