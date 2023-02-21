import tkinter as tk 
from utils.entreprise import Entreprise

HEIGHT = 700
WIDTH = 700

class App(tk.Tk):

    def __init__(self, entreprise: bool|Entreprise = False):

        super().__init__()
        
        self.config(bg="grey", width=WIDTH, height=HEIGHT)
        self.geometry("700x700")

        #definition du header avec l'affichage de toutes les statistiques

        self.moneyVar = tk.IntVar(self, value = entreprise.tresorerie)
        self.employesVar = tk.IntVar(self, value = entreprise.employes)
        self.header = tk.Frame(self, bg= "darkgrey", height=50)
        self.stats = tk.Frame(self.header)
        self.money = tk.Label(self.stats, text= "trésorerie : {}".format(self.moneyVar.get()))
        self.employes = tk.Label(self.stats, text= "employés : {}".format(self.employesVar.get()))
        self.name = tk.Label(self.header, text= entreprise.name, justify="center")

        self.name.pack(fill="y")
        self.employes.pack(side="top" ,fill="x")
        self.money.pack(side="top" ,fill="x")
        self.stats.pack(side="left" ,fill="x")
        self.header.pack(side="top" ,fill="x")


    def tour(self):
        pass