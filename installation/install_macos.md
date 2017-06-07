# Instalace pro macOS

## Instalace ovladače

Teď si nainstalujeme ovladač (driver) pro Chrome - Google Chrome Driver

Ovladač najdeš na stránce až po scrollování kousek níž [zde](http://docs.seleniumhq.org/download/)

Stáhni si Google Chrome Driver do složky `WebDrivers`. 
![Ovladače najdeš na stránce až po scrollování kousek níž.](https://github.com/PyLadiesCZ/TestLadies/blob/master/img/all_os_drivers_install.png)
Pote jdi do nastavení Macbooku (System Preferences -> Security & Privacy) a zde se po kliknutí na zámeček vlevo dole přihlaš. Pravděpodobně nad ním budeš mít informaci, že `chromedriver` je blokovan. Povol jeho otevirani na trvalo. 

## Nastavení cesty (PATH) k ovladači

Nastavení PATH pro Chrome na macOS dá trochu práce. Řeší to řádek `browser = webdriver.Chrome('chromedriver')` v souboru `test_installation.py`. 
Driver pro Chrome musíš mít přesunutý ve složce `WebDrivers` s projektem, ale je i tak potřeba nastavit PATH. 

**Postup je následující:**

1. Stažený `chromedriver` přesuň z `Downloads` složky do složky `WebDrivers`, kterou jsi si vytvořila v ~/TestLadies.

2. Otevři Terminál.

3. Zadej příkaz `sudo nano /etc/paths`.

4. Vyplň své heslo (ano, heslo je při psaní skryté úmyslně).

5. Otevřel se editor `nano`, šipkami sjeď na poslední volný řádek a přidej cestu do složky `WebDrivers`

6. Pokud jsi se řídil/a instrukcemi, měla bys mít `WebDrivers` složku v projektu TestLadies, cesta by měla být `/Users/name/slozka_kde_delas_bezne_projekty/TestLadies/WebDrivers`,
 kde `name` je jméno tvého účtu na kterém jsi přihlášená. Za ním vyplň celou cestu do složky `WebDrivers`. 

7. Ulož cestu v `nano` editoru příkazy: control + x, Y, enter.

8. Vypni a zapni Terminál (změny se projeví až po jeho restartování). Zadej příkaz `echo $PATH`, měla by jsi již vidět přidanou cestu.

9. Hurááá, teď budou naše testy fungovat v Chrome. Tento řádek nám umožňuje prohlížeč spustit a provést v něm test.

```
browser.get('http://seleniumhq.org/')
```
