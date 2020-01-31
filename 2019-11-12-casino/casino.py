""" Don't Work on explorer and wont find out why I don't care pretty much. Still usable in python directly or as a .py file. BTW it's in French"""

# -*-coding:utf-8 -*

import os
from math import ceil
from random import randrange

#Les starters :
wallet = 2000 #  Mon argent 
continue_la_partie = True


print("Bienvenue au casino.")
print("Vous commencer à jouer avec une somme de :", wallet, "euros.")

while continue_la_partie : #Bolean True = continué la game
  #le bet_case
  bet_case = -1
  while bet_case < 0 or bet_case > 49 :
    bet_case = input("Sur quelle case souhaitez-vous misé ?")
    try:
      bet_case = int(bet_case)
    except ValueError:
      print("Vous devez choisir un nombre")
      bet_case = -1
      continue
    if bet_case < 0:
      print("Séléctionner un chiffre ou un nombre compris entre 0 et 49")
    if bet_case > 49:
      print("Séléctionner un chiffre ou un nombre compris entre 0 et bet")
  
  #Le bet
  bet = 0
  while bet <= 0 or bet > wallet:
    bet = input("Tapez le montant de votre mise : ")
        # On convertit la mise
    try:
      bet = int(bet)
    except ValueError:
      print("Vous n'avez pas saisi de nombre")
      bet = -1
      continue
    if bet <= 0:
      print("La mise saisie est négative ou nulle.")
    if bet > wallet:
      print("Vous ne pouvez miser autant, vous n'avez que", wallet, "$")
  #Le bille est jetée
  nb = int(randrange(49))
  print("La bille est tombé sur le numéro :", nb,".")
  #Le résultat 
  if nb == bet_case :
    print("Vous venez de remporté :", bet*3,"soit triple de votre mise")
    wallet += bet*3
    print("Vous totalisé la somme de:", wallet,".Félicitation !")
  elif nb % 2 == bet_case % 2 :
    bet = ceil(bet * 0.5) # 
    wallet += bet
    print("Vous récupérez la moitié de votre mise.", wallet,)
  elif nb != bet_case :
    print("Vous venez de perdre votre mise de :", bet,"euros. Désolé bro.^^")
    print("Il vous reste :",wallet,"euros.")
  #Fin de partie
  if wallet <= 0:
    print("T'as plus de thunes bolosse.")
    continue_la_partie = False
  else :
    quitter = input("Souhaitez-vous relancer une partie (y/n) ? ") #J'avoue j'ai triché pour cette partie.
    if quitter == "N" or quitter == "n":
      print("Cya nerds")
      continue_la_partie = False

# On met en pause le système (Windows)
os.system("pause")
    