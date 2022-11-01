from sys import stdin


def super_digit(n,k):
    #En la primera iteración es sumar los digitos y multiplicarlo por K, no vale la pena hacer la suma de todo
    n = sum([int(i) for i in str(n)])*k
    if int(n) <= 9:
        return n
    else:
        
        return super_digit(str(n),1)
def main():
    n,k = [_ for _ in stdin.readline().strip().split()]
    super_d = super_digit(n,k)
    print(super_d)
main()

