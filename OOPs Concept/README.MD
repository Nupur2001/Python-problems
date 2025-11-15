# 🐍 Object-Oriented Programming (OOPs) Concepts in Python

## 📘 Introduction
**Object-Oriented Programming (OOP)** is a programming paradigm based on the concept of **objects**.  
Each object represents a real-world entity and contains both **data (attributes)** and **behavior (methods)**.  

Python is a **multi-paradigm** language — it supports both **procedural** and **object-oriented** styles.

---

## ⚙️ Four Pillars of OOP in Python

### 1️⃣ Encapsulation
Encapsulation means **binding data and methods** that operate on that data into a single unit (class).  
It restricts direct access to variables and methods, protecting data from unauthorized modification.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand        # public attribute
        self.__model = model      # private attribute (name mangling)

    def show_details(self):
        print(f"Brand: {self.brand}, Model: {self.__model}")

my_car = Car("Tesla", "Model S")
my_car.show_details()

# Accessing private variable (not recommended)
print(my_car._Car__model)
```

**🧠 Key Point:**  
Attributes starting with `__` (double underscore) become **private** and are not directly accessible.

---

### 2️⃣ Inheritance
Inheritance allows a class (child/subclass) to **inherit attributes and methods** from another class (parent/base class).  
It promotes **code reusability**.

```python
class Animal:
    def speak(self):
        print("This animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

dog = Dog()
dog.speak()  # Output: Woof! Woof!
```

**🧩 Types of Inheritance:**
- Single Inheritance  
- Multiple Inheritance  
- Multilevel Inheritance  
- Hierarchical Inheritance  
- Hybrid Inheritance  

---

### 3️⃣ Polymorphism
Polymorphism means **one function, many forms** — the same method behaves differently for different classes.

```python
class Cat:
    def sound(self):
        return "Meow"

class Cow:
    def sound(self):
        return "Moo"

# Polymorphism example
for animal in [Cat(), Cow()]:
    print(animal.sound())
```

**Output:**
```
Meow
Moo
```

**🧠 Key Point:**  
Polymorphism enhances flexibility — we can use objects of different types through a common interface.

---

### 4️⃣ Abstraction
Abstraction hides **complex implementation details** and shows only the **essential features**.  
In Python, abstraction is achieved using the `abc` (Abstract Base Class) module.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(circle.area())
```

**🧠 Key Point:**  
Abstract classes cannot be instantiated.  
They are used as blueprints for other classes.

---

## 🧱 Class and Object in Python

A **class** is a blueprint for creating objects.  
An **object** is an instance of a class.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# Creating an object
person1 = Person("Alice", 25)
person1.introduce()
```

---

## 🧩 OOPs Concepts Summary

| Concept | Description | Example |
|----------|--------------|---------|
| **Class** | Blueprint for creating objects | `class Car:` |
| **Object** | Instance of a class | `my_car = Car()` |
| **Encapsulation** | Hides internal details | Private variables |
| **Inheritance** | Reuse code from parent class | `class Dog(Animal)` |
| **Polymorphism** | One interface, many forms | Same `sound()` method in multiple classes |
| **Abstraction** | Hides complex logic | Abstract base class |

---

## 🕒 Advantages of OOP
✅ Code reusability  
✅ Data security  
✅ Modularity  
✅ Scalability  
✅ Easier debugging and maintenance  

---

## 🚗 Real-Life Analogy
Think of a **Car** as a class:  
- **Attributes:** color, brand, model, speed  
- **Methods:** start(), stop(), accelerate()  

Each **car you own** (Tesla, BMW, Maruti) is an **object** created from the same **Car class** blueprint.

---

## 🧠 Key Takeaway
OOP in Python allows developers to **model real-world problems** more effectively,  
making code **organized, modular, and easier to maintain**.

---

