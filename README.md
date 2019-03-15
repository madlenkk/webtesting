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
* účet na [github](https://github.com/)
* editor [např. Atom](https://atom.io/) - postup instalace na [Nauč se Python!](https://naucse.python.cz/course/pyladies/beginners/install-editor/)
* nainstalovaný [Python 3](http://python.org) - postup instalace na [Nauč se Python!](http://naucse.python.cz/lessons/beginners/install/)
* nainstalovaný [git](https://git-scm.com/) - postup instalace na [Nauč se Python!](http://naucse.python.cz/lessons/git/install)
* nainstalovaný webový prohlížeč [Chrome](https://www.google.com/chrome/browser/desktop/index.html)
* nainstalovaný webový ovladač [Google Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

  **NOTE:** Webový ovladač musí být přidán do proměnné `PATH` - postup viz [Instalace webdriveru](https://github.com/madlenkk/webtesting#instalace-webdriveru)


## Použité technologie

* [Python 3](https://python.org)
* [pytest](https://pytest.org/)
* [selenium](https://www.seleniumhq.org/)
* [pytest-selenium](http://pytest-selenium.readthedocs.io/en/latest/)
* [virtualenv](https://virtualenv.pypa.io/en/stable/)
* [Google Chrome](https://www.google.com/chrome/browser/desktop/index.html)
* [chrome webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)


## Instalace webdriveru

Stáhněte webový ovladač [Google Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) a rozbalte zip.

Přidejte `chromedriver` do proměnné `PATH` (aby mohl být spouštěn pythonem).


### Windows

Uložte soubor `chromedriver.exe` kamkoliv (např. do `C:\webdrivers\`) a přidejte cestu k souboru do Environment variables (Path):

  * Otevřete `System Properties/Vlastnosti systému`, zvolte záložku `Advanced/Upřesnit` a klikněte na `Environment variables/Proměnné prostředí`
  * v poli `System variables/Systémové proměnné` vyberte `Path` a klikněte na `Edit/Upravit`
  * klikněte na `New/Nový`, vložte cestu např. `C:\webdrivers\` a potvrďte `OK`

Zkuste spustit ovladač v cmd:
```
chromedriver
```
Odpověď by měla být:
```
Starting ChromeDriver ...
Only local connections are allowed.
```


### Linux

Uložte soubor `chromedriver` kamkoliv na disk.

Vytvořte alias pro `chromedriver` v `/usr/bin/`:
```
sudo ln -s /path/to/chromedriver /usr/bin
```
Zkontrolujte cestu k ovladači:
```
which chromedriver
```
Odpověď by měla být:
```
/usr/bin/chromedriver
```
Zkuste spustit ovladač:
```
chromedriver
```
Odpověď by měla být:
```
Starting ChromeDriver ...
Only local connections are allowed.
```


### macOS

Přesuňte `chromedriver` z `Downloads` do `/usr/local/bin/`
```
sudo mv /Downloads/chromedriver /usr/local/bin/chromedriver
```
Zkontrolujte cestu k ovladači:
```
which chromedriver
```
Odpověď by měla být:
```
/usr/local/bin/chromedriver
```
Otevřete v textovém editoru soubor `paths` - např.:
```
atom /etc/paths
```
Přidejte cestu k ovladači na poslední řádek souboru a uložte:
```
/usr/local/bin/chromedriver
```
**NOTE:** Smažte ostatní cesty k ovladači - pokud jsou v souboru uvedeny.

Zkuste spustit ovladač:
```
chromedriver
```
Odpověď by měla být:
```
Starting ChromeDriver ...
Only local connections are allowed.
```


## Instalace - pokračování

### Naklonování repozitáře

Naklonujte si repozitář `webtesting` do vašeho počítače a vstupte do adresáře:
```
git clone https://github.com/madlenkk/webtesting.git
cd webtesting
```


### Instalace virtualního prostředí

Upgradujte pip:
na Linux/macOS:
```
pip install -U pip
```
na Windows:
```
python -m pip install -U pip
```

Nainstalujte `virtualenv`, vytvořte virtuální prostředí `venv-testing` pro tento projekt:
```
pip install virtualenv
virtualenv -p python venv-testing
```

Aktivujte vytvořené virtuální prostředí:
na Linux/macOS:
```
source venv-testing/bin/activate
```
na Windows:
```
venv-testing\Scripts\activate
```

**NOTE:** Virtualenv může být deaktivován pomocí příkazu `deactivate`.


### Instalace balíčků

S aktivovaným `virtualenv` nainstalujte požadované balíčky ze souboru `requirements.txt` pomocí příkazu `pip` :
```
pip install -r requirements.txt
```

Ověřte, že byla instalace úspěšná, např. pomocí:
```
pytest
```

Odpověď by měla být zhruba následující:
```
======================================== test session starts ========================================
platform linux -- Python 3.6.5, pytest-4.0.1, py-1.7.0, pluggy-0.8.0
sensitiveurl: .*
rootdir: /home/magdalena/dev/webtesting, inifile:
plugins: variables-1.7.1, selenium-1.14.0, metadata-1.7.0, html-1.19.0, base-url-1.4.1
collected 0 items                                                                                   

=================================== no tests ran in 0.01 seconds ====================================
```


## Struktura

V adresáři `webtesting` se nacházejí dva podadresáře:
* `mapotic_testing` - adresář, který obsahuje kompletní funkční testy aplikace Mapotic (vaše nápověda)
* `my_testing` - váš adresář na hraní

Vstupte do adresáře `my_testing`:
```
cd my_testing
```

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
