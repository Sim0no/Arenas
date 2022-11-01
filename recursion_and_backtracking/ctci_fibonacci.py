from sys import stdin
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    


def main():
    n = int(stdin.readline().strip())
    print(fibonacci(n))
main()
