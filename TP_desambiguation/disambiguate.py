'''Given as command line arguments
  (1) yagoLinks.tsv
  (2) yagoLabels.tsv
  (3) wikipedia-ambiguous.txt
  (4) the output filename
  writes lines of the form
        title TAB entity
  where <title> is the title of the ambiguous
  Wikipedia article, and <entity> is the YAGO
  entity that this article belongs to.
  It is OK to skip articles (do not output
  anything in that case).
  (Public skeleton code)'''
import collections
import sys
import numpy as np
import re
from parser import Parser
from simpleKB import SimpleKB
import nltk
from nltk import word_tokenize

yago = SimpleKB(sys.argv[1], sys.argv[2])
# yago is here an object containing 3 dictionaries:
## yago.links is a dictionary of type: entity -> set(entity).
##            It represents all the entities connected to a
##            given entity in the yago graph
## yago.labels is a dictionary of type: entity -> set(label).
##            It represents all the labels an entity can have.
## yago.rlabels is a dictionary of type: label -> set(entity).
##            It represents all the entities sharing a same label.

# Note that the class Page has a method Page.label(),
# which retrieves the human-readable label of an ambiguous
# Wikipedia page.

with open(sys.argv[4], 'w', encoding="utf-8") as output:
    for page in Parser(sys.argv[3]):
        score = dict()
        label = page.label()
        content = page.content
        print(page.title)
        print(content)

        rlabs = list(yago.rlabels[label])

        for rlab in rlabs:
            a = rlab[1:-1]
            b = a.replace('_',' ').replace('(',' ').replace(')',' ').replace('  ',' ')
            labelsin= b.split(' ')
            score[rlab]=0
            for labelin in labelsin:
                if labelin in content:
                    score[rlab]+=1
                else:
                    score[rlab]-=1

            linked = list(yago.links[rlab])
            list_link = []
            for linke in linked:
                a = linke[1:-1]
                b = a.replace('_',' ').replace('(',' ').replace(')',' ').replace('  ',' ')
                linkesin= b.split(' ')
                list_link.extend(linkesin)
            set_link = list(set(list_link))
            #pos = nltk.pos_tag(set_link)
            #set_link2 = []
            #for po in pos:
            #    if po[1][:2] == 'NN':
            #        set_link2.append(po[0])
            #print(set_link2)
            for setin in set_link:
                if setin in content:
                    score[rlab]+=1

        first = sorted(score, key=score.__getitem__)[-1]
        print(first)
        pass
