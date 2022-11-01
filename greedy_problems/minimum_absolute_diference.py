from sys import stdin
minimo = float("inf")
            
def main():
    n = int(stdin.readline().strip())
    array = sorted([int(_) for _ in stdin.readline().strip().split()])
    global minimo
    for i in range(len(array)-1):
        minimo = min(minimo, abs(array[i+1]-array[i]))
        if minimo == 0:
            break

    print(minimo)
        
        
    
    
main()
