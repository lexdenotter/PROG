import requests
import xmltodict


def reisinformatie(station):
    #api aanroepen
    username = 'gokmen.simsek@student.hu.nl'
    password = 'TQxDmfd3Ghmj9HiN5MFtnfAapCWj7bcx-0Yx3SJbtgS8r0bDGcpWcw'
    auth_details = (username, password)
    api_url = 'http://webservices.ns.nl/ns-api-avt?station={}'.format(station)
    response = requests.get(api_url, auth=auth_details)

    #api wegschrijven in XML file
    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)
        vertrekXML = xmltodict.parse(response.text)
        vertrekXML = vertrekXML['ActueleVertrekTijden']
        elementen = vertrekXML['VertrekkendeTrein']

        #XML file doorlopen en gegevens opslaan in variabelen
        for vertrek in elementen:
            vertrektijd = vertrek['VertrekTijd']
            vertrektijd = vertrektijd[11:16] #range zorgt voor goede weergave tijd
            eindbestemming = vertrek['EindBestemming']
            #vertraging is niet altijd bij elke treinrit, daarom in try en except dit geldt ook voor spoor, opmerking en reistip
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

            #print maken van de gegevens uit de XML in mooie format
            print('de trein van {}, vertrekt naar {}. \n'
                    'Deze trein heeft {} vertraging. \n'
                    'Deze trein is een {} van {}. \n'
                    'Deze trein vertrekt van spoor {}. \n'
                    '{}{}'.format(vertrektijd, eindbestemming, vertraging, treinsoort, vervoerder, spoornummer, reistip, opmerking))

