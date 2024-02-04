def swap(a,b):
    temp=a
    a=b
    b=temp
    # a,b=b,a
    print(a,b)
def main():
    for i in range(3):
        a,b=map(int,input("Enter number: ").split())
        swap(a,b)
if __name__ == '__main__':
    main()