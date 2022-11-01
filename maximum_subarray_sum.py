from sys import stdin
from functools import lru_cache

@lru_cache(maxsize=128, typed=False)
def maximum_subarray_sum(arr,m):
    if len(arr)==1:
        return sum(arr)%m
    #maximo entre el arreglo actual, entre tomar el arreglo sin el primer elemento y el arreglo sin el ultimo elemento
    return max(sum(arr)%m,maximum_subarray_sum(arr[:-1],m),maximum_subarray_sum(arr[1:],m))
def main():
    q = int(stdin.readline().strip())
    for i in range(q):
        n,m = [int(_) for _ in stdin.readline().strip().split()]
        array = [int(_) for _ in stdin.readline().strip().split()]
        print(maximum_subarray_sum(tuple(array),m))
        
    
main()
