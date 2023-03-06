from entreprise import Entreprise

def choix_daction() -> int:
    answer = ""
    while type(answer) != int or answer not in (1, 2, 3):
        print("que voulez vous faire ? ")
        print("1 - acheter des ressources")
        print("2 - embaucher des employés")
        print("3 - quitter")
        answer = eval(input("votre choix >> "))
    
    return answer

def achat_ressources(entreprise: Entreprise, prix_ressources: list[int] = [50, 100]):
    """
    fonction d'interface pour permettre au joueur de choisir les ressources dans lesquelles il veut
    investir et la quantité qu'il veut acheter
    """
    ressource = ""
    while type(ressource) != int or ressource not in (1, 2):
        print("Dans quelles ressources voulez vous investire ? ")
        print("1 - du Matériel ({}€/p)".format(prix_ressources[0]))
        print("2 - matières premieres ({}€/p)".format(prix_ressources[1]))
        ressource = eval(input("votre choix >> "))
    
    ressource -= 1 #pour transformer le choix en index d'une liste
    amount = ""
    while type(amount) != int:
        amount = eval(input("quantité de ressources >>"))
        try:
            if amount*prix_ressources[ressource] > entreprise.tresorerie:
                amount = ""
                print("Vous voulez investir dans trop de ressources par rapport à vos finances")
        except:
            pass
    
    entreprise.use_tresorerie(amount*prix_ressources[ressource])
    entreprise.add_ressources(ressource, amount)

def embauche(entreprise: Entreprise):
    """
    fonction pour gérer l'embauche de nouvelles personnes dans l'entreprise
    """
    employes = ""
    while type(employes) != int:
        employes = eval(input("combien de personnes voulez vous embaucher ? >> "))

    entreprise.add_employes(employes)

def main():
    name = str(input("choisissez un nom pour votre entreprise >> "))
    entreprise = Entreprise(name)

    #boucle de jeu : 

    running = True
    tour = 0
    while running:
        print(tour, "--------------------------------------------------------| \n\n")
        entreprise.display()
        #choix d'action : 
        choice = choix_daction()
        if choice == 1:
            achat_ressources(entreprise)
        elif choice == 2:
            embauche(entreprise)
        else:
            running = False
            break

if __name__ == "__main__":
    main()