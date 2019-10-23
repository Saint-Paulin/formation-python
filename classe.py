#!/usr/bin/python3.6

class Plantes:
    def __init__(self, racine, couleur):
        self.racine = racine
        self.couleur = couleur

    def couper(self):
        self.racine = None

    def ajout_couleur(self, couleur):
        self.couleur = couleur

class Arbre(Plantes):
    def __init__(self, racine, couleur_feuillage):
        self.racine = racine
        self.couleur = couleur_feuillage
        Plantes.__init__(self, racine, couleur_feuillage)

    def get_racine(self):
        return self.racine

class Fleur:
    def __init__(self, racine, petales, couleur):
        self.racine = racine
        self.petales = petales
        self.couleur = couleur

    def couper(self):
        self.racine = None

    def retier_petales(self, nb_petales):
        self.petales -= nb_petales

    def ajouter_petales(self, nb_petales):
        self.petales += nb_petales

    def ajout_couleur(self, color):
        self.couleur = color

fleur = Fleur("toto", 24, "bleue")
fleur2 = Fleur("tata", 50, "rouge")

print(fleur.racine)
fleur.couper()
print(fleur.racine)
print(fleur.petales)
fleur.retier_petales(10)
print(fleur.petales)

fleur.ajout_couleur("verte")
print(fleur.couleur)

print(fleur2.petales)
fleur2.retier_petales(10)
print(fleur2.petales)

arbre = Arbre("pommier", "Vert")
print(arbre.get_racine)
arbre.couper()
print(arbre.racine)