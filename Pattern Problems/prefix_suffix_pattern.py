def prefix_and_suffix_pattern(p):
    for i in range(1,len(p)+1):
        print(p[:i])
    for i in range(1,len(p)+1):
        print(p[:-i])

n=input().strip()
print("\n")
prefix_and_suffix_pattern(n)