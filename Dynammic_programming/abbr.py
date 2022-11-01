from sys import stdin

def abbr(a,b):
    if b=='' and a.islower():
        return 1
    if a==b=='':
        return 1
    if b=='' and not a.islower():
        return 0
    if a == '' and b != '':
        return 0
    
    if a[0].islower():
        if a[0].capitalize() == b[0]:
            return max(abbr(a[1:],b[1:]),abbr(a[1:],b))
        else:
            return abbr(a[1:],b)
            
    else:
        if a[0] == b[0]:
            return abbr(a[1:],b[1:])
        else:
            return 0
        
        


def main():
    q = int(stdin.readline().strip())
    for i in range(q):
        a=stdin.readline().strip()
        b=stdin.readline().strip()
        if abbr(a,b):
            print('YES')
        else:
            print('NO')
main()
        
