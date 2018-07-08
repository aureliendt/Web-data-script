README

etape1.py:

Programme faisant la requête sur : url = "http://www.freepatentsonline.com/result.html?sort=relevance&srch=top&query_txt=video&submit=&patents=on"

etape2.py:

Fonction getURL -> permet de faire une requête à un url donné en argument
Fonction loading -> permet de charger une liste d'url présent sur une page


etape3.py:

Le programme va boucler sur loading() pour construire deux listes urls.
On a deux listes urls_visited et urls_toVisit.
On s'arrête quand la liste d'urls est de taille N .


etape4.py:

On ajoute une condition sur les urls : if url not in urls_toVisit.
Cela nous permet d'éviter les doublons.

etape5.py:

On ajoute une condition sur la présence de la string 'Application Number' dans la page chargée : if 'Application Number' in soup.text and a['href'] not in urls_toVisit
Cela nous permet de charger uniquement les brevets

etape6.py:

Nous avons les regex:

'[1-9]{7}.html'
et
'[A-Z]{2}[0-9]*[A-Z][0-9].html'

Nous permettant de sélectionner les urls correspondants à des brevets uniquement


etape7.py:

La fonction getInfo(soup) permet de construire un dictionnaire avec les clefs
('title','number','author','year','month','country') à partir d'un brevet .html
Nous ajoutons cette fonction dans la fonction loading, pour qu'elle fasse ce travail sur chaque urls visités.


etape8.py:

Nous ajoutons une condition dans loading() sur la valeur de la clef 'author' du dictionnaire construit
par getInfo pour que cette valeur (string) contienne la string 'FR'.
Nous arrêtons notre boucle while pour chercher les trois premiers brevets FR.
Nous chargeons le résultat (url et dictionnaire) dans 3FR.json.
