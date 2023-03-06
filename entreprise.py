

class Entreprise:

    def __init__(self, name: str, tresorerie: int = 0, employes = 1, ressources: list|int = [0, 0, 0]):
        self.name = name
        self.tresorerie = 0
        self.employes = employes
        self.ressources = ressources
    
    #fonctions utiles pour manipuler la tresorerie

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
        print("tresorerie : ", self.tresorerie)
        print("employés   : ", self.employes)
