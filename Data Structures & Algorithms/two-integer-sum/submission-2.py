class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through array, find complement of number against target. (Add to number to hashpmap if number not found, else return indicies)
        hashmap = {}

        for i ,n in enumerate(nums):
            complement = target - n
            if complement in hashmap:
                return ([hashmap[complement], i])
            hashmap[n] = i
    
    # Time Complexity = O(N), iterate through the array
    # Space Complexity = O(N), Hashmap of max size n