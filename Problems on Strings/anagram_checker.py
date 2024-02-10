
def is_anagram(str1, str2):
    str1_lower = str1.lower()
    str2_lower = str2.lower()

    return sorted(str1_lower) == sorted(str2_lower)

str1_input,str2_input=map(str,input().split())
output = is_anagram(str1_input, str2_input)
print(f'is_anagram("{str1_input}", "{str2_input}") is {output}')


