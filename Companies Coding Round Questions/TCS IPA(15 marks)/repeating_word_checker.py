# TCS IPA 15 MARKS QUESTION ON 25 FEB 2023.
# COUNT NUMBER OF TIME A GIVEN WORD REPEATED IN THE USER INPUT STRINGS
# INPUT
# HELLO ANMOL
# Hello friend
# good morning
# hello
# OUTPUT
# COUNT OF GIVEN WORD: 2
# note-> ALL SEARCH ARE CASE INSENSITIVE
# IF NO SEARCH FOUND PRINT 'NOT FOUND'

word=str(input().lower())
freq_word=1
while True:
    input_str=input()
    if not input_str:
        break

    input_str_lower=input_str.lower()

    freq_word += input_str_lower.split().count(word)

if freq_word>1:
    print("COUNT OF GIVEN WORD:",freq_word)
else:
    print('NOT FOUND')
    


    

