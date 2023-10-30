# Sorted approach
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
