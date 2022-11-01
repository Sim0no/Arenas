from sys import stdin


def ways(n,m):
    if len(m) == 0:
        return n == 0
    if n == 0:
        return 1
    if n < 0:
        return 0
    return ways(n-m[0],m) + ways(n,m[1:])





    

def main():
    n,m=[int(_) for _ in stdin.readline().strip().split()]
    coins = [int(_) for _ in stdin.readline().strip().split()]
    print(ways(n,coins))
main()
