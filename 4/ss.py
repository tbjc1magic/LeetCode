# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        len1= len(l1)
        len2= len(l2)

        longer = None
        shorter = None

        if len1>= len2:
            l = l1
            s = l2
        else:
            l = l2
            s = l1

        extra = 0
        results = []
        for i in range(max([len1,len2])):

            ####within the lenght of the shorter#####
            try:
                tmp = l[i] + s[i] +extra

            #####outside the length of the shorter###
            except:
                tmp = l[i] +extra

            if tmp>9:
                tmp = tmp-10
                extra = 1
            else:
                extra = 0

            results.append(tmp)

        if extra >0:
            results.append(1)

        return results
