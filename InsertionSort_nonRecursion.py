#write a program to sort a given list in ascending order using Insertion sort recursion method

def InsertionSort(a,n):
    if n<=1:
        return a
    for i in range(1,n):
        ith=a[i] 
        j=i-1 
        while j >=0 and a[j] >ith:
            a[j+1]=a[j]     #right shifting to avoid swapping
            j=j-1           #decreasin j for while loop
        a[j+1]=ith
    return a

if __name__=="__main__":
  a=[5,-890,-678,-8,0,0,0,87,4]
  #a=[7,6,5]
  print ("before sorting: ")
  print(a)
  print ("After sorting: ")
  print(InsertionSort(a,len(a)))
