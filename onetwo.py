import os
import time
from classeCercle import *
from interfaceGraphique import *
from classeMap import *
from creationFichier import *

###MAUVAISE ECRITURE###

def main():
    os.chdir("maps")
    fichier=open("test2.osu","r")
    lire=fichier.read()
    # exemple tout simple :
    fichier2=open("ecriture2.osu","w")
    fichier2.write(toutAvantHitObects(lire,positionHitObjects(lire)))
    cercles=HitObjects(lire,positionHitObjects(lire))
    map=separerCercles(cercles)
    map.trouverLesJumps()
    map.changerLesJumps()
    map.majLigneMap()
    map.ecritureDesCercles(fichier2)
    fichier2.close()
    game(map)
           
            
def positionHitObjects(lire):
    longueurLire=len(lire)
    i=1
    while i<longueurLire and lire[0+i:12+i]!="[HitObjects]":
        i+=1
    return i+13



def HitObjects(lire,rang):
    return lire[rang:len(lire)]

def toutAvantHitObects(lire,rang):
    return lire[0:rang]


def separerCercles(cercles):
    map=listePoints()
    for i in range(len(cercles)-17):
        if cercles[0+i:1+i]=="\n":
            map.ajoutePoint(trouverCoord(cercles[1+i:16+i],ligne(cercles[1+i:100+i])))
    return map


def ligne(ligneD):
    ligne=""
    char=""
    i=0
    while char!="\n" and i<100:
        char=ligneD[i]     
        ligne+=char
        i+=1
    return ligne
            
def trouverCoord(cercle,ligne):
    x=""
    y=""
    temps=""
    i=0
    while cercle[i]!=",":
        x+=cercle[i]
        i+=1
    i+=1
    while cercle[i]!=",":
        y+=cercle[i]
        i+=1
    i+=1
    while cercle[i]!=",":
        temps+=cercle[i]
        i+=1  

    return Point(x,y,temps,ligne)

    
main()
    
    


