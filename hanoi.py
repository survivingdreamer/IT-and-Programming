import sys
sys.setrecursionlimit(1000000)

def Hanoi(n, A, B, C):
    if n == 1:
        print("Переместим диск 1 с башни", A, "на башню", C)
        return
    Hanoi(n - 1, A, C, B)
    print("Переместим диск", n, "с башни", A, "на башню", C)
    Hanoi(n - 1, B, A, C)

Hanoi(5, 'A', 'B', 'C')