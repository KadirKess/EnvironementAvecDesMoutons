# Import des librairies dont nous aurons besoin
from random import randint # Cela va nous permettre d'intégrer l'aléatoire dont nous aurons besoin à plusieurs endroits
import matplotlib # On aura besoin de cette librairie notamment pour tracer des graphes

# On génère des noms pour les différents individus de l'écosystème 

# On veut une liste de noms pour chaque groupe :
noms_moutons = ["Marco Polo"] 
noms_loups = ["Lou Le Grand"]
noms_chasseurs = ["Casseur Flowter"]
# On crée une fonction qui ajoute la quantité de noms voulus aux listes :
def noms(liste,nb):
    '''
    Cette fonction rajoute à la liste voulue une quantité de noms voulus
    Prec : Le nom de ce qu'il faut nommer (str) et la quantité de noms voulus (int)
    Postc : La liste demandée avec la quantité de noms voulus (list)
    '''
    if liste == "moutons":
        liste = noms_moutons
    elif liste == "chasseurs":
        liste = noms_chasseurs
    elif liste == "loups":
        liste = noms_loups
    for i in range (nb):
        liste.append(liste[0] + " " + str(i + 1))
    liste[0] = liste[0] + " L'Original"
    return liste

# Création des différentes classes

class Monde :
    # Cette classe représente le monde dans lequel évolue l'écosystème, plus précisément sa carte, sous forme d'un matrice carrée de côté x

    def __init__(self, dimension, duree_repousse): 
        '''
        On définit l'objet Monde
        Prec : Une dimension (int), qui sera la longueur x du côté de la matrice carrée, et une duree de repousse (int) qui définira la durée de repousse de l'hebre
        Post : L'objet monde
        '''
        self.__dimension = dimension # On récupère la dimension qu'aura la carte
        self.__carte = [
            [0 for i in range (dimension)]for i in range (dimension) # On crée une matrice carrée d'entiers de côté x, chaque élément est un entier qui contient de l'herbe
            ] 
        for i in range (len(self.__carte)): # On rempli une case sur deux avec de l'herbe, sur la case vide, on met un debout de repous
            if i%2 == 0:
                for j in range (len(self.__carte[i])):
                    if j%2 == 0:
                        self.__carte[i][j] = duree_repousse
                    else:
                        self.__carte[i][j] = randint(0, duree_repousse - 1)
            else :
                for j in range (len(self.__carte[i])):
                    if j%2 == 0:
                        self.__carte[i][j] = randint(0, duree_repousse - 1)
                    else:
                        self.__carte[i][j] = duree_repousse
        self.__herbe_repousse = duree_repousse # On définit la durée de repousse de l'herbe

    def __repr__(self):
        '''
        On renvoie la liste de listes qui représente la matrice carrée qui représente elle-même le monde
        Postc : La carte du monde (de type Monde) exprimée sous forme de liste (list) de listes (list)
        '''
        return str(self.__carte)

    def get_info(self):
        '''
        Cette fonction va nous permette de récupérer les attributs de l'objet
        Prec : Demande des attributs
        Post : Un dictionnaire (dict) avec les attributs
        '''
        return dict(
            {
            "dimension" : self.__dimension, 
            "repousse" : self.__herbe_repousse
            }
            )

    def herbePousse(self):
        '''
        On fait pousser l'herbe dans chaque case de la matrice
        Postc : La matrice monde (Monde) avec chaque case qui a gagné un niveau de repousse d'herbe
        '''
        for i in range (len(self.__carte)): # On parcours les listes de listes
            for j in range (len(self.__carte)): # On parcours les sous-listes
                self.__carte[i][j] += 1 # On incrémente une valeur d'herbe

    def herbeMangee(self,x,y):
        '''
        On retire l'herbe d'une case de la matrice
        Prec : Un x (int) et un y (int) qui inidiquent une case à réitnitalisée
        Post : La matrice (Monde) avec la case réinitialisée
        '''
        self.__carte[x][y] -= self.__herbe_repousse
 
    def getCoefCarte(self, x, y):
        '''
        On cherhce l'entier (int) qui se trouve dans la case d'indice donnée en paramètre
        Prec : Un x (int) et un y (int) servants d'indices pour trouver la case
        Postc : L'entier qui se trouve dans la case demandée
        '''
        return int(self.__carte[x][y])

# On crée un monde de dimension 50 et avec une durée de repousse de 30
monde = Monde(50, 30)

class Mouton :
    # Cette classe représente ce qu'est un mouton, et la façon dont il va pouvoir vivre et évoluer dans l'écosystème

    def __init__(self, gain_n, x, y, duree_laine, taux_rep):
        '''
        On définit l'objet Mouton, il aura comme attributs un gain de nourriture par carré d'herbe, une position sur le monde, une énergie qui se remplit quand il mange (int), niveau de laine que des coutiriers peuvent récupérer (int), et un taux de reproduction qui définit ses chances de se reproduire en pourcentage
        Prec : Un gain de nourriture, notée gain_n (int), une position x (int) et y (int), une durée de production de laine (int), et un taux de reproduction (int)
        Postc : Un mouton (Mouton) avec ses différents attributs
        '''
        self.__gain_nourriture = gain_n # On définit le gain de nourriture par carré d'herbe mangé
        self.__positionx = x # On donne une position x
        self.__positiony = y # On donne une position y
        self.__energie = randint(1, 2) * gain_n # On donne une valeur d'énergie initale au mouton qui représente soit un soit deux carrés d'herbe mangés
        self.__repousse_laine = duree_laine # On définit le temps que met la laine à avoir pousser et être récupérable 
        self.__laine = 0 # On définit un attribut qui va contenir la laine du mouton
        self.__taux_rep = taux_rep # On définit le taux de reproduction
        # On donne un nom aléatoire au mouton
        name = noms_moutons[randint(0, len(noms_moutons) - 1)]
        self.__nom = name
        noms_moutons.remove(name)

    def __repr__(self):
        '''
        On définit une fonction __repr__ juste comme ça
        Postc : Une phrase (str) qui donne le nom du mouton et "vous dit bonjour"
        '''
        return str(self.__nom)+" vous dit bonjour !"

    def get_infos(self): # On n'utilise pas la fonction __repr__ pour obtenir un dictionnaire à la sortie
        '''
        La fonction va nous servir à récupérer les données du mouton
        Prec : Un mouton (Mouton)
        Post : Un dictionnaire (dict) avec toutes ces informations
        '''
        return dict(
            {
            "noms" : self.__nom, 
            "position" : [self.__positionx,self.__positiony], 
            "energie" : self.__energie, 
            "laine" : self.__laine, 
            "laine_repousse" : self.__repousse_laine, 
            "taux_reproduction" : self.__taux_rep
            }
            )
    
    def variationEnergie(self):
        '''
        On crée la fonction qui va permettre au mouton de restaurer son énergie en mangeant de l'herbe ou d'en perdre s'il n'en mange pas 
        Prec : Un mouton (Mouton) avec une position x et y
        Post : Le mouton a reçu ou non de l'énergie (int) s'il y avait de l'herbe sur sa case, sinon il en perd, l'herbe mangée est aussi retirée de la case
        '''
        monde_infos = monde.get_info()
        if monde_infos["repousse"] <= monde.getCoefCarte(self.__positionx,self.__positiony): # On vérifie s'il y a assez d'herbe sur la case pour qu'elle soit mangée
            self.__energie += self.__gain_nourriture # On ajoute l'énergie au mouton
            monde.herbeMangee(self.__positionx,self.__positiony) # On retire l'herbe mangée de la case
        else:
            self.__energie = self.__energie - 1

        return self.__energie
    
    def deplacement(self):
        monde_infos = monde.get_info()
        '''
        On crée une fonction qui va faire se déplacer le mouton (Mouton) dans une des huits cases qui l'entourent
        Prec : Le mouton (Mouton) à sa position initale
        Post : Le mouton (Mouton) avec sa nouvelle position
        '''
        self.__positionx = (self.__positionx + randint(-1, 1)) % monde_infos["dimension"] # On ajoute aléatoirement une valeur comprise entre -1 et 1 à sa position x, on garde le reste de la division par 50 car le monde est torique
        self.__positiony = (self.__positiony + randint(-1, 1)) % monde_infos["dimension"] # On fait de même avec la position y

    def place_mouton(self, x, y):
        '''
        Cette fonction va servir à placer un mouton à des coordonnées données en paramètre
        Prec : Un mouton (Mouton) et les coordonnées (int) auxquelles il faut le placer
        Post : Le mouton placé sur ces coordonéens
        '''
        self.__positionx = x # On donne une position x
        self.__positiony = y # On donne une position y
    
    def laine_pousse(self):
        '''
        On fait pousser la laine du mouton
        Prec : Un mouton (Mouton)
        Postc : Le mouton avec sa laine qui a poussé
        '''
        if self.__laine < self.__repousse_laine: # Si le mouton n'a pas trop de laine déjà sur lui
            self.__laine += 1

    def laine_coupee(self):
        '''
        On coupe la laine du mouton
        Prec : Un mouton (Mouton)
        Postc : Ce mouton sans la laine qu'il avait auparavant
        '''
        self.__laine = 0

# On crée un mouton de test
mouton = Mouton(5, 1, 2, 3, 5)

class Simulation :
    # Cette classe va gérer la simulation

    def __init__(self, nb_moutons, fin):
        '''
        On définit l'objet Simualation, il aura comme attributs un nombre de moutons (qui représente le nombre de moutons initialement présents sur la carte), une horloge (int) (initée à 0), une liste des moutons (list), une valeur de temps qui définira la fin du monde, une instance de la classe Monde, le nombre de carré d'herbe (list) trouvé au fur et à mesure de la simulation, idem pour les moutons
        Prec : Un nombre inital de moutons (int), une valeur pour laquelle l'horloge devra s'arrêter (int), une instance du monde (Monde)
        Postc : Les deux listes (list) de résultats
        '''
        self.__nb_moutons = nb_moutons # Le nombre de moutons initaux
        self.__horloge = 0 # L'horloge initée à 0
        self.__fin_du_monde = fin # L'heure (par rapport à l'horle créée auparavant) de fin du monde, et donc fin de la simulation
        self.__moutons = []
        self.__resulats_herbe = []
        self.__resulats_moutons = []