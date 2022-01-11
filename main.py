from Salade_composee import Salade_composee
from Tomate import Tomate
from Laitue import Laitue

tomate = Tomate(12, "rouge")
laitue = Laitue(13)
salade_composee = Salade_composee(tomate, laitue)

salade_composee.afficher_couleur_tomate()
