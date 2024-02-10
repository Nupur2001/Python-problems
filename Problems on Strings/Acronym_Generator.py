# import string

# def AcronymGenrator(phrase):
#     words=phrase.split()
#     acronym=''.join(word[0].upper() for word in words)
#     return acronym
# input_phrase=input("Enter a phrase: ")
# print(AcronymGenrator(input_phrase))


import string

punctuation_chars = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

original_string = input("Enter a string: ")

# Create a translation table to remove punctuation
translator = str.maketrans('', '', string.punctuation)

# Translate the string to remove punctuation
string_without_punctuation = original_string.translate(translator)

print(string_without_punctuation)  # Output: This is a string with punctuation Let's remove it


# def AcronymGenrator(phrase):
#     words=phrase.split()
#     punctuation_chars = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
#     if punctuation_chars in words:
#         new_word=words.replace(punctuation_chars,"")
#     acronym=''.join(new_word[0].upper() for new_word in words)
#     return acronym
# input_phrase=input("Enter a phrase: ")
# print(AcronymGenrator(input_phrase))




