class Car:
    def __init__(self,color,seater,company):
        self.color=color
        self.seater=seater
        self.company=company

class Harrier(Car):
    def race_mode(self):
        print("Race mode is on")

class Verna(Car):
    pass

c1=Car("Black",5,"Tata")
h1=Harrier("White",5,"Tata")
v1=Verna("Blue",5,"Tata")
print(h1.color)
print(h1.seater)
print(h1.company)
print("---------------")
print(v1.color)
print(v1.seater)
print(v1.company)
print("---------------")
print(c1.color)
print(c1.seater)
print(c1.company)