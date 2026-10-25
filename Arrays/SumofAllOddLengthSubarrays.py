#Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
#A subarray is a contiguous subsequence of the array.
#Example 1:
#Input: arr = [1,4,2,5,3]
#Output: 58
#Explanation: The odd-length subarrays of arr and their sums are:
#[1] = 1
#[4] = 4
#[2] = 2
#[5] = 5
#[3] = 3
#[1,4,2] = 7
#[4,2,5] = 11
#[2,5,3] = 10
#[1,4,2,5,3] = 15
#If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

class solution:
    def sumOddLengthSubArrays(self,arr:list[int])->int:
        total=0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                sub=arr[i:j+1]
                if len(sub)%2!=0:
                    total+=sum(sub)
        return total
arr=[]
n=int(input("Enter number of entries:"))
for i in range(n):
    num=int(input("enter numbers:"))
    arr.append(num)
obj=solution()
answer=obj.sumOddLengthSubArrays(arr)
print(answer)
