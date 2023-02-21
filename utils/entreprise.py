

class Entreprise:

    def __init__(self, name,
                 Mt_tresorerie: int = 0, 
                 Nb_employes: int = 0, 
                 chiffre_daffaire: int = 0, 
                 score_global: int = 0,
                 matiere_premiere : int = 0):

        self.name = name
        self.tresorerie = Mt_tresorerie
        self.employes = Nb_employes
        self.chiffre_daffaire = chiffre_daffaire
        self.score_global = score_global
        self.matiere_premiere = matiere_premiere
    
    


