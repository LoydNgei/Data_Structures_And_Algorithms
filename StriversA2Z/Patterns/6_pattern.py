# Reverse Number Triangle
class Reverse:
    def ReverseTriangle(n: int)->None:
        for i in range(n, 0, -1):
            for j in range(i):
                print(j+1, end=" ")
            print()
    ReverseTriangle(7);