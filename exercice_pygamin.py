#!/usr/bin/python3

class Pyjama:
    def __init__(self, color="jaune", texture="coton", taille="L"):
        self.color = color
        self.texture = texture
        self.taille = taille
        self.achete = False
        self.prix = 0

    # Méthode acheter
    def acheter(self):
        if self.achete:
            print("Ce pyjama est déjà acheté.")
            return

        if self.color == "jaune":
            self.prix = 10
        elif self.color == "bleu":
            self.prix = 50
        elif self.color == "bordeau":
            self.prix = 20
        else:
            print("Couleur inconnue.")
            return

        self.achete = True
        print(f"Pyjama {self.color} en {self.texture} acheté pour {self.prix} euros.")

    # Méthode laver
    def laver(self, autre_pyjama):
        if not self.achete or not autre_pyjama.achete:
            print("Impossible : pyjama non acheté.")
            return

        if self.texture == autre_pyjama.texture:
            print(f"On lave {self.texture} avec {autre_pyjama.texture}")
        else:
            print("On ne mélange pas les textures")

    # Méthode vendre
    def vendre(self):
        if not self.achete:
            print("Vous n'avez pas acheté ce pyjama.")
            return

        prix_vente = self.prix / 2
        self.achete = False
        print(f"Pyjama vendu pour {prix_vente} euros.")
