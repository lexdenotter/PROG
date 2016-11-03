import requests
import xmltodict
#lijst waar stationsnamen in komen te staan
keuzes = []
#functie om stationsnamen op te halen uit de api en in een xml bestand te schrijven
def stationNamen():
    username = 'gokmen.simsek@student.hu.nl'
    password = 'TQxDmfd3Ghmj9HiN5MFtnfAapCWj7bcx-0Yx3SJbtgS8r0bDGcpWcw'
    auth_details = (username, password)
    api_url = 'http://webservices.ns.nl/ns-api-stations-v2'
    response = requests.get(api_url, auth=auth_details)

    with open('stationsnamen.xml', 'w', encoding="utf8") as stationNaam:
        stationNaam.write(response.text)
        namen = xmltodict.parse(response.text)
        namen = namen['Stations']
        elementen = namen['Station']
        for element in elementen:
            if element['Land'] == 'NL':
                keuzes.append(element['Namen']['Lang'])
        for element in keuzes:
            if 'NS-bus' in element:
                keuzes.remove(element)
stationNamen()
