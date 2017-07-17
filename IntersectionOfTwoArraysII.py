class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2) :
            nums1, nums2 = nums2, nums1
        result = []
        for i in nums2 :
            if i in nums1 :
                result.append(i)
                del nums1[nums1.index(i)]
        return result
