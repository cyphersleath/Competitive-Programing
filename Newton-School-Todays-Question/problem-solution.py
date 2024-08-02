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
