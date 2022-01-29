
class Translate:
    def __init__(self) -> None:
        pass

    def translateXYZ(self,x,y,z):
        self.x += x
        self.y += y
        self.z += z
        return self.x,self.y,self.z
    
    def translateX(self,x):
        x += x
        return x
    
    def translateY(self,y):
        y += y
        return y

    def translateZ(self,z):
        z += z
        return z