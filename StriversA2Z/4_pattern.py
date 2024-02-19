class Solution:
    def printTriangle(N):
        # Code here
        
        for i in range(N+1):
            for j in range(i):
                print(i, end=" ")
            print('*')

    printTriangle(5)
