import numpy
import math
class Solution(object):

    def convert(self, s, numRows):

        if numRows == 1:
            return s

        cycle = (numRows-1)*2

        alllist = []
        for i in range(numRows):
            alllist.append([])

        di = 1
        R = 0
        for one in s:
            alllist[R].append(one)
            print R
            if R== numRows-1:
                di = -1

            if R== 0:
                di = 1

            R+=di

        return_list = []

        for onelist in alllist:
            return_list += onelist

        rs = "".join(return_list)

        return rs
