import requests
# from lxml import etree
import xml.etree.ElementTree as etree

ICAO_CODE = 'LKTB'
DATA_SOURCE =  'https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString=LKTB,%20PHNL&hoursBeforeNow=2'.format(ICAO_CODE)

def main():
    response = requests.get(DATA_SOURCE)

    tree = etree.fromstring(response.content)
    for element in tree.findall('//data/METAR'):
        time = element.find('./observation_time').text
        temp = element.find('./temp_c').text
        print('{} - {}'.format(time,temp))

if __name__ == '__main__':
    main()




