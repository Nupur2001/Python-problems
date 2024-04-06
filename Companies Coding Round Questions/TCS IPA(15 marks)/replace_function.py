#   HOW TO USE SPLIT() AND REPLACE() FUNCTION IN PYTHON
#   Consider an Input
#   INPUT->Richard is now happyil and satisfiedil with his situationil
#   Take this input to the program and convert the input into following output which is
#   OUTPUT-> Richard is now happy and satisfied with his situation I purpose we have to remove "il" unwanted character from string

line=str(input("Enter a line"))
print("Original String:", line)
r=str(input("Enter the word you want to replace with: "))
p=str(input("Enter the word you want to put in place of it: "))
transformed_line=line.replace(r,p)
print("Transformed String: ",transformed_line)