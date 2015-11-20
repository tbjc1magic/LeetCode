class Solution(object):
    def longestSubstring(self, s):

        if len(s) ==0 or len(s) ==1:
            return len(s)

        results = {"firstIdx":0, "secondIdx":0}

        fIdx = results["firstIdx"]
        sIdx = 0

        while 1:
            for sIdx in range(fIdx,len(s)):
                if s[sIdx] in s[fIdx:sIdx]:
                    if results["secondIdx"]-results["firstIdx"]< sIdx-fIdx:
                        results["firstIdx"] = fIdx
                        results["secondIdx"] = sIdx
                        print results,fIdx

                    print s[fIdx:sIdx]
                    fIdx = s[fIdx:sIdx].find(s[sIdx])+1+fIdx
                    break

            if sIdx == len(s)-1:
                if results["secondIdx"]-results["firstIdx"]< sIdx-fIdx+1:
                    results["firstIdx"] = fIdx
                    results["secondIdx"] = sIdx+1
                break

        print results
        return -results["firstIdx"]+results["secondIdx"]
