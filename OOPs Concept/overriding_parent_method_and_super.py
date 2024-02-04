class Car:
    def __init__(self,color,seater,company):
        self.color=color
        self.seater=seater
        self.company=company
        
    def speedup():
        print("Speed increasing")
        
    def speeddown():
        print("Speed decreasing")
    
    def movement(Self):
        print("Car is moving back and fourth")
class Harrier(Car):
    # Super->used to give access to methods and properties of a parent or sibling class
    def __init__(self,mileage,color,seater,company):
        self.mileage=mileage
        super().__init__(color,seater,company)
    # pass
    def race_mode(self):
        print("Race mode is on")


class Verna(Car):
    pass

class Pal_V(Car):
    # Overriding parent method
    pass
    # def movement(self):
    #     print("Car is moving back and fourth,up and down")

c1=Car("Black",5,"Tata")
h1=Harrier(15,"White",5,"Tata")
v1=Verna("Blue",5,"Tata")
p1=Pal_V("Black",2,"Personal Air and Land Vehicle")
print("Harrier")
print(h1.color)
print(h1.seater)
print(h1.company)
print("---------------")
print("Verna")
print(v1.color)
print(v1.seater)
print(v1.company)
print("---------------")
print("Pal_V")
print(p1.color)
print(p1.seater)
print(p1.company)
print(p1.movement())
