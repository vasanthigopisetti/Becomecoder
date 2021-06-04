import math as m
def isprime(num):
    if num==1:
        return 0
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1


def findPrimes(n,data):
    prime=[]
    for i in data:#45 43 17 18 13
        if isprime(i):
           prime.append(i)
    return prime



n=int(input())
data=list(map(int,input().split()))
primes=findPrimes(n,data)
print(*primes)
