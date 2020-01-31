"""
Gestion de fiche de contact avec
prenom, nom, naissance, couriel
"""

import pickle 
import sys
sys.exit(0)

### Section class
class CarnetAdr(object):
    """ Conteneur de fiches """
    
   
            
class FichAdr(object):
    """ Fiche d'un contact """
    #Ajout méthode
    def __init__(self, prenom=None, nomfami=None,
                datenaiss=None, courriel=None):
        """ Initialise les 4 attributs.
        le format de datenaiss est JJ/MM/AAAA"""
        
        self.prenom = prenom
        self.nomfami = nomfami
        self.datenaiss = datenaiss
        self.courriel = courriel
        
    def __repr__(self):
        """ Produit une chaine selon l'objet FichAdr
        fourni en argument self."""
        
        patron = "FichAdr(prenom = '%s', "+\
            "nomfai = '%s', "+\
            "datenaiss = '%s' "+\
            "courriel = '%s')"
        return patron%(self.prenom, self.nomfami,
                       self.datenaiss, self.courriel)

    def add(self) :  
        global my_list
        my_list = []
        my_list.append(self)

def addinfo() :
    
    a = input("nom:")
    b = input("prénom:")
    c = input("date de naissance:")
    d = input("mail:")
    
    contact = FichAdr(a,b,c,d).add()
    return contact

### Section fonction
### Section principal main

def main(): 
    userchoice = input("hihi (y/Y)")
    if userchoice == "y" or "Y" :
        main()
        addinfo()
    else :
        main()
        
main()