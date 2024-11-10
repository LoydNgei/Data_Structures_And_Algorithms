class Solution:
    def printTriangle(self, N:int):
        # Code here
        for i in range(1, N+1):
            for j in range(i):
                print("* ", end="")
            print()


if __name__ == "__main__":
    t = int(input("Enter the number of test cases: "))
    for _ in range(t):
        N = int(input("Enter the input: "))
        ob = Solution()
        ob.printTriangle(N)
