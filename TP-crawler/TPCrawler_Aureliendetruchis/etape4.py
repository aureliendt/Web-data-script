from tasktimer import call_repeatedly
import urllib.request
from bs4 import BeautifulSoup
import re
import time


def getURL (url, Retrieve=True):
    req = urllib.request.Request(url)
    req = urllib.request.urlopen(req).read()

    if Retrieve == True:
        urllib.request.urlretrieve(url, str(url))
    else:
        pass
    return req

# mise en route d'un appel toutes les 5s de la fonction urlcall avec un dictionnaire
# qui contient les paramÃ¨tres passÃ©s Ã  chaque appel de la fonction
n_page = 2



domain = 'http://www.freepatentsonline.com'
urls_visited = []
urls_toVisit = ['/result.html?sort=relevance&srch=top&query_txt=video&submit=&patents=on']

def loading():
    url = urls_toVisit.pop(0)
    urls_visited.append(url)
    req = getURL (domain + url, Retrieve=False)
    soup = BeautifulSoup(req, 'html.parser')
    if a['href'] not in urls_toVisit:
        soupa = soup.find_all('a',href=True)
        for a in soupa:
            if  a['href'] not in urls_toVisit:
                urls_toVisit.append(a['href'])

while urls_toVisit and len(urls_visited)<=10:
    time.sleep(1)
    loading()
