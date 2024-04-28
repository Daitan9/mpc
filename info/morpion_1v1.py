from fltk import *

def resultat_joueur(lst,joueur):
    for k in range(3):
        if lst[0][j+k]==lst[1][j+k]==lst[2][j+k]==joueur:
            return True
        if lst[i+k][0]==lst[i+k][1]==lst[i+k][2]==joueur:
            return True
    
        if lst[0][0]==lst[1][1]==lst[2][2]==joueur:
            return True
        elif lst[0][2]==lst[1][1]==lst[2][0]==joueur:
            return True
        else: 
            return False


# construction grille
cree_fenetre(300,300)
for k in range(3):
    ligne(k*100,0,k*100,299)
    ligne(0,k*100,299,k*100)
    

#création matrice du jeu
lst=[[0,0,0],[0,0,0],[0,0,0]]   

joueur=1
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
             texte(45,150,'La case a déjà été jouée',couleur='black',taille=15,tag='texte')
             attente(0.5)
             efface('texte')
        
        #mise à jour matrice du jeu + création rond
        else:    
            if joueur==1:
                lst[i][j]=1
                cercle(50+j*100,50+i*100,50,couleur='indigo')
                
            else:
                lst[i][j]=2
                ligne(0+j*100,0+i*100,100+j*100,100+i*100,couleur='darkolivegreen')
                ligne(100+j*100,0+i*100,0+j*100,100+i*100,couleur='darkolivegreen')
        
        #vérification si un joueur a gagné ou pas
        if resultat_joueur(lst,joueur):
            print("Le joueur "+str(joueur)+" a gagné !!")
            gagnant="Le joueur "+str(joueur)+" a gagné !!"
            texte(45,150,gagnant,couleur='black',taille=15)
            attente(1)
            break
        
        #vérification match nul
        if c==8:
            print("Match Nul")
            break
        
        #passage au joueur suivant
        if joueur==1:
            joueur=2
        else:
            joueur=1
        
               
        c=c+1
    
    if tev=='Quitte':
        break
    
    mise_a_jour()
  
ferme_fenetre()