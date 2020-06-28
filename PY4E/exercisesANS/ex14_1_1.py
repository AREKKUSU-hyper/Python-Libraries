# Object Inheritance: extend a classto make a new class

class PartyAnimal:
    x=0
    name=""
    def __init__(self,nam):                  
        self.name=nam
        print(self.name, "constructed")
    
    def party(self):
        self.x+=1
        print(self.name,"count",self.x)
    
class FootballFan(PartyAnimal): # 包含PartyAnimal的所有屬性及方法
    point=0
    def touchdown(self):
        self.point=self.point+7
        self.party()
        print(self.name,"points",self.point)

s=FootballFan("sam") 
s.party()
print("------------------------------")
s.touchdown()
