from operator import truediv
from bs4 import BeautifulSoup
import requests

hospitals = [
    ["A.O. Fox Memorial Hospital", "1 Norton Ave, Oneonta, NY 13820", "https://www.bassett.org/locations/ao-fox-hospital/ao-fox-patients-visitors/ao-fox-hospital-pricing"]
]

def interpretNLE():
    pass

def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
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
            print(url[0] + " not downloadable")

def collect_insurers():
    pass

def find_price(CPTCode, hospital):
    pass

collect_hospitals()