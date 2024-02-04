class student:
    def __init__(self, name, gender, rollNo):
        self.name = name
        self.gender = gender
        self.rollNo = rollNo

def main():
    s1=student("Nupur","Female",50)
    print(s1.name)
    print(s1.gender)
    print(s1.rollNo)
    s2=student("Mayank","Male",49)
    print(s2.name)
    print(s2.gender)
    print(s2.rollNo)

if __name__ == '__main__':
    main()