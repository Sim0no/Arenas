from sys import stdin


def maximum_recu(array,total):
    if len(array)==0:
        return total
    if len(array)==1:
        return max(total,total+array[0],0)
    #Maximo entre tomar y no tomar
    return max(maximum_recu(array[2:],total+array[0]),maximum_recu(array[1:],total),0)
    

def maximum_dinamic(array):
    array=[0,0]+array
    answer=[0 for i in range(len(array)+2)]
    for i in range(len(array)):
        if i == 0:
            answer[i] = array[0]
        elif i == 1:
            answer[i] = array[1]
        else:
            answer[i] = max(answer[i-2]+array[i],answer[i-1],array[i])
        answer+=[0]
    return max(answer)
            
            

def main():
    n = int(stdin.readline().strip())
    arr=[int(_) for _ in stdin.readline().strip().split()]
    print(maximum_dinamic(arr))
    
main()
