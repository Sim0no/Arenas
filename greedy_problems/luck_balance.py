from sys import stdin
def main():
    n,k = [int(i) for i in stdin.readline().split()]
    eventos = []
    suerte = 0
    for i in range(n):
        l,t = [int(i) for i in stdin.readline().split()]
        eventos += [(l,t)]
    eventos = sorted(eventos, reverse=True)

    for i in range(len(eventos)):
        if k-eventos[i][1] >= 0:
            k -= eventos[i][1]
            suerte += eventos[i][0]
        else:
            suerte -= eventos[i][0]
        
    print(suerte)
    
main()
