# Iterative approach
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr1 = collections.defaultdict(int)
        arr2 = collections.defaultdict(int)
        for num in nums1:
            arr1[num] += 1
        for num in nums2:
            arr2[num] += 1
        res = []
        for item in arr1:
            if item in arr2:
                frequency = min(arr1[item], arr2[item])
                res.extend([item] * frequency)
        return res

'''# Sorted approach
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            else:
                small_num = nums1[i] if nums1[i] < nums2[j] else nums2[j]
                if res and nums1[i] == res[-1] and nums2[j] != res[-1]:
                    i += 1
                elif res and nums1[i] != res[-1] and nums2[j] == res[-1]:
                    j += 1
                else:
                    if nums1[i] < nums2[j]:
                        i += 1
                    else:
                        j += 1
        return res
'''
