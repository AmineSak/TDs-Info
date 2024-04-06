import matplotlib.pyplot as plt
from time import perf_counter

# ====== Classs ====== #

class hashtable:
    
    def __init__(self, h, N):
        self.capacity = N
        self.table = [[None] for i in range(self.capacity)]
        self.hash_function = h

    def show(self):
        """prints the representation of self"""
        print(self.table)
    
    def put(self, key, value):
        """ Adds (key,value) to self using the hash function"""
        index = self.hash_function(key) % self.capacity
        
        if (key,value) not in self.table[index] :
            self.table[index].append((key,value))
        else:
            for elt in self.table[index] : 
                if elt[0] == key:
                    self.table[index].remove(elt)
                    self.table[index].append(elt)
    
    def get(self ,key):
        """ Returns value of key if (key,value) in self """
        index = self.hash_function(key) % self.capacity
        i=0
        while i < len(self.table[index])-1:
            if self.table[index][i] == None:
                i += 1
            if self.table[index][i][0] == key :
                    return self.table[index][i][1]
        return None
          
    def repartition(self, couleur):
        """Returns the distibution of collisions in self """
        x=range(self.capacity)
        y=[]
        for elt in self.table:
            y.append(len(elt))
        return plt.bar(x,y,color=couleur)
    
    def resize(self):
        """ Doubles the size of self.table """
        self.capacity = self.capacity*2
        self.table = [[None] for i in range(self.capacity)]
    
    def __setitem__(self,key,value):
        """syntaxe self[key] = value"""
        self.put(key,value)

    def __getitem__(self,key):
        """syntaxe self[key] """
        self.get(key)
        




# ====== Functions ===== #
def hashage_naif(key : str):
    hashVal = 0
    for char in key:
        hashVal += ord(char)
    return hashVal

def hashage_horner(key: str):
    h=0
    for char in key:
        h += 33*h+ord(char)
    return h

def read_file(path):
    #fonction qui renvoie la liste des mots du lexique 
    f= open(path,'r')
    lexique=list()
    for line in f:
        mot=line[0:len(line)-1]
        if len(mot) <= 8:
            lexique.append(mot)
    f.close()
    return lexique

def liste_longueurs(l):
    #fonction qui renvoie la liste des longuerus des mots du lexique 
    L=[]
    for elt in l:
        L.append(len(l))
    return L

def list_tuple(l):
    ##fonction qui renvoie la liste des tuples: (mot,longueur)
    T=[]
    L=liste_longueurs(l)
    for elt in l:
        T.append((elt,l.index(elt)))
    return T

def put_all(d,ht):
    # fonction qui prend en argument une liste de tuple (key,value) et qui les ajoute à la table de hashage ht
    for elt in d:
        ht.put(elt[0],elt[1])
               
def nb_elt(table):
    r=0
    for elt in table:
        for tuple in elt:
            if tuple != None:
                r += 1
    return r



# ====== Script ====== #
if __name__ == "__main__":
    ht= hashtable(hashage_naif , 16)
    t_start = perf_counter()
    ht['abc'] = 3
    t_end = perf_counter()
    print("Elapsed time of adding :",t_end-t_start)
    t_start = perf_counter()
    ht['abc']
    t_end = perf_counter()
    print(ht.get('abc'), "Elapsed time of getting :",t_end-t_start)
    
    #Creation de la liste liste_tuple contenant les tuples ("mot",longueur) 
    lexique= read_file(r'C:\Users\Amine Sakouhi\OneDrive\Desktop\Programmation et Structures de données/frenchssaccent')
    liste_tuple=list_tuple(lexique)

    #Visualisation de la répartition des collisions pour le hashage_naif et le hashage_horner
    dictionnaire_naif=hashtable(hashage_naif ,1000)
    t_start = perf_counter()
    put_all(liste_tuple,dictionnaire_naif)
    t_end = perf_counter()
    print("Elapsed time of adding 48843 tuple to dictionnaire_naif:",t_end-t_start)
    dictionnaire_horner=hashtable(hashage_horner ,1000)
    t_start = perf_counter()
    put_all(liste_tuple,dictionnaire_horner)
    t_end = perf_counter()
    print("Elapsed time of adding 48843 tuple to dictionnaire_horner:",t_end-t_start)
    print(dictionnaire_naif.repartition('blue'))
    print(dictionnaire_horner.repartition('red'))
    plt.title("répartition des collisions pour le hashage_naif et le hashage_horner")
    plt.ylabel("Nombre de tuple par case")
    plt.xlabel("Numéro de la case")
    plt.legend(["hashage_naif","hashage_horner"])
    plt.show()
    plt.close('all')
    
#Ex1:
#1) on peut représenter la table de hachage
#2) on peut ajouter une clé et sa valeur
#3) on peut mettre à jour une valeur
#4)  " " renvoyer la valeur d'une clé ou inversement