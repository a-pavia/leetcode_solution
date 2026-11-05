class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        p1 = 0
        p2 = len(nums) - 1
        k = len(nums)

        while p1 <= p2:
            if nums[p2] == val:
                p2 -= 1
                k -= 1
            else:
                if nums[p1] == val:
                    nums[p1] = nums[p2]
                    p1 += 1 
                    p2 -= 1
                    k -= 1
                else:
                    p1 += 1

        return k 
        