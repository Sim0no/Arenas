from collections import Counter
from sys import stdin
def main():
    n =  int(stdin.readline().strip())
    array = [int(_) for _ in stdin.readline().strip().split()]
    c = Counter(array)
    pares = 0
    for i in c:        
        pares += c[i]//2
    print(pares)
main()
