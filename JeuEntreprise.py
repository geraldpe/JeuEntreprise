from entreprise import Entreprise

def main():
    name = str(input("choisissez un nom pour votre entreprise >> "))
    entreprise = Entreprise(name)
    entreprise.display()


if __name__ == "__main__":
    main()