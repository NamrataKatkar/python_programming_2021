#write a program to sort the below list in ascending order using selection sort

def selectionsort(a):
    for i in range(0,len(a)):
        min=i
        for j in range(i+1,len(a)):
            if a[j]<a[min]:
                min=j
        temp=a[min]
        a[min]=a[i]
        a[i]=temp
    return a

if __name__=="__main__":
  a=[5,-890,-678,-8,0,0,0,87,45]
  print(selectionsort(a))
