 _____                _                
|  __ \              | |               
| |__) |___  __ _  __| |_ __ ___   ___ 
|  _  // _ \/ _` |/ _` | '_ ` _ \ / _ \
| | \ \  __/ (_| | (_| | | | | | |  __/
|_|  \_\___|\__,_|\__,_|_| |_| |_|\___|
                                     
 _   _  _____   _  __                _             
| \ | |/ ____| | |/ /               | |             
|  \| | (___   | ' / __ _  __ _ _ __| |_ ___ _ __   
| . ` |\___ \  |  < / _` |/ _` | '__| __/ _ \ '_ \  
| |\  |____) | | . \ (_| | (_| | |  | ||  __/ | | |
|_| \_|_____/  |_|\_\__,_|\__,_|_|   \__\___|_| |_|                                                    
                                                   
               _                              _   
    /\        | |                            | |  
   /  \  _   _| |_ ___  _ __ ___   __ _  __ _| |_ 
  / /\ \| | | | __/ _ \| '_ ` _ \ / _` |/ _` | __|
 / ____ \ |_| | || (_) | | | | | | (_| | (_| | |_ 
/_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__,_|\__|

Auteurs: Sven, Gökhan, Gökmen, Lex, Paul

Versie:
------------------------------
GUI.py release 1.0


Wat doet deze applicatie?
------------------------------
Met deze applicatie kunnen reizigers van de van de NS actuele reistijden opvragen.
Tevens kun je zien of en waar er vertragingen zijn.


Software
-----------------
Om dit programma goed te kunnen uitvoeren zijn de volgende applicatie's nodig:

- Python 3.5.0 -> Hoger
- PyCharm Educational Edition 1.0.1 -> hoger


Download links
----------------
https://www.python.org/downloads/
https://www.jetbrains.com/pycharm-edu/download/


Voordat je de kaartautomaat gaat openen moeten de volgende packages worden geïnstalleerd.
--------------------------------------
Om de kaartautomaat correct werkend te krijgen moeten de volgende packages geïnstalleerd worden in pycharm. 
- xmltodict
- requests

Packages installeren doe je als volgt:

- Open het bestand GUI.py 
- Klik op file
- Klik op settings
- Vouw het tabje Project:projectprog uit
- Klik op Project Interpreter
- Klik op de groene +(plus) knop
- Typ xmltodict
- Klik linksonder op Install Package
- Typ requests
- Klik linksonder op Install Package
- Sluit dit venster af, en klik op OK


De kaartautomaat gebruiken
--------------------------
- Open het bestand GUI.py
- Klik op de groene afspeelknop bij coderegel 1 en de applicatie start.
- Er verschijnt een startmenu met twee opties, hier maak je de keuze of je reisinformatie van de huidige station wilt zien of die van een andere station.
- Als de gebruiker kiest voor een andere station, krijgt de gebruiker een optie om een station te selecteren via een dropdownmenu.
- Druk vervolgens op "Haal reisgegevens op"
- Er verschijnt een lijst met gegevens met de treinen die binnen een uur vertrekken vanaf het gekozen station.

