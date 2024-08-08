'''Given three numbers a, b and m. The task is to find (a^b)%m.
Note: a is given as a String because it can be very big.'''

class Solution:
    def powerMod(self, a, b, m):
        result=1
        a=int(a)%m
        if b==0:
            return 1%m
        while b>0:
            if b%2==1:
                result=(result*int(a))%m
            b=b//2
            a=int(a)*int(a)%m
        return result
#Problem 2
'''Given two positive integers a and b, find GCD of a and b.'''
#Solution
class Solution:
    def gcd(self,a,b):
        if a==0:
            return b
        return self.gcd(b%a,a)
