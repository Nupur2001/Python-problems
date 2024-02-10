'''
Instructions
You are going to write a program that calculates the highest score from a
List of scores.
eg. student_scores = 178, 65, 89, 86, 55, 91, 64, 891
Important you are not allowed to use the max or min functions. The output words must match the example. Let the highest score in the class is x
Example input
78 65 85 86 55 91 64 89
In this case, student_acores would be a list that looks like: [78, 65,
83,86.55,91, 64, 891
Example Output
The highest score in the class is 91


Note: I've also added lowest score as well
'''

n=int(input())
student_scores=[]

def max_score():
    highest_score=student_scores[0]

    for score in student_scores:
        if score>highest_score:
            highest_score=score
    return highest_score



def min_score():
    lowest_score=student_scores[0]
    for score in student_scores:
        if score<lowest_score:
            lowest_score=score
    return lowest_score
    
if __name__=="__main__":
    max_result = max_score()
    print(f"The highest score in the class is {max_result}")

    min_result = min_score()
    print(f"The lowest score in the class is {min_result}")




