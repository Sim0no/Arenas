from sys import stdin

def candies_d(rating):
    candies = [1 for i in range(len(rating))]
    for i in range(1,len(rating)):
        if rating[i] > rating[i-1] and candies[i] <= candies[i-1]:
           candies[i] = candies[i-1] + 1
    for i in range(len(rating)-1,0,-1):
        if rating[i] < rating[i-1] and  candies[i] >= candies[i-1]:
            candies[i-1] = candies[i] + 1
    return sum(candies)

        
        
        
                   
                   
    


def main():
    rating=[]
    n=int(stdin.readline().strip())
    for i in range(n):
        rating+=[int(stdin.readline().strip())]
    print(candies_d(rating))
main()
        
