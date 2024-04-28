from fltk import *
from random import randint
from random import choice

#...............................FONCTIONS UTILES..............................#
def accueil():
    #crée la fenetre d'accueil
    cree_fenetre(500,500)
    rectangle(2,2,498,498,remplissage='lightgrey',couleur='black')
    texte(100,50,'BATAILLE NAVALE',couleur='black',police='Garamond',taille=25)
    for k in range(50):
        texte(10*k,65,'.',couleur='black',taille=20)
    rectangle(155,205,355,255,remplissage='grey',couleur='grey')
    rectangle(155,305,355,355,remplissage='grey',couleur='grey')
    rectangle(150,200,350,250,remplissage='white',couleur='black')
    rectangle(150,300,350,350,remplissage='white',couleur='black')
    texte(160,210,'Comment jouer ?',couleur='black',police='Garamond',taille=20)
    texte(170,310,'Lancer la partie',couleur='black',police='Garamond',taille=20)
    
    mise_a_jour()

def règles():
    #crée la mise en page des règles
    rectangle(2,2,498,498,remplissage='lightgrey',couleur='black')
    texte(150,30,'Comment jouer ?',couleur='black',police='Garamond',taille=25)
    for k in range(50):
        texte(10*k,45,'.',couleur='black',taille=20)
    cercle(20,110,2,remplissage='black')
    texte(30,100,'Placement des bateaux :',couleur='black',police='Garamond',taille=15)
    ligne(30,120,210,120)
    texte(40,130,'- clic gauche : bateau horizontal',couleur='black',police='Garamond',taille=15)
    rectangle(300,130,400,150,couleur='black')
    texte(40,160,'- clic droit : bateau vertical',couleur='black',police='Garamond',taille=15)
    rectangle(260,160,280,260)
    texte(40,270,'- touche "E" : efface le dernier bateau posé',couleur='black',police='Garamond',taille=15)
    
    cercle(20,320,2,remplissage='black')
    texte(30,310,'Phase de tirs :',couleur='black',police='Garamond',taille=15)
    ligne(30,330,135,330)
    texte(40,340,'- clic gauche : tirs',couleur='black',police='Garamond',taille=15)
  
    mise_a_jour()

def choix_options():
    #crée la mise en page des options
    rectangle(2,2,498,498,remplissage='lightgrey',couleur='black')
    texte(130,30,'Choix des options',couleur='black',police='Garamond',taille=25)
    for k in range(50):
        texte(10*k,45,'.',couleur='black',taille=20)
    texte(50,100,'"En vue" : permet de détecter si un bateau est à proximité du tir',police='Garamond',taille=15)   
    texte(50,150,"Mode triche : apparition des bateaux de l'ordinateur",police='Garamond',taille=15)
    rectangle(20,100,40,120,couleur='black')
    rectangle(20,150,40,170,couleur='black')
    rectangle(295,400,455,450,remplissage='grey',couleur='black')
    texte(302,410,'Lancer la partie',police='Garamond',taille=19)

    
def interface(h):
    #crée la fenêtre da la bataille navale
    cree_fenetre(21*h+10,15*h+10)
    rectangle(2,2,21*h+8,15*h+8,remplissage='white',couleur='black')
    rectangle(20,50,10*h+20,11*h,remplissage='lightblue',couleur='grey')
    rectangle(11*h-10,50,20*h+40,11*h,remplissage='lightblue',couleur='grey')
    for k in range(9):
        ligne(20+(k+1)*h,50,20+(k+1)*h,50+10*h,couleur='grey')
        ligne(20,50+(k+1)*h,20+10*h,50+(k+1)*h,couleur='grey')
        ligne(40+(11+k)*h,50,40+(11+k)*h,50+10*h,couleur='grey')
        ligne(40+10*h,50+(k+1)*h,40+20*h,50+(k+1)*h,couleur='grey')
        texte(10*h+27,h//2+h*k+45,str(k+1),couleur='black',taille=10)
    for k in range(10):
        texte(h//2+h*k+15,33,chr(65+k),couleur='black',taille=10)
        texte(h//2+h*(k+10)+35,33,chr(65+k),couleur='black',taille=10)
    texte(10*h+23,h//2+h*k+45,'10',couleur='black',taille=10)
    texte((10*h)//2-1.6*h,2,'Zone des bateaux',police='Cambria',taille=20)
    texte(10*h+(10*h)//2-10,2,'Zone de tirs',police='Cambria',taille=20)
    mise_a_jour()    
    
def zeros(n,m):
    #crée une liste de liste représentant la grille du jeu
    lst=[]
    matrice=[]
    for k in range(m):
        lst.append(0)
    for i in range(n):
        matrice.append(lst.copy())
    return matrice

def flotte():
    #affiche la flotte disponible du joueur au départ
    texte(25,10*h+90,'Votre flotte :',police='Cambria',taille=15,tag='flotte')
    for k in range(3):
        rectangle(30+30*k,10*h+220,60+30*k,10*h+250,remplissage='royalblue3',couleur='black')
        rectangle(30+30*k,10*h+185,60+30*k,10*h+215,remplissage='royalblue3',couleur='black')
    for k in range(4):
        rectangle(30+30*k,10*h+150,60+30*k,10*h+180,remplissage='royalblue3',couleur='black')
    for k in range(5):
        rectangle(30+30*k,10*h+115,60+30*k,10*h+145,remplissage='royalblue3',couleur='black')

def zone_bateau(x,y,orientation,t):
    #renvoie True si le bateau ne serait pas placé en dehors de sa zone
    if x<20:
        return True
    
    if y<50 or y>(10*h+50):
        return True 
    
    if orientation==1:
        return x>(520-(t-1)*h)

    if orientation==2:
        return y>(550-(t-1)*h)

def chevauchement(lst,i,j,orientation,t):
    #renvoie True si la case aurait déjà été jouée par des bateaux
    if orientation==1:
        for k in range(t):
            if lst[i][j+k]!=0:
                return True
        else :
            return False
    
    if orientation==2:
        for k in range(t):
            if lst[i+k][j]!=0:
                return True
        else :
            return False

def placement_bateau(lst,i,j,orientation,t):
    #modifie la grille lorsqu'un bateau est placé
    if orientation==1:
        for k in range(t):
            lst[i][j+k]=c+2  
    else:
        for k in range(t):
            lst[i+k][j]=c+2

def affichage_bateau(orientation,i,j,x0,y0,t):
    #affiche les bateaux sur l'interface
    if orientation==1:
        rectangle(h*j+x0+5,h*i+y0+5,h*(j+t)+x0-5,h*(i+1)+y0-5,tag=('B'+str(c+2)))
    else:
        rectangle(h*j+x0+5,h*i+y0+5,h*(j+1)+x0-5,h*(i+t)+y0-5,tag=('B'+str(c+2)))
    mise_a_jour()
    
def zone_tirs(x,y):
    #renvoie True si les tirs ne seraient pas dans la zone de tirs
    if x<x0t or x>(x0t+10*h) or y<y0 or y>(10*h+y0):
        return True

def affichage_tirs(lst,i,j,x0,y0,couleur):
    #modifie la liste et/ou affiche les tirs sur l'interface
    if couleur=='navy':
        ligne(h*j+x0+5,i*h+y0+5,h*(1+j)+x0-5,(i+1)*h+y0-5, couleur='navy',epaisseur=3)
        ligne(h*(1+j)+x0-5,i*h+y0+5,h*j+x0+5,(i+1)*h+y0-5, couleur='navy',epaisseur=3)
    if couleur=='lightcoral':
        lst[i][j]=1
        cercle(h*(0.5+j)+x0,h*(i+0.5)+y0,h//4,remplissage='lightcoral',couleur='lightcoral')

def en_vue(lst,i,j):
    #renvoie True si un bateau est à proximité du tir effectué (diagonale+côté)
    if j>0 and lst[i][j-1]!=0 and lst[i][j-1]!=1: #gauche
        return True
    if j<9 and lst[i][j+1]!=0 and lst[i][j+1]!=1: #droite
        return True
    if i>0 and lst[i-1][j]!=0 and lst[i-1][j]!=1: #haut
        return True
    if i<9 and lst[i+1][j]!=0 and lst[i+1][j]!=1: #bas
        return True
    if i>0 and j>0 and lst[i-1][j-1]!=0 and lst[i-1][j-1]!=1: #diagonale haut-gauche
        return True
    if i<9 and j>0 and lst[i+1][j-1]!=0 and lst[i+1][j-1]!=1: #diagonale bas-gauche
        return True
    if i>0 and j<9 and lst[i-1][j+1]!=0 and lst[i-1][j+1]!=1: #diagonale haut-droite
        return True
    if i<9 and j<9 and lst[i+1][j+1]!=0 and lst[i+1][j+1]!=1: #diagonale bas-droite
        return True

def vérif_bateau_coulé(lst,n):
    #revoie True si le bateau n'a pas été coulé
    for a in range(len(lst)):
        for b in range(len(lst)):
            if lst[a][b]==n :
                return True

def affichage_mots(mot,x,y,taille,wait,tag):
    #affiche le texte désiré à l'endroit et à la taille voulus + renvoie dans la console le mot désiré + efface le texte au bout du moment désiré
    print(mot)
    texte(x,y,mot,couleur='black',taille=taille,tag=tag)
    attente(float(wait))
    efface(tag)

def tirs_stratégiques(a,b,stratA,stratB,cS,tirs_ordi):
    #renvoie des coordonnées de tirs a et b pour l'ordi de façon stratégique
    if cS>2:
        if stratA[cS]==stratA[cS-1]:
            if stratB[cS]>stratB[cS-1]:
                if stratB[cS]==9:
                    b=min(stratB)-1
                else:
                    b=choice([stratB[cS]+1,min(stratB)-1])
            if stratB[cS]<stratB[cS-1]:
                if stratB[cS]==1:
                    b=max(stratB)+1
                else:
                    b=choice([stratB[cS]-1,max(stratB)+1])
            a=stratA[cS]
        
        if stratB[cS]==stratB[cS-1]:
            if stratA[cS]>stratA[cS-1]:
                if stratA[cS]==9:
                    a=min(stratA)-1
                else:
                    a=choice([stratA[cS]+1,min(stratA)-1])
            if stratA[cS]<stratA[cS-1]:
                if stratA[cS]==1:
                    a=max(stratA)+1
                else:
                    a=choice([stratA[cS]-1,max(stratA)+1])
            b=stratB[cS]
                      
    elif cS==2:
        if stratA[cS]==stratA[cS-1]:
            if stratB[cS]>stratB[cS-1]:
                if stratB[cS]==9:
                    b=stratB[cS-1]-1
                elif stratB[cS-1]==1:
                    b=stratB[cS]+1
                else:
                    b=choice([stratB[cS]+1,stratB[cS-1]-1])

            else:
                if stratB[cS-1]==9:
                    b=stratB[cS]-1
                elif stratB[cS]==1:
                    b=stratB[cS-1]+1
                else:
                    b=choice([stratB[cS]-1,stratB[cS-1]+1])
            
            a=stratA[cS]
                        
        if stratB[cS]==stratB[cS-1]:
            if stratA[cS]>stratA[cS-1]:
                if stratA[cS]==9:
                    a=stratA[cS-1]-1
                elif stratA[cS-1]==1:
                    a=stratA[cS]+1
                else:
                    a=choice([stratA[cS]+1,stratA[cS-1]-1])

            else:
                if stratA[cS-1]==9:
                    a=stratA[cS]-1
                elif stratA[cS]==1:
                    a=stratA[cS-1]+1
                else:
                    a=choice([stratA[cS]-1,stratA[cS-1]+1])
            
            b=stratB[cS]
    
    elif cS==1:
        if a==9:
            r1=choice([0,-1])
        elif a==1:
            r1=choice([1,0])
        else:
            r1=randint(-1,1)
        a=stratA[cS]+r1
        if r1==-1 or r1==1:
            b=stratB[cS]
        else :
            if b==1:
                r2=1
            elif b==9:
                r2==-1
            else:
                r2=choice([-1,1])
            b=stratB[cS]+r2
    
    return a,b

###############################################################################
###############################################################################
accueil() #affichage de l'accueil
while True :
    ev=donne_ev()
    tev=type_ev(ev)
    
    if tev=='ClicGauche': 
        x=abscisse(ev) #coordonnées du clic
        y=ordonnee(ev)
        
        if 149<x<351 and 200<y<251: #si le clic est dans le rectangle pour "Comment jouer ?"
            efface_tout()
            règles() #affichage mise en page des règles
            attend_ev()
            break
        if 149<x<351 and 259<y<351: #si le clic est dans le rectangle "Lancer la partie"
            break
    
    if tev=='Quitte':
        ferme_fenetre()
        quit()
    mise_a_jour()
    
choix_options() #affichage des choix d'options
option1=0 #compteur nombre de clic pour l'option "en vue"
option2=0 #compteur nombre de clic pour l'option "triche"
while True :
    ev=donne_ev()
    tev=type_ev(ev)
    
    if tev=='ClicGauche':
        x=abscisse(ev) #coordonnées du clic
        y=ordonnee(ev)
        
        if 20<x<40 and 100<y<120: #si le clic est dans le carré pour la fonction "en vue"
            option1+=1
            if option1%2!=0: #affiche sur l'interface une croix pour signifer que l'on désire l'option
                ligne(20,100,40,120,couleur='grey',tag='option1')
                ligne(40,100,20,120,couleur='grey',tag='option1')
            else: #efface la croix
                efface('option1')
        if 20<x<40 and 150<y<170: #si le clic est dans le carré pour la fonction "triche"
            option2+=1
            if option2%2!=0: #affiche sur l'interface un carré pour signifer que l'on désire l'option
                ligne(20,150,40,170,couleur='grey',tag='option2')
                ligne(40,150,20,170,couleur='grey',tag='option2')
            else: #efface la croix
                efface('option2')
        if 300<x<450 and 400<y<450 : #si le clic est dans "Lancer la partie"
            ferme_fenetre()
            break
    
    if tev=='Quitte':
        ferme_fenetre()
        quit()
    mise_a_jour()

# division des compteurs pour déterminer si l'on veut ou non l'option
if option1%2==0:
    option_en_vue=False
else:
    option_en_vue=True
if option2%2==0:
    debug_menu=False
else:
    debug_menu=True
    
#................................PLATEAU DE JEU...............................#    
h=50
interface(h) #affichage du plateau de jeu

taille=[3,3,4,5]  #liste des taille de bateaux à placer 
lstB=zeros(10,10) #liste de la grille des bateaux du joueur
lstT=zeros(10,10) #liste de la grille des tirs du joueur et des bateaux de l'ordi

x0b=20 #coordonnée de l'abscisse du point haut-gauche de la grille du joueur
x0t=10*h+40 #coordonnée de l'abscisse du point haut-gauche de la grille de l'ordi
y0=50 #coordonnée de l'ordonnée du point haut-gauche des grilles

#.........................PLACEMENT DES BATEAUX JOUEUR........................#
#---------------------------------CONVENTIONS---------------------------------#
#       0 : case vide
#       1 : bateau touché lors de la phase de tirs
#       2,3,4,5 : numéro du bateau placé
#-----------------------------------------------------------------------------#
c=0 #compteur bateau joueur
flotte() #affichage de la flotte de départ
while True :
    ev = donne_ev()
    tev = type_ev(ev)
    
    if tev=='ClicGauche' or tev=='ClicDroit' : 
        x=abscisse(ev) #coordonnées du clic
        y=ordonnee(ev)
        
        #récupére le numéro de la case correspondante
        j=(x-x0b)//h     #numéro colonne case
        i=(y-y0)//h      #numéro ligne case
        
        if tev=='ClicGauche':
            orientation=1
        else:
            orientation=2
        
        if c==len(taille): #vérifie si tous les bateaux placés
            efface('flotte')
            affichage_mots('Tous les bateaux ont été placés',2*h+20,10*h+55,15,0.5,'bateaux_placés')
            mise_a_jour()
            break
        else:
            t=taille[c]  #taille du bateau à placer
        
        if zone_bateau(x,y,orientation,t): #vérifie si le bateau se place dans la zone
            affichage_mots('Impossible de jouer ici !',3*h+20,10*h+55,15,0.2,'zone')
        else:
            if chevauchement(lstB,i,j,orientation,t): #vérifie si la case n'a pas déjà un bateau
                affichage_mots('La case a déjà été jouée',3*h+20,10*h+55,15,0.5,'chevauchement')
            else:
                placement_bateau(lstB,i,j,orientation,t) #changement de la grille
                affichage_bateau(orientation,i,j,x0b,y0,t) #affiche des bateaux sur l'écran
                rectangle(x0b,15*h-35*c-30,x0b+190,15*h-35*c,remplissage='white',couleur='white',tag=('B'+str(c+2))) #affiche un rectangle permettant de cacher le bateau de la flotte correspondant
                c+=1
    
    if tev == 'Touche':
        if touche(ev)=='e': #efface le dernier bateau qui a été placé, dans la grille, sur l'écran et dans la flotte
            if c>0:
                efface('B'+str(c+1))
                for i in range(len(lstB)): #remplace tous les chiffres attribués au bateau dans la liste par un 0 (case vide)
                    for j in range(len(lstB)):
                        if lstB[i][j]==c+1 :
                            lstB[i][j]=0                
                c=c-1 #compteur-1
            
    if tev=='Quitte':            
        ferme_fenetre()
        break

    mise_a_jour()

#..........................PLACEMENT DES BATEAUX ORDI.........................#
c=0 #compteur bateaux ordi
while True :
    if c==len(taille): #vérifie si tous les bateaux sont placés
        break
    else:
        t=taille[c] #taille du bateau à placer
    
    orientation=randint(1,2) #(1:bateau horizontale(clic gauche), 2:bateau vertical(clic droit))
    if orientation==1:
        b=randint(0,9-t) #numéro colonne (j)
        a=randint(0,9)   #numéro ligne (i)
    else:
        b=randint(0,9)
        a=randint(0,9-t)
    
    if chevauchement(lstT,a,b,orientation,t): #vérifie si les cases ont déjà un bateau
        pass
        
    else:
        placement_bateau(lstT,a,b,orientation,t)
        if debug_menu==True: #si l'option "triche" activée
            affichage_bateau(orientation,a,b,x0t,y0,t)
        c+=1 
    
#................................PHASE DE TIRS................................#
cJ=0 #compteur bateau coulé joueur
cO=0 #compteur bateau coulé ordi

tirs_ordi=[] #liste permettant de stocker tous les tirs de l'ordi pour éviter de retirer au même endroit
stratA=[0]
stratB=[0]
cS=0

while True :
    ev = donne_ev()
    tev=type_ev(ev)
    
    if tev=='ClicGauche':          
        x=abscisse(ev)  #coordonnées du clic de tirs
        y=ordonnee(ev)
        
        #récupére le numéro de la case correspondante
        j=(x-x0t)//h     #numéro colonne case
        i=(y-y0)//h      #numéro ligne case
        
               
        if zone_tirs(x,y): #vérfie si le tir est effectué dans la zone
            affichage_mots('Impossible de tirer ici !',13*h+30,10*h+55,15,0.5,'tir_impossible') 
        
        else:
            n=lstT[i][j]    #valeur du clic dans la liste 
            
            if n==0: #si la case est vide => MANQUE
                affichage_tirs(lstT,i,j,x0t,y0,'navy')
                affichage_mots('Manqué',14*h+40,10*h+55,15,0.5,'manqué')
                
                if option_en_vue==True: #si option fonction "en_vue" activée
                    if en_vue(lstT,i,j):
                        affichage_mots('En vue',14*h+40,4*h+55,25,0.5,'en_vue')
    
            elif n==1: #si case déjà tirée
                print('Déjà tiré')
                
            else: #si la case est un bateau
                affichage_tirs(lstT,i,j,x0t,y0,'lightcoral') #affiche le tir correspondant
                if not(vérif_bateau_coulé(lstT,n)): #si le bateau est coulé
                    affichage_mots('Bateau coulé',14*h+30,10*h+55,15,0.5,'bateau_coulé')
                    cJ+=1 #compteur bateau coulé +1
                else :
                    affichage_mots('Touché',14*h+40,10*h+55,15,0.5,'touché')
            
            if cJ==len(taille) : #vérifié si tous les bateaux de l'ordi ont été coulés
                affichage_mots('Vous avez gagné !',6*h+40,12*h+55,30,1,'joueur')
                break
        
        #moment tir ordi :
        nouvtir=False
        while not(nouvtir):
            if cS!=0 :
                a,b=tirs_stratégiques(a,b,stratA,stratB,cS,tirs_ordi)
            else :
                a=randint(0,9) #coordonnées du tir aléatoire de l'ordi
                b=randint(0,9)
            
            if (a,b) in tirs_ordi: #si le tir de l'ordi a déjà été effectué
                nouvtir=False
            else:
                nouvtir=True

        n=lstB[a][b]    #valeur du tir dans la liste 
    
        if n==0: #si la case est vide => MANQUE
            affichage_tirs(lstB,a,b,x0b,y0,'navy')
        
        else: #si le tir touche un bateau
            affichage_tirs(lstB,a,b,x0b,y0,'lightcoral')
            if not(vérif_bateau_coulé(lstB,n)): #vérifie si le bateau est coulé
                cO+=1
                cS=0
                stratA=[0]
                stratB=[0]
            else:
                stratA.append(a)
                stratB.append(b)
                cS+=1
        
        if cO==len(taille) : #vérifie si tous les bateaux du joueur ont été coulé
            affichage_mots("L'ordinateur a gagné !",6*h+40,12*h+55,30,1,'ordi')
            break
        
        tirs_ordi.append((a,b)) #ajoute dans la liste le tir de l'ordi effectué
        print(cS)
        
    if tev=='Quitte':            
            break
    
    mise_a_jour()
ferme_fenetre() 

