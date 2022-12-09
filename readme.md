## Description
Vpn changer finder for linux and windows with scraper

## Version
You need to have python 3.10.6 installed

## How to use without changing the vpn?

```bash

git clone https://github.com/Ediannys/but-python.git

cd but-python

pip install pipenv

pipenv shell

pipenv install

cd windows
pipenv run python search.windows.py

```

## How to use changing the vpn?

- You must have protonvpn-cli installed [How to install early-access Proton VPN Linux CLI](https://protonvpn.com/support/linux-vpn-tool-early-access/)

```bash
# Login with Proton VPN credentials.
protonvpn-cli login <pvpn_username>

git clone https://github.com/Ediannys/but-python.git

cd but-python

pip install pipenv

pipenv shell

pipenv install

cd linux
pipenv run python search.linux.py

```

## How to modify the list of search terms

- The first line must be numeric. Represents the number of pages in which you want to search
- The rest of the lines are the words or phrases you want to search for separated by line breaks.
- Example : search.file.txt:

```
12
Pencil
Pen
Crayon
Marker
Color Pencil
sharpener
scissors
```




