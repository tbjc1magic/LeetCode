import numpy
import math
class Solution(object):

    def reverse(self, x):

        sig = x/math.fabs(x)

        num = int(math.fabs(x))

        r = 0
        while num>0:
            lastD = num%10
            num = num/10
            r = r*10+lastD

        r = int(sig*r)

        return r
