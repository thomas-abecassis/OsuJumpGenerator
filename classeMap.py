from math import *
from classeJumps import *
from classeCercleJump import *
import os
import random

class listePoints:

    def __init__(self):
        self.liste=[]


    def ajoutePoint(self,Point):
        self.liste.append(Point)


    def getCercle(self,index):
        return self.liste[index]


    ###### A FAIRE ######
    def trouverLesJumps(self):
        jumps=Jumps()
        listeJump=[]
        for i in range(len(self.liste)-1):
            if (self.PJ(i)>12):
                listeJump.append(self.liste[i])
            elif (self.PJ(i+1)>12):
                jumps.ajouterUnJump(listeJump)
                listeJump=[]
        i=0
        while(i<len(jumps.liste)):
            if(len(jumps.liste[i])<3):
                del jumps.liste[i]
                i-=1
            i+=1
        self.jumps=jumps


    #PJ = PointsJump
    def PJ(self,index):
        pjAvant=self.calculerPjAvant(index)
        pjApres=self.calculerPjApres(index)

        if(pjApres>pjAvant):
            return pjApres
        return pjAvant
    
    def afficher(self):
        for i in range(len(self.liste)):
            print(self.liste[i].afficher())

    def calculerPjApres(self,index):
        if(index>=len(self.liste)):
            distanceXapres=(self.liste[index+1].x-self.liste[index].x) 
            distanceYapres=(self.liste[index+1].y-self.liste[index].y)
            return (pythagore(distanceXapres,distanceYapres))/(self.liste[index+1].temps-self.liste[index].temps)*10000
        return 0
    
    def calculerPjAvant(self,index):
            if(index!=0):
                distanceXavant=(self.liste[index].x-self.liste[index-1].x)
                distanceYavant=(self.liste[index].y-self.liste[index-1].y)
                if (pythagore(distanceXavant,distanceYavant) <11):
                    return 0
                return (pythagore(distanceXavant,distanceYavant))/(self.liste[index].temps-self.liste[index-1].temps)*10000
            return 0

    def ecritureDesCercles(self,fichier):
        for cercle in self.liste:
            fichier.write(cercle.ligne)

    def chargerJump(self,jumpDonne):
        ########## choisir le meilleur jump possible ###############
        random.seed()
        rand=str(random.randint(3,9))
        os.chdir("D:/testpython12/jumps")
        fichier=open(rand+".osu","r")
        jump=Jumps()
        jump.chargerJump(fichier)
        return jump
        
        

    def changerLesJumps(self):
        ######### a faire ##############################################
        jump=Jumps()
        for jumpTemp in self.jumps.liste:
            jump=self.chargerJump(jumpTemp)
            for i in range (len(jumpTemp)) :
                jumpTemp[i].x=jump.liste[i%(len(jump.liste))].x
                jumpTemp[i].y=jump.liste[i%(len(jump.liste))].y

    def majLigneMap(self):
        for jump in self.jumps.liste:
            for cercle in jump:
                cercle.majLigne()
                
                
        
            
        
def pythagore(x,y):
    return sqrt(x**2+y**2)
     
