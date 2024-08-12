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
#Problem 3
'''Given an array of N positive integers, find GCD of all the array elements.'''
#Solution
class Solution:
    def gcd(self, n, arr):
        from functools import reduce
        def gcd_arr(a,b):
            while b:
                a,b=b,a%b
            return a
        return reduce(gcd_arr,arr)

#Problem 4
'''
Given two integers a and b, write a function lcmAndGcd() to compute their LCM and GCD. The function takes two integers a and b as input and returns a list containing their LCM and GCD.'''

#Solution
class Solution:
    def lcmAndGcd(self, A , B):
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b,a%b)
        def lcm(a,b):
            return ((a*b)//gcd(a,b))
        return (lcm(A,B),gcd(A,B))

#Problem 5
'''
For an integer N find the number of trailing zeroes in N!.'''
#Solution
class Solution:
    def trailingZeroes(self, N):
        n=N
        if (n<0):
            return -1
        count =0
        while(n>=5):
            n//=5
            count+=n
        return count

