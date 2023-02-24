from game import App
from utils.entreprise import Entreprise

def main():
    entreprise = Entreprise("test")
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()