'''
Coding Question :
Aman, who is working at a software company forgot the password of his LinkedIn Account. But he knows the ASCIl values of his password in reverse order.
Help Aman to find the password.
To decode the password, first reverse the string of digits, then successively pick valid values from the string and convert them to their ASCIl equivalents. Some of the values will have two digits, and others three. Use the ranges of valid values when decoding the string of digits.
Some of the ASCIl values are given with their characters:
• The ASCII value of A to Z is 65 to 90.
• The ASCII value of a to z is 97 to 122.
• The ASCII value of space characters is 32.
Note: The password only has alphabets and blank spaces.
Given a string, decode the password by following the steps mentioned above.
Constraints:
・1<= |sl<=10^5
・s[il is an ascii character in the range [A-Za-z] or a space character
Example :
Sample Input: 796115110113721110141108
Sample Output : Prepinsta
'''
s=input("Enter string: ")
s=s[::-1]
print(s)
i=0
result=""
while (i<len(s)-1):
    x=s[i]+s[i+1]
    if x=="32":
        result=result+" "
    elif int(x) in range(65,90) or int(x) in range(97,122):
        result=result+chr(int(x))
    elif i+2<len(s):
        x=x+s[i+2]
        result=result+chr(int(x))
        i+=1
    i+=2
print(result)