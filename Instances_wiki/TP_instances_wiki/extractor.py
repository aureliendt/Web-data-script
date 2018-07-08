'''Extracts type facts from a wikipedia file
usage: extractor.py wikipedia.txt output.txt

Every line of output.txt contains a fact of the form
    <title> TAB <type>
where <title> is the title of the Wikipedia page, and
<type> is a simple noun (excluding abstract types like
sort, kind, part, form, type, number, ...).

If you do not know the type of an entity, skip the article.
(Public skeleton code)'''

from parsy import Parsy
import sys
import nltk
import re
import numpy as np
precision = 0
count_good = 0
count_bad = 0

if len(sys.argv) != 3:
    print(__doc__)
    sys.exit(-1)

l = ['type','kind','word','style']

def extractType(page):
    global count_good
    global count_bad
    content = page.content
    text = nltk.word_tokenize(content)
    pos_tag = nltk.pos_tag(text)
    array = np.array(pos_tag)
    cond = np.argwhere((array=='is')|(array=='was')|(array=='were')|(array=='are')|(array=='will')|(array=='means'))
    regexNN = re.compile('NN|NNS')
    #print(array)
    if cond.size!=0:
        k = cond[0][0]
        #print (k,len(pos_tag))
        for i in range(k,len(pos_tag)):
            if re.match(regexNN,array[i,1]) and array[i,0] not in l:
                classe = array[i,0]
                a=i
                if re.match(regexNN,array[a+1,1]):
                    classe = array[a+1,0]
                    a=a+1
                    if re.match(regexNN,array[a+1,1]):
                        classe = array[a+1,0]
                break
            else:
                classe = None
    else:
        classe = None

    return classe



SolDict = {}
with open("./gold-standard-sample.tsv") as f:
    for line in f:
        token = line.split("\t")
        SolDict[token[0]] = token[1].replace("\n", "")


with open(sys.argv[2], 'w', encoding="utf-8") as output:
    for page in Parsy(sys.argv[1]):
        #print(page.title)
        if page.title in SolDict:
            #print("--------------------------")
            #print(page.title)
            #print("Solution :" + SolDict[page.title])
            typ = extractType(page)
            #print(typ)

            if typ:
                output.write(page.title + "\t" + typ + "\n")
                if typ == SolDict[page.title]:
                    count_good += 1
                    #print("Yes")
                else:
                    count_bad += 1
                    #print("No")
            #print("--------------------------")
precision = (count_good / (count_good + count_bad)) * 100
#print('good :',count_good)
#print('bad :',count_bad)
#print(precision)
