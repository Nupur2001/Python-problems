# PREPBYTES STRING SLICING MCQ QUESTIONS
# Question1
str="hello"
print(str[:2])

# Question2
str="I study at prepbytes"
print(str.isalnum())


# Question3
strOne = str("prepBytes")
strTwo = "prepBytes"
print(strOne == strTwo)
print(strOne is strTwo)

# Question4
myString = "prepbytes"
stringList = ["abc", "prepbytes", "xyz"]
print(stringList[1] == myString)
print(stringList[1] is myString)

# Question5
str1 = 'Welcome'
print (str1[:6] + ' PrepBytes')

# Question6
str1="6/4"
print("str1")


# Question7
# Which of the following will produce an error
str1="python"

# Option 1
print(str1[2])   
# Option 2
str1[1] = "x"
# Option 3
print(str1[1:9])


# Question8
str1 = 'PrepBytes'
print(str1[0:4])


# Question9
str1 = 'Welcome'
print(str1*2)

# Question10
class Count:
        def __init__(self, count = 0):
           self.__count = count
c1 = Count(2)
c2 = Count(2)
print(id(c1) == id(c2), end = " ")
s1 = "Good"
s2 = "Good"
print(id(s1) == id(s2))

# Question11
print("Hello {name1} and {name2}".format(name1='foo', name2='bin'))