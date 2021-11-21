#find the fibonacci series upto n using recursion
#if n=5, output= 8  [0,1,1,2,3,5,8]

def fib(n):
    if n==1 or n==0:
        return 1
    return fib(n-1)+fib(n-2)
if __name__=='__main__':
    print(fib(5))
