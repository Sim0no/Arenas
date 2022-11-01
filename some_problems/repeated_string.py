from sys import stdin
from collections import Counter
def busqueda_a(s,n):

    completas = n//len(s)
    incompleto = n%len(s)
    cadena = s.count('a')*completas
    
    for i in range(incompleto):
        if s[i] == 'a':            
            cadena += 1
    
    
    return cadena
def main():
    cadena = stdin.readline().strip()
    x = Counter(cadena)
    
    n = int(stdin.readline().strip())
    if len(x) == 1 and x['a']:
        print(n)
    else:
        print(busqueda_a(cadena,n))
main()
