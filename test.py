#!/usr/bin/python3.6
import random
noms = ["Jeremy", "Paulin", "Theo"]
anim = ["l'ours", "la belette", "le blaireau"]
print(noms[random.randint(0, len(noms)-1)] + " " + anim[random.randint(0, len(anim)-1)])
if noms == noms[2]: if anim == anim[2]: print("Aie !")
