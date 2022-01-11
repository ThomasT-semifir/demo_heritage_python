from Engin_motorise import Engin_motorise


class Voiture(Engin_motorise):
    """
    La classe Voiture hérite de Engin_motorise et donc de tous ses attributs et méthodes.
    Par conséquent, dès sa création et sans aucune mention nous pouvons utiliser get_marque et set_marque
    En plus des attributs et méthodes de la classe Engin_motorise, la classe Voiture possède ses attributs propres et ses méthodes propres
    Nous lui rajoutons ici set_nbr_porte et get_nbr_porte
    """

    def __init__(self, marque, nbr_porte):
        # self._marque = marque
        super().__init__(marque)
        self._nbr_porte = nbr_porte

    def set_nbr_porte(self, value):
        self._nbr_porte = value

    def get_nbr_porte(self):
        return self._nbr_porte

    # redéfinition de méthode
    # def presenter(self):
    #     """
    #     Il s'agit ici de redéfinition, on réutilise la méthode de la classe parent mais
    #     le comportement est intégralement modifié. On écrase la méthode du parent.
    #     :return: La phrase de présentation
    #     """
    #     return f"Ma voiture a {self.get_nbr_porte()} portes"

    # surcharge de méthode
    def presenter(self):
        return f"{super().presenter()} et le nombre de portes est {self.get_nbr_porte()} parce que moi je suis une voiture pas simplement un engin motorisé!!!"

    # def __str__(self):
    #     return f"Ma voiture est une {self.get_marque()} et a {self.get_nbr_porte()} portes"
