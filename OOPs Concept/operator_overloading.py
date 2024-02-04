
class Student:
    def __init__(self,x,y):
        self.x = x
        self.y = y

# Example 1
    def __add__(self,other):
        ans1=self.x+other.x
        ans2=self.y+other.y
        return '{} {}'.format(ans1,ans2)

# Example 2
    def __lt__(self,other):
        ans1=self.x+self.y
        ans2=other.x+other.y
        if(ans1<ans2):
            return True
        else:
            return False


# S1=Student(10,20)
# S2=Student(30,40)
# S3=S1+S2
# # S3=Student.__add__(S1,S2)
# print(S3)


S1=Student(10,20)
S2=Student(30,40)
if(S1<S2):
    print("S1 is smaller")
else:
    print("S2 is smaller")







