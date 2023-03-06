
SALAIRE = 1150

class Entreprise:

    def __init__(self, name: str, tresorerie: int = 1000, employes = 1, ressources: list[int] = [0, 0]):
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
    
    #fonctions utiles pour manipuler la tresorerie

    def calcul_benefice(self):
        salaires = self.employes * SALAIRE

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
