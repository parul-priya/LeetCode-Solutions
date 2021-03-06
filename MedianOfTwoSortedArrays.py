class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        
        i = 0
        j = 0
        
        result = []
        while i < len(nums1) and j < len(nums2) :
            if nums1[i] < nums2[j] :
                result.append(nums1[i])
                i += 1
                
            else :
                result.append(nums2[j])
                j += 1
                
            
        while i <len(nums1) :
            result.append(nums1[i])
            i+=1
            
        while j < len(nums2) :
            result.append(nums2[j])
            j+=1
            
        if not len(result) :
            return 
        if len(result) == 1 :
            return result[0]
        
        mid = len(result) / 2
        
        
        if len(result) %2 :
            return result[mid]
        return (result[mid-1] + result[mid])/2.0
