""""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
""""
# My first attemp
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtred_str = ''.join(filter(str.isalnum,str(s)))
        if lower(filtred_str) == lower((filtred_str[::-1])):
            return True
        else:
            return False








""""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
""""

# My first attemp
""""
The first think i thought was that i need a matrix.
list = [1,2,3,4]

    0 1 2 3
   --------
0 | 2 3 4 5
1 | 3 4 5 6
2 | 4 5 6 7
3 | 5 6 7 8

We don't need the first column.

    1 2 3
   -------
0 | 3 4 5
1 | 4 5 6
2 | 5 6 7
3 | 6 7 8

and because index_column should always be greater than index_row, pass calculating more than half of the matrix  

    1 2 3
   -------
0 | 3 4 5
1 |   5 6
2 |     7
3 |

so the indexs i for index_column and j for index_row:

0,1 - 0,2 - 0,3
      1,2 - 1,3
            2,3
so:
num_of_columns = len(list) - 1
num_of_rows = len(list) - 1
and when for-looping, the first index has to increase (i > j):
first_index = 0 -> first_index += 1

Because there should be only one solution, 
insert if statement that if calculated elements are equal to target and return [i+1,j+1] (+1 because of Python superiority)
""""

# the code
import numpy as np

def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    matrix = [[] for _ in range(len(numbers)-1)]
    first_index = 0
    for i in range(first_index,len(numbers)-1):
        for j in range(first_index+1,len(numbers)):
            if numbers[i]+numbers[j] == target:
                return [i+1,j+1]
            else: continue
        first_index += 1


# The quickest
# two-pointer
def twoSum1(self, numbers, target):
    l, r = 0, len(numbers)-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        else:
            r -= 1

# My learning part

















# 15. 3Sum

""""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

 
""""



class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output = []
        n = len(nums)
        
        for i in range(n - 2):
            if nums[i] > 0:
                break
                
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l, r = i + 1, n - 1
            
            while l < r:
                tri_sum = nums[i] + nums[l] + nums[r]
                if tri_sum > 0:
                    r -= 1
                elif tri_sum < 0:
                    l += 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                    
        return output
