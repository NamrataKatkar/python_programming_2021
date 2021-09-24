#werite a program to sort the items in given list in ascending order using Merge sort

def MergeSort(A):
    start=0
    end=len(A)-1
    SortedList=MergeSortHelper(A,start,end)
    return SortedList
    
def MergeSortHelper(A,start,end):
    if start>=end:
        return A
    else:
        mid=(start+end)//2
        L=MergeSortHelper(A,start,mid)
        R=MergeSortHelper(A,mid+1,end)
        aux=[]
        i=start
        j=mid+1
        while i <=mid and j<=end:
            if A[i]<=A[j]:
                aux.append(A[i])
                i=i+1
            else:
                aux.append(A[j])
                j=j+1
        
        while i<=mid:
            aux.append(A[i])
            i=i+1
            
        while j<=end:
            aux.append(A[j])
            j=j+1
            
        A=aux
        return A
   

if __name__=="__main__":
  a=[5,-890,-678,-8,0,0,0,87,4]
  #a=[7,6,5,4]
  #a=[1]
  print ("before sorting: ")
  print(a)
  print ("After sorting: ")
  print(MergeSort(a))
  
