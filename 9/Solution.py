import numpy
import math
class Solution(object):

    def isPalindrome(self,x):

        if x<0:
            return False

        numlist = []
        num = x
        while num>0:
            digit = num%10
            numlist.append(digit)
            num = int(num/10)

        for i in range(int( math.ceil(len(numlist)/2.0))):
            a = numlist[i]
            b = numlist[-1-i]

            if a != b:
                return 0

        return 1
