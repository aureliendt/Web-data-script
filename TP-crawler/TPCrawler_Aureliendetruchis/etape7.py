from tasktimer import call_repeatedly
import urllib.request
from bs4 import BeautifulSoup
import re
import time
import json


def getURL (url, Retrieve=True):
    req = urllib.request.Request(url)
    req = urllib.request.urlopen(req).read()
    if Retrieve == True:
        urllib.request.urlretrieve(url, str(url))
    else:
        pass
    return req

def getInfo(soup):
    brevet = {}
    for elm in soup.find_all('form', {'name':'biblio'}):
        #brevet[url_0] = {}
        for itm in (elm.find_all('input')):
            if itm.get('name') =='title':
                brevet['title'] = itm.get('value')
            elif itm.get('name') =='number':
                brevet['number'] = itm.get('value')
            elif itm.get('name') =='author':
                brevet['author'] = itm.get('value')
            elif itm.get('name') =='year':
                brevet['year'] = itm.get('value')
            elif itm.get('name') =='month':
                brevet['month'] = itm.get('value')
            elif itm.get('name') =='country':
                brevet['country'] = itm.get('value')
    return(brevet)

# mise en route d'un appel toutes les 5s de la fonction urlcall avec un dictionnaire
# qui contient les paramÃ¨tres passÃ©s Ã  chaque appel de la fonction
def loading():
    url = urls_toVisit.pop(0)
    urls_visited.append(url)
    req = getURL (domain + url, Retrieve=False)
    soup = BeautifulSoup(req, 'html.parser')
    json_info[url] = getInfo(soup)
    soupa = soup.find_all('a',href=True)
    for a in soupa:
        if  re.match('[1-9]{7}.html',a['href'].split("/")[-1])\
                        or re.match("[A-Z]{2}[0-9]*[A-Z][0-9].html", a['href'].split("/")[-1])\
                        and a['href'] not in urls_toVisit:
            urls_toVisit.append(a['href'])


domain = 'http://www.freepatentsonline.com'
urls_visited = []
urls_toVisit = ['/result.html?sort=relevance&srch=top&query_txt=video&submit=&patents=on']
json_info={}


while urls_toVisit and len(urls_visited)<=5:
    #time.sleep(1)
    loading()
json_info = json.dumps(json_info)
