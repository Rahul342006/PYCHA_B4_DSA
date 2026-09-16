#Given a square matrix mat, return the sum of the matrix diagonals.
#Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
#Example 1:
#Input: mat = [[1,2,3],
              #[4,5,6],
              #[7,8,9]]
#Output: 25
#Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
#Notice that element mat[1][1] = 5 is counted only once.

class solution:
    def diagonalSum(self,mat:list[list[int]])->int:
        n=len(mat)
        total=0
        for i in range(n):
            total+=mat[i][i]
            total+=mat[i][n-1-i]
        if n%2==1:
            total-=mat[n//2][n//2]
        return total
        
mat=[]
n=int(input("enter size of matrix:"))
for i in range(n):
    row=[]
    for j in range(n):
        nu=int(input(f"enter number [{i}][{j}]:"))
        row.append(nu)
    mat.append(row)
obj=solution()
answer=obj.diagonalSum(mat)
print(answer)
