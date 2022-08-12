from bs4 import BeautifulSoup
import requests
import validators
import pandas as pd
from finalhospitals import hospitals

def remove_newline(list):
    new_list = [x[:-1] for x in list]
    new_list[-1] = list[-1]
    return new_list

IPs = []

def interpretNLE(nl):
    pass

def is_downloadable(url):
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


def collect_hospitals():
    def if_button(string):
        keywords = ['standard', 'charges', 'download', 'charge']
        numin = 0
        for stri in keywords:
            if stri in string.lower():
                numin +=1
        if numin >= 2:
            return True
        else:
            return False
    for url in hospitals:
        if validators.url(url[2]):
            location = url[2]
            firstvar = location.split('/')

            domain = "https://" + firstvar[2]

            result = requests.get(location)
            soup = BeautifulSoup(result.text, "html.parser")

            occurences = []

            for link in soup.find_all('a'):
                occurences.append(str(link.get('href')))

            for string in occurences:
                if if_button(string.lower()):
                    exacturl = domain + string

            if is_downloadable(exacturl):
                r = requests.get(exacturl, allow_redirects=True)
                open(str(url[0]) + '.xlsx', 'wb').write(r.content)
            else:
                return url[0] + " not downloadable"
        else:
            continue

def collect_insurers():
    pass


def find_price(CPTcode, hospital):
    df = pd.read_excel(hospital + '.xlsx')  
    print(df.head())