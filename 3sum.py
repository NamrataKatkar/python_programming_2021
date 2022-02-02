
def findTriplets( arr, n):
    #code here
    arr.sort()
    b=False
    for i in range(0,len(arr)):
        n3=0-arr[i]
        arr[i],arr[0]=arr[0],arr[i]
        b=twoSum(arr[1:],n3)
        arr[i],arr[0]=arr[0],arr[i]
        if b :
            return 1
    return 0
        
def twoSum(a, target):
    i=0
    j=len(a)-1
    while i <j:
        if a[i]+a[j]==target :
            return True
        elif a[i]+a[j]>target:
            j-=1
        else: 
            i+=1
            
if __name__=="__main__":
    arr = [-1,0,2]
    print(findTriplets(arr,len(arr)))
