#Write a program to sort a given list in ascending order using bubble sort

def BubbleSort(a):
    n=len(a)
    for i in range(0,n-1):
        for j in range(n-1,i,-1):
            if a[j]<a[j-1]:
               (a[j],a[j-1]) =(a[j-1],a[j])
    return a

if __name__=="__main__":
  a=[5,-890,-678,-8,0,0,0,87,4]
  print ("before sorting: ")
  print(a)
  print ("After sorting: ")
  print(BubbleSort(a))
