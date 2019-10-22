#!/usr/bin/python3.6
def compte_mots(ligne):
    ligne_tab = ligne.split(" ")

    return len(ligne_tab)

def compte_lignes_et_mots(contenu):
    lignes = contenu.split('\n')
    compteur_lignes = len(lignes)
    compteur_mots = 0
    for ligne in lignes:
        compteur_mots += compte_mots(ligne)
    return (compteur_lignes, compteur_mots)
with open("exe4.txt", "r") as f:
    contenu = f.read()

print(compte_lignes_et_mots(contenu))