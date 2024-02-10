'''
Prepbytes Question
Print Prefix and Suffix
The prefix of a string is any leading contiguous part and Suffix is any trailing contiguous part (See sample test case explanation for better understanding). Given a string S, your task is to first print all the prefixes of S each in a new line, then print all the suffixes of S each in a new line.

Input Format
There is only one input, a string S containing only lowercase English alphabets.

Output
Print the required output as mentioned above.

Constraints
1≤|S|≤103
, where |S| is length of string.

Time Limit
1 second

Example
Input 1
abc

Output 1
a
ab
abc
c
bc
abc

Input 2
prep

Output 2
p
pr
pre
prep
p
ep
rep
prep

Sample test case explanation
Prefixes of string prep are p, pr, pre, prep. All are leading contiguous parts of the given string.
Suffixes of string prep are p, ep, rep, prep. All are trailing contiguous parts of the given string.

'''
def prefix_and_suffix(s):
        for i in range(1,len(s)+1):
        # Will print prefix
            print(s[:i])
        for i in range(1,len(s)+1):
        # Will print suffix
            print(s[-i:])
            # print(s[:-j])

n=input().strip()
prefix_and_suffix(n)
