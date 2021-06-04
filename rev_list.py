def total_marks(n,data):
    data.reverse()

n=int(input())
data=list(map(int,input().split()))
total_marks(n,data)
print(*data)
