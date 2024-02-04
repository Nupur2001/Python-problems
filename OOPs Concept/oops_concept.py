class Mobile:
    def __init__(self, brandname, color, isJack):
        self.brandname = brandname
        self.color = color
        self.isJack = isJack

    def calling(self):
        print("Mobile calling")

    def clicking(self):
        print("Mobile clicking")

def main():
    m1=Mobile("Apple","Black",True)
    print(m1.brandname)
    print(m1.color)
    print(m1.isJack)
    print(m1.clicking())

if __name__ == '__main__':
    main()   

