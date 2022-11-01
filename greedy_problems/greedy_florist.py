from sys import stdin
def main():
    n,k = [int(i) for i in stdin.readline().strip().split()]
    flores = [int(i) for i in stdin.readline().strip().split()]
    interes = 0
    promocion = k
    flores = sorted(flores,reverse=True)
    precio = 0
    for i in range(len(flores)):
        valor_flor = (1+interes)*flores[i]
        precio += valor_flor
        promocion -= 1
        if promocion == 0:
            promocion = k
            interes += 1
    print(precio)

main()
    
