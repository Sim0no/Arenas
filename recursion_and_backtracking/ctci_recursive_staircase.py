from sys import stdin


from functools import lru_cache

@lru_cache(maxsize=128, typed=False)
def ways_climb_staircase(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return ways_climb_staircase(n-1)+ways_climb_staircase(n-2)+ways_climb_staircase(n-3)
    
    
    

def main():
    n_m =(10**10)+7
    s = int(stdin.readline().strip())
    for i in range(s):
        n = int(stdin.readline().strip())
        print(ways_climb_staircase(n)%n_m)
main()
