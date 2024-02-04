class Car:
    def __init__(self,color,seater,company):
        self.color=color
        self.seater=seater
        self.company=company
    
    def movement(self):
        print("Car moves back and fourth")
        
        
class Harrier(Car):
    def race_mode(self):
        print("Race mode is on")
        
    def __init__(self,mileage,color,seater,company):
        self.mileage=mileage
        super().__init__(color,seater,company)
       

class Hyundai:
    def __init__(self):
        self.brandname="Hyundai"
    
        
class Verna(Car,Hyundai):
    def __init__(self,color,seater,company):
        Car.__init__(self,color,seater,company)
        Hyundai.__init__(self)
    # pass

class Pal_V(Car):
    def movement(self):
        print("Car moves back and fourth,up and down")
    # pass
        
h1=Harrier(15,"White",5,"Tata")
v1=Verna("Black",5,"Hyundai")
p1=Pal_V("Blue",2,"Personal Air and Land Vehicle")
print(h1.color)
print(h1.seater) 
print(h1.company) 
print(h1.mileage) 
print("-----------------------------")
print(v1.color)
print(v1.seater)
print(v1.company) 
# print(v1.mileage) 
print("-----------------------------")
print(p1.color)
print(p1.seater)
print(p1.company) 
print(p1.movement())
print("-----------------------------")
# Multiple Inheritance
print(v1.brandname)
print(v1.company)
# print(v1.)