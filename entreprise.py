
SALAIRE = 1150

class Entreprise:

    def __init__(self, name: str, tresorerie: int = 10000, employes = 0, ressources: list[int] = [0, 0], prix_produit: int = 100):
        """
        name : nom de l'entreprise
        tresorerie : ressources financières de l'entreprise
        employes : nombre d'employés de l'entreprise
        ressources[0] : matériel
        ressources[1] : matières premières
        """
        self.name = name
        self.tresorerie = tresorerie
        self.employes = employes
        self.ressources = ressources
        self.prix_produit = prix_produit
    
    #fonctions utiles pour manipuler la tresorerie

    def calcul_benefice(self, production_modifier: float):
        salaires = self.employes * SALAIRE
        entree_brute = round(self.ressources[0]*self.employes*self.prix_produit*production_modifier, 2)

        benefice_net = entree_brute - salaires

        return (benefice_net, entree_brute, salaires)

    def add_tresorerie(self, amount: int):
        self.tresorerie += amount
    
    def use_tresorerie(self, amount: int):
        if self.tresorerie >= amount:
            self.tresorerie -= amount
        else:
            print("Vous n'avez pas assez d'argent")

    #fonctions utiles pour manipuler les employes
    
    def add_employes(self, amount: int):
        self.employes += amount

    def licenciement(self, amount: int):
        if amount <= self.employes:
            self.employes -= amount
        else:
            print("vous essayez de licencier plus de personnes que vous n'avez d'employés")

    #fonctions utiles pour manipuler les ressources
    
    def add_ressources(self, index: int, amount: int):
        self.ressources[index] += amount
    
    def use_ressources(self, index: int, amount: int):
        if self.ressources[index] >= amount:
            self.ressources[index] -= amount
        else:
            print("Vous n'avez pas assez de ressources")
        
    #fonctions de display

    def display(self):
        print("---------", self.name, "---------")
        print("tresorerie : ", self.tresorerie, "  || materiel           : ", self.ressources[0])
        print("employés   : ", self.employes, "  || matières premières : ", self.ressources[1])
