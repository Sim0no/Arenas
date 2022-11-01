from sys import stdin
def minimum_swaps(arr,n):
    grafo = {}    
    solucion = [i+1 for i in range(n)]
    ans = 0
    i = 0
    while solucion != arr:
        #print(solucion,arr)
        #Si no es necesario acomodar el elemento en su lugar
        if arr[i] != solucion[i]:
            
            aux = arr[i] #4
            arr[i] = arr[aux-1] 
            arr[aux-1]=aux
            ans += 1
        else:
            i+=1
    return ans
        
        
            
        
        
    
    
def main():
    n = int(stdin.readline().strip())
    array = [int(_) for _ in stdin.readline().strip().split()]
    print(minimum_swaps(array,n))

    
main()
