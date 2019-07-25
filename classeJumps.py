from classeCercleJump import *

class Jumps:

    def __init__(self):
        self.liste=[]

    def chargerJump(self,fichier):
        cercles=fichier.read()
        for i in range(len(cercles)-5):
             if cercles[0+i:1+i]=="\n":
                self.ajouterUnJump(trouverCoord(cercles[1+i:9+i]))            
        
    
    def ajouterUnJump(self,jump):
        self.liste.append(jump)

    def estContenu(self,cercle):
        for i in range(len(self.liste)):
            if(cercle in self.liste[i]):
                return True
        return False
    
def trouverCoord(cercle):
    x=""
    y=""
    i=0
    while cercle[i]!=",":
        x+=cercle[i]
        i+=1
    i+=1
    while cercle[i]!="\n":
        y+=cercle[i]
        i+=1
    return cercleJump(x,y)


