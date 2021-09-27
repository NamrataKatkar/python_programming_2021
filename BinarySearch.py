#write a program to find a target value in given SORTED array

def BinarySearch(A,T):
    start=0
    end=len(A)-1
    return BinarySearchHelper(A,start,end,T)
    
def BinarySearchHelper(A,start,end,T):
    if start>=end:
        if T==A[start]:
            return start
        return -1
        
    else:
        mid=start+(end-start)//2
        if T==A[mid]:
            return mid
        elif T<A[mid]:
            return BinarySearchHelper(A,start,mid,T)
        elif T>A[mid]:
            return BinarySearchHelper(A,mid+1,end,T)
   

if __name__=="__main__":
  #a=[5,-890,-678,-8,0,0,0,87,4]
  a=[5,6,9,15]
  #a=[1]
  T=15
  index=BinarySearch(a,T)
  if index== -1:
      print("{} not found".format(T))
  else:
      print("{} is at {}".format(T,index))
