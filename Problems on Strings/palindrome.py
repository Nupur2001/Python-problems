string=input()
reverse_string=string[::-1]
if reverse_string==string:
    print(f"{string} is a plaindrome")
else:
    print(f"{string} is not a plaindrome")