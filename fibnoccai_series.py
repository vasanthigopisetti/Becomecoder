def gen_fib(L,U,a=0,b=1):
 C=0
while C<=U:
        c=a+b
if C>=L and C<=U:
          print(C,end="")
          a=b
          b=c

L,U=map(int,input().split())
gen_fib(L,U)
 
