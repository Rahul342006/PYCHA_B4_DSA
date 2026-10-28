#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#Given a string s, return true if it is a palindrome, or false otherwise.
#Example 1:
#Input: s = "A man, a plan, a canal: Panama"
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.

#Example 2:
#Input: s = "race a car"
#Output: false
#Explanation: "raceacar" is not a palindrome.

class solution():
    def validPalindrome(self,s:str)->bool:
        s=s.lower()
        left=0
        right=len(s)-1
        while(left<right):
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
s=input("Enter a string:")
obj=solution()
answer=obj.validPalindrome(s)
print(answer)
        
