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
Given an 0-indexed array of integers arr[] of size n, find its peak element and return it's index. An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements (if they exist).

Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.'''

#Solution
class Solution:   
    def peakElement(self,arr, n):
        l=sorted(arr)
        return arr.index(l[-1])  
#Problem 6
'''
Given an array arr. Your task is to find the minimum and maximum elements in the array.

Note: Return an array that contains two elements the first one will be a minimum element and the second will be a maximum of an array'''
#Problem 7
class Solution:
    def get_min_max(self, arr):
        max=0
        min = arr[0]
        for i in arr:
            if min >=i:
                min = i
            if max < i:
                max = i
        return min,max
#Problem 8
'''
You are given a string s. You need to reverse the string.'''
#Problem 9
class Solution:
     def reverseWord(self, str: str) -> str:
         return str[::-1]

