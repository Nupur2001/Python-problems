"""
Aditya and Danish
Aditya and Danish are great chess players and they want to know who is the better player. So they play 
N games in a row. For each game, we noted down the winner- Aditya or Danish. There was no tie.
Now they are tired of playing the game and want you to find out who won more games.

Input format
The first line contains an integer 
T, denoting the number of test cases.
For each test case
First-line contains an integer N, denoting the length of the string.
The second line contains a string with 
N characters and each character is either A or D where A means Aditya won and D means Danish won.

Output format
For each test case on a new line,

Print Aditya if Aditya wins more number of games.
Print Danish if Danish wins more number of games.
Print AdiDan is both have equal number of wins.
Constraints
1<=T<=10

1<=N<=10^7

Time limit
1 second

Example
Input
3
6

ADAAAA
7

DDDAADA
6

DADADA

Output
Aditya
Danish
AdiDan
"""

def win(win_A,Win_B):
    if win_A>Win_B:
        return "Aditya"
    elif Win_B>win_A:
        return "Danish"
    else:
        return "AdiDan"
    
def main():
    t=int(input())
    for i in range(t):
        n=int(input())
        result=input().strip()
        win_A=result.count("A")
        win_B=result.count("D")

        winner=win(win_A,win_B)
        print(winner)

if __name__ == "__main__":
    main()