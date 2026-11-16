class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l=0
        r=len(nums)-1
        i=(l+r)//2
        while l<=r:
            print(l,r,i)
            if l==r:
                if nums[l]>=target:
                    return l
                else:
                    return l+1
            i=(l+r)//2

            if nums[i]==target:
                return i
            elif nums[i]<target:
                l=i+1
            else:
                r=i
            