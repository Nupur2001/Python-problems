def pythagorean_triplet(l):
    a,b,c=map(int,input().split())
    l=[a,b,c]
    if len(l)!=3:
        raise ValueError("Value Error")
    for i in l:
        i**2
        if (l[0])**2+(l[1]**2)==l[2]**2:
            return True
        else:
            return False
        
if __name__=="__main__":
    try:
# print(pythagorean_triplet([3,4,5]))
        print(pythagorean_triplet([]))
    except Exception as e:
        print(e)