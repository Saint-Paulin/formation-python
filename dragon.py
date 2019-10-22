#!/usr/bin/python3.6

import random, math

class Population():
    def __init__(self):
        self.humains = []
        self.dragons = []
        self.moutons = []

    def repro_humain(humains):
        nb_bebe = int(len(self.humains)/2)
        for i in range(nb_bebe):
            self.humains.append(Humain(nom=Humains.genere_nom()))

    def repro_mouton(moutons):
        nb_agneau = int(len(self.moutons)/2)*2
        for i in range(nb_agneau):
            self.moutons.append(Moutons(nom=Moutons.genere_nom()))

    

    def snap_violent(self):
        self.humains = []
        self.moutons = []
        self.humains = []

    def passer_une_annee(self):
        '''
        :return: True si ce n'est pas fini, False si une liste est vide
        '''
        self.repro_humains()
        self.repro_moutons()
        list_animaux = self.humains + self.dragons + self.moutons

        for dragons in self.dragons:
            sacrifice = random.choice(self.humains+self.moutons)
            if dragon.peut_manger(sacrifice):
                del sacrifice
        # Les humains festoient
        if len(self.humains)>0:
            nb_banquet = math.ceil(len(humains)/4)
            for _ in range(0,nb_banquet):
                mouton_cuit = random.choice(self.moutons)
                del mouton_cuit
                

        for animal in list_animaux:
            if not animal.viellir():
                del animal
        if not self.humains:
            print("Oh ils sont tous morts les humains")
            return False
        if not self.moutons:
            print("On a tout mangé !")
            return False
        elif not self.dragons:
            print("DOVAHKIN !")
            return False
        return True

    def jouer(self, nb_dragons, nb_humains, nb_moutons):
        cpt_annees = 0
        for i in range(0, nb_dragons):
            self.dragons.append(Dragons(nom=Dragons.genere_nom()))
        for i in range(0, nb_humains):
            self.humains.append(Humains(nom=Humains.genere_nom()))
        for i in range(0, nb_moutons):
            self.moutons.append(Moutons(nom=Moutons.genere_nom()))

        while self.passer_une_annee():
            print("Et une année de plus ! Depuis {} ans.".format(cpt_annees))

class Animaux:
    '''
    Classe Générique des animaux
    '''
    def __init__(self, nom):
        self.nom = nom
        self.age = 0
        self.age_max = 100 # magic number

    def viellir(self):
        '''
        return true si animal en vie, False sinon
        :rtype: bool
        '''
        if self.age > self.age_max:
            return False
        self.age += 1
        return True

    def peut_manger(self, animal):
        if not isinstance(animal, Animal):
            print("Ca se mange pas ça")

    @staticmethod
    def genere_nom():
        raise NotImpementedError
    


class Dragons(Animaux):
    def __init__(self, nom):
        Animaux.__init__(self, nom)
        self.age_max = 250

    @staticmethod
    def genere_nom():
        return random.choice(["Alduin", "Paarthurnax", "Michel"])


class Moutons(Animaux):
    def __init__(self, nom):
        Animaux.__init__(self, nom)
        self.age_max = 10

    def peut_manger(self, animal):
        if not isinstance(animal):
            print("Je bouffe de l'herbe")
            return False
        return True
    
    @staticmethod
    def genere_nom():
        return random.choice(["Beh", "Bah", "Boh"])

class Humains(Animaux):
    def __init__(self, nom):
        Animaux.__init__(self, nom)
        self.age_max = 50

    def peut_manger(self, animal):
        if not isinstance(animal, Moutons):
            print("Je mange que du mouton")
            return False
        return True

    @staticmethod
    def genere_nom():
        return random.choice(["Robert", "Jeanne", "Pierre", "Biloute", "Dominique", "Camille", "Alix"])