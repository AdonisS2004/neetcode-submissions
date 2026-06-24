class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # case 1: list(s) is/are empty
        if not nums1 and not nums2:
            return 0
        if not nums1:
            n2 = len(nums2)
            mid = n2//2
            if n2%2 != 0: return nums2[mid]
            else: return ((nums2[mid] + nums2[mid-1])/2)
        if not nums2:
            n1 = len(nums1)
            mid = n1//2
            if n1%2 != 0: return nums1[mid]
            else: return ((nums1[mid] + nums1[mid-1])/2)

        # prepare variables
        # small is always the smaller one
        small, big = None, None
        nSmall, nBig = 0, 0
        if len(nums1) > len(nums2):
            small, big = nums2, nums1
            nSmall, nBig = len(nums2), len(nums1)
        else:
            small, big = nums1, nums2
            nSmall, nBig = len(nums1), len(nums2)
        
        # case 2: arrays don't interleave
        if small[-1] <= big[0]: # [small][big]
            if nSmall == nBig:
                return ((small[-1] + big[0])/2)
            else:
                l, r = 0, nBig-nSmall
                mid = (l+r)//2
                if (nBig+nSmall)%2 != 0: return big[mid]
                else: return ((big[mid] + big[mid-1])/2)
        if big[-1] <= small[0]: # [big][small]
            if nSmall == nBig:
                return ((big[-1] + small[0])/2)
            else:
                l, r = nSmall, nBig
                mid = (l+r)//2
                if (nBig+nSmall)%2 != 0: return big[mid]
                else: return ((big[mid] + big[mid-1])/2)
        
        # base case: arrays interleave
        half = (nSmall + nBig)//2
        l, r = 0, nSmall-1
        while l <= r:
            mid = (l+r)//2
            bdx = half - mid
            # print(f"l:({l},{small[l]}); b:({r},{small[r]}); Median @ index {mid} = {small[mid]}; Checking ({bdx=}, {big[bdx-1]=})")
            # early return
            if small[mid] >= big[bdx-1] and big[bdx] >= small[mid]:
                if (nSmall+nBig)%2 == 0:
                    if mid != 0:
                        return (small[mid] + max(small[mid-1], big[bdx-1]))/2
                    else: 
                        return (small[mid] + big[bdx-1])/2
                else: 
                    return small[mid]
            # update l or r
            if small[mid] <= big[bdx-1]:
                l = mid + 1
            elif small[mid] >= big[bdx-1]:
                r = mid - 1 

        # regular return
        if (nSmall+nBig)%2 != 0: return (big[half] + big[half+1])/2
        else: return big[half-1]

            