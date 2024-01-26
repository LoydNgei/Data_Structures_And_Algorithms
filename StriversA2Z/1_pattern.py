class Solution:
    def nForest(self, N:int) ->None:

        for i in range(N):

            for j in range(N):

                print("* ",end="")

            print()


# LEARN HOW TO WRITE TEST CASES

if __name__ == '__main__':
    t = int(input("Enter the number of test cases: "))
    for _ in range(t):
        N = int(input("Enter the value of N: "))
        ob = Solution()
        ob.nForest(N)