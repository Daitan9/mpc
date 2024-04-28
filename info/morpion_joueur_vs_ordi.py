from fltk import *
from random import randint

def resultat_joueur(lst,joueur):
    for k in range(3):
        if lst[0][k]==lst[1][k]==lst[2][k]==joueur:
            return True
        if lst[k][0]==lst[k][1]==lst[k][2]==joueur:
            return True
    
        if lst[0][0]==lst[1][1]==lst[2][2]==joueur:
            return True
        elif lst[0][2]==lst[1][1]==lst[2][0]==joueur:
            return True
    return False

# construction grille
cree_fenetre(300,300)
for k in range(3):
    ligne(k*100,0,k*100,299)
    ligne(0,k*100,299,k*100)
    

#création matrice du jeu
lst=[[0,0,0],[0,0,0],[0,0,0]]   

c=0

while True:
    ev = donne_ev()
    tev=type_ev(ev)
    if tev=='ClicGauche':
        x=abscisse(ev)
        y=ordonnee(ev)
 
        #récupérer numéro de la case correspondante
        j=x//100
        i=y//100
       
        #si la case a déjà été jouée
        if lst[i][j]!=0:
             print('La case a déjà été jouée !')
        
        #mise à jour matrice du jeu + création rond
        else:        
            lst[i][j]=1
            cercle(50+j*100,50+i*100,50,couleur='indigo')
                
            #vérification si le joueur a gagné ou pas
            if resultat_joueur(lst,1):
                print("Le joueur 1 a gagné !!")
                break
            
            if c==4:
                print("Match nul")
                break
                
            #création croix de l'ordi
            a=randint(0,2)
            b=randint(0,2)
            while True:
                if lst[a][b]!=0:
                    a=randint(0,2)
                    b=randint(0,2)
                else:
                    break
            lst[a][b]=2
            attente(0.5)
            ligne(0+b*100,0+a*100,100+b*100,100+a*100,couleur='darkolivegreen')
            ligne(100+b*100,0+a*100,0+b*100,100+a*100,couleur='darkolivegreen')
                
            mise_a_jour()
            #vérification si l'ordi a gagné ou pas
            if resultat_joueur(lst,2):
                print("L'ordinateur a gagné !!")
                break
        
        
        c=c+1
    
    if tev=='Quitte':
        break
    
    mise_a_jour()

attend_ev()  
ferme_fenetre()