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
