# find factorial of n using recursion
# if n=5 , output : 120

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
if __name__=='__main__':
    print(fact(5))
