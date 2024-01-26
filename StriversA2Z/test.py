class Solution():
    def loop_this(n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end="")
            print()

    loop_this(4)