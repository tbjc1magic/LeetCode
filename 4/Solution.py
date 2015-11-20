import numpy
class Solution(object):

    def findMedianSortedArrays(self,nums1, nums2):
        nums = []

        idx1 = 0
        idx2 = 0

        while 1:

            if idx1 >= len(nums1):
                nums+=nums2[idx2:]
                break

            if idx2 >= len(nums2):
                nums+=nums1[idx1:]
                break

            try:
                if nums1[idx1] > nums2[idx2]:
                    nums.append(nums2[idx2])
                    idx2+=1
                else:
                    nums.append(nums1[idx1])
                    idx1+=1
            except:
                print idx1,idx2
        print nums1, nums2
        print nums

        mm = None

        if len(nums)%2 ==1:
            idx = (len(nums)+1)/2-1
            mm = nums[idx]
        else:
            idx1 = len(nums)/2
            idx2 = idx1-1
            mm=(nums[idx1]+nums[idx2])/2.0

        return mm
