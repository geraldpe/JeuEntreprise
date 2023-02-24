import tkinter as tk 
from utils.entreprise import Entreprise

HEIGHT = 700
WIDTH = 700

MENU_COLOR = "darkgrey"

class Header(tk.Frame):

    def __init__(self, root, entreprise: Entreprise):

        super().__init__(root, bg= MENU_COLOR, height=50)

        self.entreprise = entreprise

        self.moneyVar = tk.StringVar(self, value = "trésorerie : {}".format(entreprise.tresorerie))
        self.employesVar = tk.StringVar(self, value = "employés : {}".format(entreprise.employes))
        self.stats = tk.Frame(self)
        self.money = tk.Label(self.stats, textvariable= self.moneyVar)
        self.employes = tk.Label(self.stats, textvariable= self.employesVar)
        self.name = tk.Label(self, text= entreprise.name, justify="center")

        self.name.pack(fill="y")
        self.employes.pack(side="top" ,fill="x")
        self.money.pack(side="top" ,fill="x")
        self.stats.pack(side="left" ,fill="x")
    
    def pack(self):
        super().pack(side="top", fill="x")

    def update_money(self):
        self.moneyVar.set("trésorerie : {}".format(self.entreprise.tresorerie))


class EnterpriseCreatorMenu(tk.Frame):

    def __init__(self, root):

        super().__init__(root, bg = MENU_COLOR, padx=20, pady=20)

        self.nameFrame = tk.Frame(self, border=None, bg=MENU_COLOR)
        self.nameLabel = tk.Label(self, text="Nom de votre entreprise", bg=MENU_COLOR)
        self.nameEntry = tk.Entry(self)


        self.nameLabel.pack(side="left")
        self.nameEntry.pack(side="left")
        self.nameFrame.pack(fill="x")

    def pack(self):
        super().pack(fill="both")

class App(tk.Tk):

    def __init__(self, entreprise: bool|Entreprise = False):

        super().__init__()
        
        self.entreprise = entreprise
        self.config(bg="grey", width=WIDTH, height=HEIGHT)
        self.geometry("700x700")

        if not entreprise:
            menu = EnterpriseCreatorMenu(self)
            menu.pack()
        #definition du header avec l'affichage de toutes les statistiques
        


    def init_header(self):
        self.header = Header(self, self.entreprise)
        self.header.pack()

    def add_money(self, amount: int):
        self.entreprise.tresorerie += amount
        print(self.entreprise.tresorerie)
        self.header.update_money()
        self.header.money.update()
        


    def tour(self):
        pass