from sys import stdin
def main():
    n_juguetes,dinero=[int(i) for i in stdin.readline().strip().split()]
    juguetes = [int(i) for i in stdin.readline().strip().split()]
    juguetes.sort()
    i = 0
    comprados=0
    while dinero >= juguetes[i]:
        dinero -= juguetes[i]
        comprados+=1
        i+=1
    print(comprados)
main()
