'''
TCS IPA 15 MARK QUESTION
Create a function count_words () which takes a string as input and creates a dictionary
with a word in the string as a key and its value as the number of times the
word is repeated in the string. It should return the dictionary.
eg: "hello hi hello world hello"
    dict={'hello':3,'hi': 1, 'word':1}
Sample input:
"hello hi hello world hello"
Sample output:
'hello' I
'''  
import string
from collections  import Counter
def count_words(s):
    s=s.lower()
    s=s.translate(str.maketrans("","",string.punctuation))
    words=s.split()
    word_count=Counter(words)
    print(dict(word_count))

input_string=str(input())
count_words(input_string)
