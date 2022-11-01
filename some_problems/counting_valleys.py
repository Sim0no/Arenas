from sys import stdin
def main():
    steps = int(stdin.readline().strip())
    path = stdin.readline().strip()
    valles = 0
    nivel = 0
    for step in path:
        if step == 'U':
            nivel += 1
        if step == 'D':
            nivel -= 1
        if nivel == 0 and step == 'U':
            valles += 1
    print(valles)
main()
