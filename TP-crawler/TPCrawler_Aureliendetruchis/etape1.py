import urllib.request
url = "http://www.freepatentsonline.com/result.html?sort=relevance&srch=top&query_txt=video&submit=&patents=on"
req = urllib.request.urlretrieve(url,'FPO_etape1.html')
