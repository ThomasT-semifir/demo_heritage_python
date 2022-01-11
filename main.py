from Engin_motorise import Engin_motorise
from Moto import Moto
from Voiture import Voiture

engin_motorise = Engin_motorise("Beko")
print(engin_motorise.presenter())

voiture = Voiture("Renault", 5)
print(voiture.presenter())

moto = Moto("Honda", "essence")
print(moto.presenter())
