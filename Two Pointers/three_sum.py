# 15. 3Sum

class Solution:
    # Time: O(n^2), Memory:O(n)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = [] 
        for i in range(len(nums) - 2):
            if i-1 >= 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1 

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return triplets