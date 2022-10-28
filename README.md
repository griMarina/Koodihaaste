# Koodihaaste 2022
Solidabiksen Koodihaaste - Ruokarähinä


Käytetyt tekniikat / käyttöjärjestelmä:

* Python, macOS-käyttöjärjestelmää 

Käynnistys:

* cd Koodihaaste/
* python -m venv env_name	
* source env_name/bin/activate 
* pip install -r requirements.txt 
* python3 main.py

Ratkaisu:

* dictionary.csv  - sisältää tuotenimet; englanninkielisen nimellä haetaan ravintosisällöt API:sta
* winner.txt - sisältää viimeisen taistelun voittajan nimen; jos tiedosto ei ole tyhjä, voittaja menee seuraavaan taisteluun, vastustaja määritetään satunnaisesti tiedostosta dictionary.csv
* fighter.py - sisältää luokan Fighter
* main.py - luodaan objekteja fighter1 ja fighter2; nimitetään vastustajia; luodaan attack funktion, johon välitämme objektin, joka iskee välillä delay. Tarkistetaan sitten, onko se voittaja osumisen jälkeen. Silmukassa for ajetaan attack funktiota välillä 0-100. Oletetaan, että voittaja selviää sadassa vedossa. Jos ei, se on ERITTÄÄÄÄIN pitkä taistelu ;)
