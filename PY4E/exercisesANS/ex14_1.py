class PartyAnimal:
    x=0
    def __init__(self):                 # constructor: code that runs when an object is created
        print("I am constructed")
    
    def party(self):
        self.x+=1
        print("So far",self.x)
    
    def __del__(self):
        print("I am destructed", self.x)# destructor

an=PartyAnimal() # 建立實體物件
an.party()
an.party()
an=42 # (覆蓋or結束程式)摧毀實體物件
print("=============")
print("an now is",an)

