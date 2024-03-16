dico_score={"a":1,"e":1,"i":1,"l":1,"n":1,"o":1,"r":1,"s":1,"t":1,"u":1,
            "k":10,"w":10,"x":10,"y":10,"z":10,
           "d":2,"g":2,"m":2,
            "b":3,"c":3,"p":3,
            "f":4,"h":4,"v":4,
            "j":8,"q":8}






# =================================== Functions
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
            
def isMotPossible(tirage, mot):
    #fonction qui renvoi True si on ne peut pas écrire le mot avec le tirage
    l=list(mot)
    t=tirage.copy()
    for elt in mot:
        if elt in t:
            t.remove(elt)
            l.remove(elt)
               
    if l == []:
        return True
    else:
        return False
                
                
    
def liste_mot_possible(tirage,path):
    #creation de la liste des mots possibles
    return [ elt for elt in read_file(path) if isMotPossible(tirage,elt)]


def mot_plus_long(tirage,path):
    l=liste_mot_possible(tirage,path)
    mot_long=l[0]
    i = 0
    while i<len(l)-1:
        i+=1
        if len(l[i])> len(mot_long):
            mot_long=l[i]
    
    return mot_long

#=====================ex3
def score(mot):
    #fonction qui renvoie le score d'un mot
    score=0
    for elt in mot:
        score += dico_score[elt]
    return score

def max_score(liste_mots):
    #fonction qui renvoie le mot qui a le score maximal 
    score_max= score(liste_mots[0])
    mot_gagnant=liste_mots[0]
    for mot in liste_mots:
        if score(mot) > score_max:
            score_max= score(mot)
            mot_gagnant= mot
    return score_max,mot_gagnant



# =========== Script/main
#ex1:
#1) lire le ficher et créer un liste contenant les mots composés de au plus 8 lettres
#2) créer une liste des mots possibles à partir de la liste tirage
#3) retourner le mot le plus long

#Ex 3 :
# On peut créer un dictionnaire qui a pour clés les lettre et valeurs les scores

