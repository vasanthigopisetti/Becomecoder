def even_odd(n,data):
    ec=0
    oc=0
    for i in range(n):
        if data[i]%2:
            oc+=1
        else:
            ec+=1
    return ec,oc


n=int(input())
data=list(map(int,input().split()))
total=even_odd(n,data)
print(*total)
