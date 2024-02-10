def list_comprehension(n):
    return [num for num in range(1,n+1) if num%2==0]

n_input=int(input("Enter a number: "))
result=list_comprehension(n_input)
print(result)

