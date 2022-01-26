''' 1.	Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and number that come immediately
after a 13 also do not count.

sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
sum13([1, 2, 2, 1, 13,6,2,1]) → 9
'''

def sum13(a):
    if len(a)==1 :
        if a[0]==13:
            return 0
        return a[0]
    sum=a[0]
    for i in range(1,len(a)):
        if a[i]!=13 and a[i-1]!=13:
            sum=sum+a[i]
    return sum
            

if __name__=="__main__":
    a = [1]
    print(sum13(a))
