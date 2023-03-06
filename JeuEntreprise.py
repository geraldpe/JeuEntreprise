from entreprise import Entreprise
import random


def investissement(entreprise: Entreprise, prix_ressources: list[int] = [50, 100, 200]) -> int:
    """
    fonction d'interface pour permettre au joueur de choisir les ressources dans lesquelles il veut
    investir (Materiel, matières premières, publicité ou rien du tout)
    """
    ressource = ""
    while type(ressource) != int or ressource not in (1, 2, 3, 4):
        print("Dans quelles ressources voulez vous investire ? ")
        print("1 - du Matériel ({}€/p)".format(prix_ressources[0]))
        print("2 - matières premieres ({}€/p)".format(prix_ressources[1]))
        print("3 - investir dans la publicité ({}€/p)".format(prix_ressources[2]))
        print("4 - Ne pas dépenser d'argent à ce tour")
        ressource = eval(input("votre choix >> "))
    
    
    ressource -= 1 #pour transformer le choix en index d'une liste
    if ressource == 3:
        return 0, 1
    elif ressource == 2:
        #on renvoie un nombre aleatoire qui va definir l'efficacité de la publicité
        modifier = round(random.random() + 1, 2)
        entreprise.use_tresorerie(prix_ressources[ressource])
        return prix_ressources[ressource], modifier
    amount = ""
    while type(amount) != int:
        amount = eval(input("quantité de ressources >> "))
        try:
            if amount*prix_ressources[ressource] > entreprise.tresorerie:
                amount = ""
                print("Vous voulez investir dans trop de ressources par rapport à vos finances")
        except:
            pass
    
    entreprise.use_tresorerie(amount*prix_ressources[ressource])
    entreprise.add_ressources(ressource, amount)
    return amount*prix_ressources[ressource], 1

def gestion_du_personnel(entreprise: Entreprise):
    answer = ""
    while type(answer) != int or answer not in (1, 2, 3):
        print("Que voulez vous faire de vos employés ? ")
        print("1 - Embaucher de nouvelles personnes")
        print("2 - licencier du personnel")
        print("3 - Ne rien faire")
        answer = eval(input("votre choix >> "))
    
    if answer == 3:
        return 0
    elif answer == 2:
        amount = ""
        while amount > entreprise.employes:
            amount = eval(input("combien d'employés voulez vous licencier ? >> "))

        entreprise.licenciement(amount)
    else:
        amount = ""
        while type(amount) != int:
            amount = eval(input("combien de personnes voulez vous embaucher ? >> "))

        entreprise.add_employes(amount)

def show_benef(benef: tuple):
    print("entree d'argent brute : {}".format(benef[1]))
    print("salaires : {}".format(benef[2]))
    print("benefice net : {}".format(benef[0]))


def main():
    name = str(input("choisissez un nom pour votre entreprise >> "))
    entreprise = Entreprise(name)

    #boucle de jeu : 

    running = True
    tour = 0
    prod_modifier = 1
    while running:
        print(tour, "--------------------------------------------------------| \n\n")
        benef = entreprise.calcul_benefice(prod_modifier)
        entreprise.add_tresorerie(benef[0])
        entreprise.display()

        
        show_benef(benef)
        
        #investissement : 
        invested, prod_modifier = investissement(entreprise)
        print("vous avez investi : {}".format(invested))
        print("")
        
        #gestion du personnel : 
        gestion_du_personnel(entreprise)
        print("")
        tour += 1

if __name__ == "__main__":
    main()