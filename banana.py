class Singe:
    def __init__(self, prenom):
        self.prenom = prenom
        print(' creation singe ' + self.prenom)

    def mange(self, banane):
        phrase = str(self.prenom) + ' mange une banane ' + str(banane.couleur)
        print(phrase)

    def reproduire(self, singe, nomEnfant):
        print(str(self.prenom) + ' se reproduit avec ' + str(singe.prenom) + ' pour faire ' + nomEnfant)
        enfant = Singe(nomEnfant)
        return enfant




class Banane:
    def __init__(self, couleur):
        self.couleur = couleur
        print(' creation banane ' + self.couleur)

pierre = Singe('Pierre')
marie = Singe('Marie')

bananeJaune = Banane('jaune')
bananeVerte = Banane('verte')

pierre.mange(bananeJaune)
marie.mange(bananeVerte)

pierre.reproduire(marie, 'Eliott')





