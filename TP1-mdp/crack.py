# Written with <3 by Julien Romero

import hashlib
from sys import argv
import sys
from itertools import chain, product,permutations
if (sys.version_info > (3, 0)):
    from urllib.request import urlopen
    from urllib.parse import urlencode
else:
    from urllib2 import urlopen
    from urllib import urlencode
import pandas as pd

class Crack:
    """Crack The general method used to crack the passwords"""

    def __init__(self, filename, name):
        """__init__
        Initialize the cracking session
        :param filename: The file with the encrypted passwords
        :param name: Your name
        :return: Nothing
        """
        self.name = name.lower()
        self.passwords = get_passwords(filename)

    def check_password(self, password):
        """check_password
        Checks if the password is correct
        !! This method should not be modified !!
        :param password: A string representing the password
        :return: Whether the password is correct or not
        """
        password = str(password)
        cond = False
        if (sys.version_info > (3, 0)):
            cond = hashlib.md5(bytes(password, "utf-8")).hexdigest() in \
                self.passwords
        else:
            cond = hashlib.md5(bytearray(password)).hexdigest() in \
                self.passwords
        if cond:
            args = {"name": self.name,
                    "password": password}
            args = urlencode(args, "utf-8")
            page = urlopen('https://julienromero.com/ATHENS/' +
                                          'submit?' + args)
            if b'True' in page.read():
                print("You found the password: " + password)
                return True
        return False

    def crack(self):
        """crack
        Cracks the passwords. YOUR CODE GOES HERE.
        """
        pswd = 'Wagner'
        self.check_password(pswd)

        pass

    #Crack pour les digits ou les lettres
    def crack2(self, charset, maxlength):
       """crack
       Cracks the passwords. YOUR CODE GOES HERE.
       """

       L =  list((''.join(candidate)
               for candidate in chain.from_iterable(product(charset, repeat=i)
                                                    for i in range(1, maxlength + 1))))
       for pswd in L:
            self.check_password(pswd)

    # Crack les mots les plus fréquents
    def crack3(self, filenamepwd):
       """crack
       Cracks the passwords. YOUR CODE GOES HERE.
       """

       with open(filenamepwd, "r") as f:
           for line in f:
               pswd = line.strip()
               self.check_password(pswd)

    # Crack pour les tuples de mots séparés par hyphen
    def crack6(self, filenamepwd):
       """crack
       Cracks the passwords. YOUR CODE GOES HERE.
       """
       l = []
       with open(filenamepwd, "r") as f:
           for line in f:
               l.append(line[:-1])

       for group in permutations(l, 2):
           ret = crack.check_password('-'.join(group))

       with open(filenamepwd, "r") as f:
           for line in f:
               pswd = line.strip()
               self.check_password(pswd)

    # Crack pour les remplacements de lettres par caractères
    def crack5(self, filenamepwd):
       """crack
       Cracks the passwords. YOUR CODE GOES HERE.
       """
       dic = {'a':'@','e':'3','o':'0'}
       L=[]
       with open(filenamepwd, "r") as f:
           for line in f:
               pswd = line.strip()
               i=0
               L=[]
               for letter in pswd:
                   if letter in dic:
                        pswd1 = list(pswd)
                        pswd1[i] = dic[letter]
                        pswd1 = "".join(pswd1)
                        pswd2 = pswd
                        self.check_password(pswd1)
                        self.check_password(pswd2)
                        i+=1
    # crack pour les communes françaises
    def crack4(self, filenamecities):
       """crack
       Cracks the passwords. YOUR CODE GOES HERE.
       """
       df = pd.read_csv('villes_france.csv')
       pswdlist = list(df.iloc[:,2].values)

       for pwd in pswdlist:
            pwd = pwd.capitalize()
            self.check_password(pwd)




def get_passwords(filename):
    """get_passwords
    Get the passwords from a file
    :param filename: The name of the file which stores the passwords
    :return: The set of passwords
    """
    passwords = set()
    with open(filename, "r") as f:
        for line in f:
            passwords.add(line.strip())
    return passwords


if __name__ == "__main__":
    # First your password file, then your name
    crack = Crack(argv[1], argv[2])
    crack.crack()
    #crack.crack4('villes_france.csv')
    crack.crack5('google-10000-english.txt')
