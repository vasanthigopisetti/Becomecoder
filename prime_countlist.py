import math as m
def isprime(num):
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1


def countPrimes(n,data):
    pc=0
    for i in data:#45 43 17 18 13
        if isprime(i):
           pc+=1
    return pc


n=int(input())
data=list(map(int,input().split()))
pc=countPrimes(n,data)
print(pc)
