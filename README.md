# Web testing using Python

*a workshop by Magdalena Kabátová for PyCon CZ 2017*

*Write and run automated tests of web applications in few hours and let it work for you since then. First brief introduction to web testing will be given. Then we will use pytest and Selenium frameworks to create automated tests of a demo web page.*

*Basic knowledge of Python is required (suitable for PyLadies). Basic knowledge of html and css (DOM and selectors) is advantage.*

*Requirements: Python 3, Chrome, Git, GitHub account, others will be installed in the workshop.*

## Potřebné technologie

Před zahájením workshopu potřebujete mít:

* nainstalovaný [Python 3](http://python.org) - postup instalace na [Nauč se Python!](http://naucse.python.cz/lessons/beginners/install/)
* nainstalovaný webový prohlížeč [Chrome](https://www.google.com/chrome/browser/desktop/index.html)
* nainstalovaný [git](https://git-scm.com/) - postup instalace na [Nauč se Python!](http://nau2cse.python.cz/lessons/git/install)
* účet na [github](https://github.com/)


Další technologie nainstalujeme během workshopu:

* [pytest](http://pytest.org/) - The pytest framework makes it easy to write
  small tests, yet scales to support complex functional testing for applications
  and libraries. We use it, because it's better then standard Python Unittest
* [selenium](http://www.seleniumhq.org/) - Selenium automates browsers.
  Primarily, it is for automating web applications for testing purposes.
* [pytest-selenium](http://pytest-selenium.readthedocs.io/en/latest/) -
  pytest-selenium is a plugin for py.test that provides support for running
  Selenium based tests.
* [Google Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads) - ovladač webového prohlížeče Chrome
* [virtualenv](https://virtualenv.pypa.io/en/stable/) - virtualenv is a tool to
  create isolated Python environments.

## Instalace

1. Otevřete konzoli a vstupte do vámi zvolené složky:
```
cd my_projects
```

1. Naklonujte si repozitář `webtesting` z githubu a vstupte do složky `webtesting`:
```
git clone https://github.com/madlenkk/webtesting.git
cd webtesting
```

1. Vytvořte virtuální prostředí:
```
virtualenv -p python3 venv-tests
```

1. Spusťte virtuální prostředí:

  * Windows:
```
> venv-tests\Scripts\activate.bat
```

   V případě potíží, restartujte bash.

  * Linux/macOS:
```
$ source venv-tests/bin/activate
```

1. Do vitruálního prostředí nainstalujte potřebné balíky uvedené v souboru `requirements.txt` pomocí `pip`:
```
pip install -r requirements.txt
```

Úspěšnost této instalace můžete ověřit například pomocí příkazu:
```
pytest --version
```

1. Proveďte instalaci a nastavení webového ovladače:

* [Windows](installation/install_windows.md)
* [Linux](installation/install_linux.md)
* [macOS](installation/install_macos.md)

Stáhněte a nainstalujte [Google Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

Přidejte `chromedriver` do adresáře `$PATH`:

  * Windows: Exportujte zip, uložte soubor chromedriver.exe a přidejte cestu k souboru do Environment Variables (PATH).

  * Linux: Exportujte zip do `/usr/local/bin/`.

1. Správné nastavení webdriveru ověřte spuštěním zkušební testu, který se nachází ve složce `installation`:
```
python installation/test_installation.py
```
Pokud je vše v pořádku, spustí se prohlížeč, provede se test, prohlížeč se opět vypne a v konzoli se vypíše výsledek testu.
Proveďte úkon, který jste našli ve vaší konzoli.


## Spuštění testů

Všechny testy jsou uloženy ve složce `tests` a rozděleny do podsložek podle Test Suites. 

Před spuštěním testů, je potřeba:
* mít aktivované virtuální prostředí `venv-tests`
* být ve složce `tests`

Vaše konzole by tedy měla vypisovat zhruba toto:
* Linux:
```
(venv-tests) user: ~/webtesting/tests $
```

Všechny testy ve složce `tests` spustíte pomocí příkazu:
```
pytest
```

Pokud chcete spouštět testy jednotlivě, přidejte cestu k souboru s daným testem - např.:
```
pytest test_suite_02_login/test_case_01_valid_login.py
```

Probíhající test můžete přerušit zavřením prohlížeče, ve kterém test probíhá, nebo v konzoli pomocí:
```
CTRL + C
```

## Konfigurace testů

Rozmanitá konfigurace je uložena v souboru [pytest.ini](tests/pytest.ini), díky kterému není potřeba vypisovat parametry do konzole. Nicméně vypsáním parametrů do konzole lze výchozí konfiguraci přebýt nebo doplnit o další parametry.
```
pytest --html=reports/report_all.html -
```

Více o jednotlivých parametrech se dozvíte pomocí:
```
pytest --help
```

## Proměnné

V testech jsou použity proměnné, které jsou odděleny od kódu a najdete je v souboru: `variables.json` ve složce `tests`.

Proveďte registraci na [testovacím eshopu](http://testshop.pyladies.cz/accounts/login/).

Otevřete soubor `variables.json` a přepište hodnoty proměnných na vaše vlastní - `username` a `password` se musí shodovat s údaji, které jste vyplnili při registraci.
