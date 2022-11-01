from sys import stdin

def main():
    n = int(stdin.readline().strip())
    k = int(stdin.readline().strip())
    array = []
    injusticia = float("inf")
    for i in range(n):
        elemento = int(stdin.readline().strip())
        array += [elemento]
    array = sorted(array)
    for i in range(n-k+1):
        injusticia = min(injusticia, array[i+k-1]-array[i])
        if injusticia == 0:
            break
    
    print(injusticia)
main()
