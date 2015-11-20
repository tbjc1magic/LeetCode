class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        one1 = l1
        one2 = l2

        extra = 0

        results = []

        list1 = []
        list2 = []

        while one1:
            list1.append(one1.val)
            one1 = one1.next

        while one2:
            list2.append(one2.val)
            one2 = one2.next

        len1= len(list1)
        len2= len(list2)

        longer = None
        shorter = None

        if len1>= len2:
            l = list1
            s = list2
        else:
            l = list2
            s = list1

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
