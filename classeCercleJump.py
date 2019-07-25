class cercleJump:
    def __init__(self,x,y):
        self.x=int(x)
        self.y=int(y)
    
    def deplace(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


    def afficher(self):
        return "mon x : " + str(self.x) + " mon y : " + str(self.y)

    def afficher2(self):
        return 0
