import tkinter as tk 
from utils.entreprise import Entreprise

HEIGHT = 700
WIDTH = 700


class App(tk.Tk):

    def __init__(self, entreprise: bool|Entreprise = False):

        super().__init__()
        
        self.config(bg="grey", width=WIDTH, height=HEIGHT)


    def tour(self):
        pass