n =10
def fibo(n):
    if n==0 : return 0
    if n==1 :return 1
    else :
        n= (fibo(n-1) + fibo(n-2))
        print(n)
        return n

fibo(n)