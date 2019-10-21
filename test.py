#!/usr/bin/python3.6
import random
noms = ["Jeremy", "Paulin", "Theo"]
anim = ["l'ours", "la belette", "le blaireau"]
#print(noms[random.randint(0, len(noms)-1)] + " " + anim[random.randint(0, len(anim)-1)])
ins = noms[2] + " " + anim[2]
if ins == noms[2]:
	if ins == anim[2]:
		print("Aie ! On a insulté le prof ...")
else:
	print(noms[random.randint(0, len(noms)-1)] + " " + anim[random.randint(0, len(anim)-1)])
