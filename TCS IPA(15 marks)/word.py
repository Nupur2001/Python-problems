# input
# hello wordaeiou 123
# output
# new word hll wrd 123 and count of number 3

word=input()
new_word=""
count=0
for i in range(len(word)):
    vowels=['a','A','e','E','i','I','o','O','u','U']
    if word[i] not in vowels:
        new_word+=word[i]
    elif word[i].isdigit():
        count+=int(word[i])
print("New Word: ",new_word)
print("Count of numbers: ",count)
