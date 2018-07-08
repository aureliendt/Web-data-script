from parsy import Parsy
import sys
import nltk
import re
import numpy as np

L = ['An isthmus is a narrow strip of land, with water on either side, that connects two bigger landmasses.']
l = ['type','kind']

def extractType(page):

    content = page
    text = nltk.word_tokenize(content)
    pos_tag = nltk.pos_tag(text)
    array = np.array(pos_tag)
    cond = np.argwhere((array=='is')|(array=='was')|(array=='were')|(array=='are')|(array=='will')|(array=='means'))
    regexNN = re.compile('NN|NNS')
    print(pos_tag)
    if cond.size!=0:
        k = cond[0][0]
        for i in range(k,len(pos_tag)):
            if 'of' in array[k+1:,0]:
                array2 = array[k+1:,0]
                cond2 = np.argwhere(array=='of')
                k2 = cond2[0][0]
                print(k2)
                for i in range(k2+1,len(pos_tag)):
                    if re.match(regexNN,array[i,1]) and array[i-1,0]!='the':
                        classe = array[i,0]
                        print(classe)
                        break
            elif re.match(regexNN,array[i,1]) and array[i,0] not in l:
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
