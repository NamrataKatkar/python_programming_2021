#Sort the 2D list contains players name and score. Sort in Descending order 1st by score and then by players name.
#[["Smith",20],["Jones",15],["Jones",20]]

def Sort_Desc_asc(a):
    for i in range(0,len(a)):
        j=len(a)-2
        temp=a[len(a)-1]
        while j>=i:
            if temp[1]>a[j][1]:
                a[j+1]=a[j]
                j-=1
            elif temp[1]==a[j][1]:
                if temp[0]<a[j][0]:
                    a[j+1]=a[j]
                    j-=1
        a[j+1]=temp
        return a
                    


if __name__=='__main__':
    a=[["Smith",20],["Jones",15],["Jones",20]]
    print(Sort_Desc_asc(a))
