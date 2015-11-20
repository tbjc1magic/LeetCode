import numpy
class Solution(object):
    def longestPalindrome1(self, s):

        print s
        results = {"firstIdx":0,"secondIdx":0}

        for idx1 in range(len(s)):

            for idx2 in range(idx1+1,len(s)+1):
                tmpstr = s[idx1:idx2]

                l=len(tmpstr)
                for i in range(len(tmpstr)/2):
                    if tmpstr[i] != tmpstr[len(tmpstr)-i-1]:
                        l=0

                if l >results["secondIdx"] - results["firstIdx"]:
                    results["secondIdx"] = idx2
                    results["firstIdx"]  = idx1

                print tmpstr,l

        return s[results["firstIdx"]:results["secondIdx"]]

    def PalindromeLengthOdd(self,s,idx):
        one1 = idx-1
        one2 = idx+1

        while 1:
            if one1 < 0 or one2 > len(s)-1:
                return one2 - one1-1

            if s[one1] != s[one2]:
                return one2 - one1- 1

            one1 -= 1
            one2 += 1
        return 0

    def PalindromeLengthEven(self,s,idx):
        one1 = int(idx)
        one2 = int(idx)+1
        while 1:
            if one1 < 0 or one2 > len(s)-1:
                return one2 - one1-1

            if s[one1] != s[one2]:
                print "here", one1, one2
                print s[one1],s[one2]
                return one2 - one1- 1

            one1 -= 1
            one2 += 1

    def longestPalindrome(self, s):

        print s

        if len(s) <2:
            return s

        ii1 = 0
        ii2 = 0

        repetitive = 0

        for idx1 in range(len(s)):

            ###### check for repetitive ########

            if repetitive !=0:
                for i in range(idx1,len(s)):
                    if s[idx1] == s[i] and i-idx1 >=3:
                       repetitive = i - idx1 +1

                    if repetitive  > ii2 - ii1:
                        ii1 = i
                        ii2 = i+repetitive

            if repetitive:
                repetitive -= 1
                continue

            if idx1 <len(s)-1 and s[idx1] == s[idx1+1]:
                tmp = self.PalindromeLengthEven(s, (idx1*2+1)/2.0)
                print tmp
                if tmp > ii2 - ii1:
                    ii1 = idx1 - tmp/2 + 1
                    ii2 = idx1 + tmp/2 + 1

            if idx1 <len(s)-2 and s[idx1] == s[idx1+2]:
                tmp = self.PalindromeLengthOdd(s, idx1+1)

                if tmp > ii2 - ii1:
                    ii1 = idx1 - (tmp-1)/2 + 1
                    ii2 = idx1 + (tmp-1)/2 + 2

        return s[ii1:ii2]
