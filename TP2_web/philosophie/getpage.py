#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Ne pas se soucier de ces imports
import setpath
from bs4 import BeautifulSoup
from json import loads
from urllib.request import urlopen
from urllib.parse import urlencode
import json
import pprint
from functools import lru_cache
import encodings

pp = pprint.PrettyPrinter(indent=4)

# Si vous écrivez des fonctions en plus, faites-le ici


def getJSON(page):
    params = urlencode({
      'format': 'json',  # TODO: compléter ceci
      'action': 'parse',  # TODO: compléter ceci
      'prop': 'text',
      'redirects': 'true', # TODO: compléter ceci
      'page': page})
    API = "https://fr.wikipedia.org/w/api.php"  # TODO: changer ceci
    response = urlopen(API + "?" + params)
    return response.read().decode('utf-8')


def getRawPage(page):
    parsed = loads(getJSON(page))
    try:
        title = parsed['parse']['title'] # TODO: remplacer ceci
        content = parsed['parse']['text'] # TODO: remplacer ceci
        return title, content
    except KeyError:
        # La page demandée n'existe pas
        return None, None


def getPage(page):
    try:
        title,content=getRawPage(page)
        soup = BeautifulSoup(content['*'], 'html.parser')
        a = soup.div.find_all('p',recursive = False)
        liste1 = [aa.find_all('a') for aa in a]
        liste2 = [val for sublist in liste1 for val in sublist]

        liste3 = [L.get('href') for L in liste2]
        liste4=[]
        for l in liste3:
                  if l.startswith('/wiki') :
                      word = l[6:]
                      word = word.replace('%C3%A9','é').replace('%C3%A8','è').replace('_',' ')\
                                    .replace('%C3%A9','é').replace('%C3%A8','è').replace('%C3%AB','ë')\
                                    .replace('%C3%A0','à').replace('%C3%89','E').replace('%27','\'')

                      liste4.append(word)

                  else:
                      pass
        liste5 = []
        for elem in liste4:
            if elem not in liste5:
                liste5.append(elem)
        return liste5[:10],title
    except TypeError:
        return None, []



if __name__ == '__main__':
    # Ce code est exécuté lorsque l'on exécute le fichier
    print("Ça fonctionne !")
    js = getJSON('aristote')

    # Voici des idées pour tester vos fonctions :
    # print(getJSON("Utilisateur:A3nm/INF344"))
    # print(getRawPage("Utilisateur:A3nm/INF344"))
    # print(getRawPage("Histoire"))
