import requests
import xmltodict


def reisinformatie(station):
    # api aanroepen
    username = 'gokmen.simsek@student.hu.nl'
    password = 'TQxDmfd3Ghmj9HiN5MFtnfAapCWj7bcx-0Yx3SJbtgS8r0bDGcpWcw'
    auth_details = (username, password)
    api_url = 'http://webservices.ns.nl/ns-api-avt?station={}'.format(station)
    response = requests.get(api_url, auth=auth_details)
    # gegevens api wegschrijven in xml file
    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)
        vertrekXML = xmltodict.parse(response.text)
        vertrekXML = vertrekXML['ActueleVertrekTijden']
        elementen = vertrekXML['VertrekkendeTrein']
        total = [("{:5} {:21} {:11} {:17} {:12}".format('Tijd', 'Bestemming', 'Vertraging', 'Soort',
                                                        'Spoor'))]  # list waar reisinformatie in wordt opgeslagen
        # xml file doorlopen en gegevens daaruit in variabelen opslaan
        for vertrek in elementen:
            vertrektijd = vertrek['VertrekTijd']
            vertrektijd = vertrektijd[11:16]
            eindbestemming = vertrek['EindBestemming']
            try:
                vertraging = vertrek['VertrekVertragingTekst']
            except:
                vertraging = '0 min'
            treinsoort = vertrek['TreinSoort']
            try:
                spoor = vertrek['VertrekSpoor']
                spoornummer = spoor['#text']
            except:
                spoornummer = 'N/A'

            total.append("{:5} {:25} {:7} {:17} {:8}".format(vertrektijd, eindbestemming, vertraging, treinsoort,
                                                             spoornummer))  # toevoegen van reisinformatie aan de lijst
    return total
