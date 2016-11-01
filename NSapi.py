import requests
import xmltodict

station = 'ah'
def reisinformatie(station):
    #api aanroepen
    username = 'gokmen.simsek@student.hu.nl'
    password = 'TQxDmfd3Ghmj9HiN5MFtnfAapCWj7bcx-0Yx3SJbtgS8r0bDGcpWcw'
    auth_details = (username, password)
    api_url = 'http://webservices.ns.nl/ns-api-avt?station={}'.format(station)
    response = requests.get(api_url, auth=auth_details)

    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)
        vertrekXML = xmltodict.parse(response.text)
        vertrekXML = vertrekXML['ActueleVertrekTijden']
        elementen = vertrekXML['VertrekkendeTrein']
        for vertrek in elementen:
            vertrektijd = vertrek['VertrekTijd']
            vertrektijd = vertrektijd[11:16]
            eindbestemming = vertrek['EindBestemming']
            try:
                vertraging = vertrek['VertrekVertragingTekst']
            except:
                vertraging = '0 min'
            treinsoort = vertrek['TreinSoort']
            vervoerder = vertrek['Vervoerder']
            try:
                spoor = vertrek['VertrekSpoor']
                spoornummer = spoor['#text']
            except:
                spoornummer = '0'
            try:
                reistip = 'Opmerking: ' + vertrek['ReisTip'] + '. \n'
            except:
                reistip = ''
            try:
                opmerking = 'Opmerking: ' + vertrek['Opmerkingen']['Opmerking'] + '. \n'
            except:
                opmerking = ''
            print('de trein van {}, vertrekt naar {}. \n'
                    'Deze trein heeft {} vertraging. \n'
                    'Deze trein is een {} van {}. \n'
                    'Deze trein vertrekt van spoor {}. \n'
                    '{}{}'.format(vertrektijd, eindbestemming, vertraging, treinsoort, vervoerder, spoornummer, reistip, opmerking))

reisinformatie(station)

