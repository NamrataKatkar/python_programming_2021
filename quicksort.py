#Write a program to sort a given list in ascending order using Quick sort

import random
def quicksort(A):
    start=0
    end=len(A)-1
    sortedList=quicksortHelper(A,start,end)
    return sortedList

def quicksortHelper(A,start,end):
    #base case
    if start>=end:
        return A
    else:
    #logic - decrease and conquer
        random_index=random.randint(start,end)
        pivot=A[random_index]
        small=start
        big=start+1
        (A[random_index],A[start])=(A[start],A[random_index])
        while big<=end:
            if A[big]<pivot:
                small=small+1
                (A[big],A[small])=(A[small],A[big])
                big=big+1
            else:
                big=big+1
                
        (A[small],A[start])=(A[start],A[small])
        
        # recursion
        quicksortHelper(A,start,small-1)
        quicksortHelper(A,small+1,end)
        return A
        
if __name__=='__main__':
    #a=[6,7,3,90,3,-1,-2]
    a=[5,-890,-678,-8,0,0,0,87,4]
    print("before sorting:")
    print(a)
    print("After sorting:")
    print(quicksort(a))
    
