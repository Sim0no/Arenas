from sys import stdin

def recorrido_minimo(array):
    posicion_actual = 0
    pasos = 0
    while posicion_actual != len(array)-1:
        if posicion_actual+2 < len(array) and array[posicion_actual+2] == 0:
            posicion_actual += 2
        elif posicion_actual+1 < len(array) and array[posicion_actual+1] == 0:
            posicion_actual += 1
            
        pasos += 1
    return pasos
        
        
        
    

def main():
    n = int(stdin.readline().strip())
    array = [int(_) for _ in stdin.readline().strip().split()]
    print(recorrido_minimo(array))
    
    
main()
