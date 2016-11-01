import requests
import xmltodict

station = 'ut'
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
                reistip = vertrek['ReisTip']
            except:
                reistip = None

            if reistip == None:
                print("{} en {}".format(vertrektijd, eindbestemming))
            else:
                print("{} en {} en {}".format(vertrektijd, eindbestemming, reistip))
reisinformatie(station)

