    
class Point:
    
    def __init__(self,x,y,temps,ligne):
        self.x=int(x)
        self.y=int(y)
        self.temps=int(temps)*1000
        self.ligne=ligne
    
    def deplace(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def getMicro(self):
        return self.temps
        

    def afficher(self):
        return "mon x : " + str(self.x) + " mon y : " + str(self.y) + "mon temps est " + str(self.temps) + "flood : " + self.ligne

    def afficher2(self):
        return 0
    
    def majLigne(self):
        maj=""
        maj+=str(self.x)+","+str(self.y)+","
        i=0
        nbVirgules=0
        while(nbVirgules!=2):
            if self.ligne[i]==",":
                nbVirgules+=1
            i+=1
        maj+=self.ligne[i:len(self.ligne)]
        self.ligne=maj
        
        
