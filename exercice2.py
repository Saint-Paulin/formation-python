#!/usr/bin/python3.6
print("Saisir une année :")
b = 1700
annee = int(input())
if annee%4 == 0:
	if annee%100 != 0 or annee%100 ==0:
		print("C'est une année bissextile")
else:
print("Ce n'est pas une année bissextile")
