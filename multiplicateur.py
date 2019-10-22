#!/usr/bin/python3.6
'''
1 ) Saisir la chaine
2 ) Si c'est un int alors multiplier par 3
3 ) Sinon print "Nope"
'''

try:
    numero = float(input("Entrez un nombre : "))
    print("resultat : ", numero*3)
except:
    print("Nope, c'est pas un nombre boloss")