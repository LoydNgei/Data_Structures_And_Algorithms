class Solution:
    def invertedRightPyramid(N):

        for i in range(N, 0, -1):
            for j in range(i):
                print("*", end="")
            print()

    invertedRightPyramid(3);