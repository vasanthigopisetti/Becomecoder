n=int(input())
data=list(map(int,input().split()))
res=0
for i in range(n):
    res=res+data[i]
print(res)

