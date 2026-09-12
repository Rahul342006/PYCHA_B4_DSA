#Given a binary array nums, return the maximum number of consecutive 1's in the array.
#Example 1:
#Input: nums = [1,1,0,1,1,1]
#Output: 3
#Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

#Example 2:
#Input: nums = [1,0,1,1,0,1]
#Output: 2

class solution:
    def findMaxConsecutiveOnes(self,nums:list[int])->int:
        count=0
        maximum=0
        for i in nums:
            if i==1:
                count+=1
                maximum=max(maximum,count)
            else:
                count=0
        return maximum
nums=[]
n=int(input("Enter number of entries:"))
for i in range(n):
    num=int(input("Enter numbers:"))
    nums.append(num)
obj=solution()
answer=obj.findMaxConsecutiveOnes(nums)
print(answer)
    
