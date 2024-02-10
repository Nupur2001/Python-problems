# Without using random module
def names():
    t=int(input("Enter number of test cases:\n"))
    while t>0:
        alphabet=input("Enter an alphabet:\n").lower()
        name=input("Enter your name:\n").lower()
        # for i in name:
        if name[0]==alphabet:
            print("Your name starts with the given alphabet.")
        else:
            print("Your name does not start with the given alphabet.")
        t=t-1

names()


# Using random module
import random
import string
def generate_random_alphabets():
    return random.choice(string.ascii_lowercase)
def names():
    t=int(input("Enter number of test cases:\n"))
    while t>0:
        alphabet=generate_random_alphabets()
        print(alphabet)
        name=input("Enter your name:\n").lower()
        if name[0]==alphabet:
            print(f'{name[0]} matches with {alphabet}')
        else:
            print(f"{name[0]} doesn't match with {alphabet}")
        t=t-1

generate_random_alphabets()
names()
