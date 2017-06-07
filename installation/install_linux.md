# Instalace pro Linux

## Instalace ovladače

Teď si nainstalujeme ovladač (driver) pro Chrome - Google Chrome Driver.

Balík s ovladačem chromedriver stáhneme z [webu](https://sites.google.com/a/chromium.org/chromedriver/downloads/) pomocí příkazu `wget`

* pro Linux 32bit:
```
wget https://chromedriver.storage.googleapis.com/2.27/chromedriver_linux32.zip
```
* pro Linux 64bit:
```
wget https://chromedriver.storage.googleapis.com/2.27/chromedriver_linux64.zip
```

Rozbalíme ho pomocí `unzip`

* pro Linux 32bit:
```
unzip chromedriver_linux32.zip
```
* pro Linux 64bit:
```
unzip chromedriver_linux64.zip
```

## Nastavení cesty (PATH) k ovladači

Aby byl ovladač spustitelný z prográmků, které budeme tvořit, je třeba ho přidat do proměnné prostředí `$PATH`. Nainstalovaný ovladač chromedriver proto přesuneme do `/usr/local/bin/`: 
```
sudo mv chromedriver /usr/local/bin/
```

Ověříme, že je na správném místě a že je spustitelný: 
```
which chromedriver
```