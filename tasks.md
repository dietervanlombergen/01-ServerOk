# Oefening “Server OK?”
Je maakt in Python een network monitoring tool waarmee je aan de hand van een
ping kunt nagaan of een server online is. Om de zoveel tijd wordt voor elke
geregistreerde server een ping uitgevoerd en wordt de status naar een log
weggeschreven.
Je hoeft op dit moment enkel de ping als check aan te bieden (op basis van IP-adres
of hostname), maar je bouwt nu al in je toepassing in dat in een latere fase zou
kunnen uitgebreid worden met andere checks
Voor de concrete-implementatie ben je vrij. Probeer te voldoen aan de specificaties
die hier zijn opgelijst. Meer mag ;-)

- Je zorgt voor een interactieve interface via de terminal. De gebruiker kan de
toepassing bedienen via de terminal (input-functie).  => done

- Je zorgt ervoor dat servers
kunnen toegevoegd, verwijderd, of in een lijst getoond worden. => done

- Je zorgt ervoor dat je systeem ook op dezelfde manier bedienbaar via de
command-line interface. Je gebruikt hiervoor sys.argv.

- Je houdt de ingevoerde data, alsook de uitgevoerde checks bij in één of
meerdere json-bestand(en). => done

- Je zorgt er met command-line argumenten voor dat je tool in 2 modi kan
uitgevoerd worden, in management modus (om servers toe te voegen en
eventueel de settings van het programma aan te passen) en in check modus
(waarbij de checks gebeuren)

- In de praktijk zouden de checks (met je tool in check modus) via een Cronjob
bvb om de 2min kunnen herhaald worden.

- Je zorgt ervoor dat je script telkens de checks gebeurd zijn een html-pagina
genereert waarin over de toestand van de servers gerapporteerd wordt. Je
maakt hiervoor ook gebruik van een template bestand zodat je in je script zo
weinig mogelijk html moet genereren en vertrekt voor de data van de
weggeschreven data in het json-bestand.

- Probeer je code zo georganiseerd mogelijk te houden, in meerdere modules als
het moet. Met gebruik van functies.

## Tip: pingen in Python? https://www.delftstack.com/howto/python/python-ping/
## Optioneel: voeg de mogelijkheid tot meerdere checks toe aan je toepassing. Bvb: het checken van een web pagina (hiervoor kan je gebruik maken van de requests library). Je mag hier zo ver gaan als je zelf wil.

## Usage

- Command line arguments

1. python main.py mode - management or check
1. python main.py mode command - See command options ( add, delete, show, clear, stop)
1. python main.py mode command parameters - See options for parameters




- User input with terminal