#Problem1

'''
Sia bought car insurance. The policy of the insurance is:



    The maximum rebatable amount for any damage is Rs X lakhs.

    If the amount required for repairing the damage is ≤ X lakhs, that amount is rebated in full.



Sia's car meets an accident and required Rs Y lakhs for repairing. Determine the amount that will be rebated by the insurance company.
Input
The first line of input will contain a single integer T, denoting the number of test cases.
The first and only line of each test case contains two space-separated integers X and Y.

Constraints
1 ≤ T ≤ 1000
1 ≤ X, Y ≤ 30
'''
#Solution
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if x>y:
        print(y)
    else:
        print(x)

#Problem2

'''
Neha has a square-shaped chart paper with the side length equal to N. She wants to cut out K x K squares from this chart paper. Find the maximum number of K x K squares she can cut from the entire chart paper.
Note that, some part of the chart paper might not be a included in any K x K cutout square.
'''
#Solution
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    print((n//k)**2)

#Problem 3
'''
Your teacher gave you an assignment - given an integer N, construct a binary string B = b1​b2​b3​…bN​ of length N such that: max(bi​, bi+1​) = 1 for every i from 1 to N - 1.
What is the minimum number of 1's such a binary string can contain?
Note: A binary string is a string consisting of only the digits 0 and 1.
'''
#Solution
t=int(input())
for _ in range(t):
    n=int(input())
    print(n//2)
#Problem 4
'''
In Zomaland, denominations less than rupees 10 have stopped and now rupees 10 is the smallest denomination.
Suppose Zoma goes to buy some item with cost not a multiple of 10, then, he will be charged the cost that is the nearest multiple of 10.
If the cost is equally distant from two nearest multiples of 10, then the cost is rounded up.
For example, 35, 38, 40, 44 are all rounded to 40.
Zoma purchased an item having cost X (X ≤ 100) and gave a bill of rupees 100. How much amount will he get back?'''

#Solution
t = int(input())
for _ in range(t):
    x= int(input())
    if int(str(x)[-1])<5:
        cs=10*(x//10)
    else:
        cs=(10*(x//10))+10
    print(100-cs)

#Problem 4
'''
Chef's bank gives him a unique offer - at the end of each year, they offer Chef to either add 1000 rupees to his bank account, or double the amount stored in his bank account. Chef initially has X rupees in his account. What is the maximum amount of money that Chef can accumulate after Y years?'''

#Solution
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    max_amount=0
    while y:
        ax=x+1000
        mx=x*2
        x=max(ax,mx)
        y-=1
    print(x)
#Problem 5
'''
Gaurav is currently standing at stair 0 and he wants to reach stair numbered X.
Gaurav can climb either Y steps or 1 step in one move.
Find the minimum number of moves required by him to reach exactly the stair numbered X.'''
#solution
t= int(input())
for _ in range(t):
    x,y = map(int,input().split())
    c=0
    while True:
        if x/y==int(x/y):
            c+=x//y
            break
        else:
            x-=1
            c+=1
    print(c)
