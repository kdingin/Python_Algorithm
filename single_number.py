from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0  
        
        for number in nums:
            result = number ^ result  
        
        return result

if __name__ == "__main__":
    solution = Solution()
    test_nums = [3,5,7,4,3,5,7]
    print(solution.singleNumber(test_nums))  
    '''bit manipulation'''
'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''