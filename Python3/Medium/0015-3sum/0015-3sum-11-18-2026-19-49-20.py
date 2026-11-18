class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        n = len(nums)
        

        for i in range(n-2):
            
            if nums[i]>0:
                break

            if i>0 and nums[i] == nums[i-1]:
                continue

            left,right = i+1,n-1

            while left<right:
                ts = nums[i]+nums[left]+nums[right]

                if ts>0:
                    right-=1
                elif ts<0:
                    left+=1

                else:
                    result.append([nums[i],nums[left],nums[right]])

                    left+=1
                    right-=1

                    while left<right and nums[left] == nums[left-1]:
                        left+=1
                    while left<right and nums[right] == nums[right+1]:
                        right-=1

        
        return result