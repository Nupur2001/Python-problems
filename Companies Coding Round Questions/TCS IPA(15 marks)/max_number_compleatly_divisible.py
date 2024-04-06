# TCS 10th FEB 2023 15 marks IPA QUESTION
# Input
# 4 #number of value need to store
# 5
# 5
# 10
# 15
# 5  # divisor
# output
# MAXIMUM NUMBER COMPLETELY DIVISIBLE :15
# note:
# if there is no max number completely divisibe by given input
# print "No number found



n=int(input())
list1=list(map(int,input().split()))
divisor=int(input())
mi=max(list1)
if mi%divisor==0:
    print("MAXIMUM NUMBER COMPLETELY DIVISIBLE :",mi)
else:
    print("No number found")


