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
    nonprimes=[]
    for i in data:#45 43 17 18 13
        if isprime(i):
           prime.append(i)
        else:
            nonprimes.append(i)
    return prime,nonprimes



n=int(input())
data=list(map(int,input().split()))
primes,np=findPrimes(n,data)
print(*primes)
print(*np)
