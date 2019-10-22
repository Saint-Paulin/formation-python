#!/usr/bin/python3.6
#def dictionnaire(valeur)
#	print("Bonjour !" + valeur)
#	ou return (valeur)
def compter_voyelles(phrase):
	voyelles = {"a":0,"e":0,"i":0,"o":0,"u":0,"y":0}
	for lettre in phrase:
		if lettre in voyelles.keys():
			voyelles[lettre] = voyelles[lettre]+1
	return voyelles
ma_phrase = input()
print(compter_voyelles(ma_phrase))

def compte_points(points):
	cara = {";":0,",":0,".":0}
	for var1 in points:
		if var1 in cara.keys():
			cara[var1] +=1
	return cara
print(compte_points(ma_phrase))
