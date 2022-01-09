# sort the array with k numbers in it (like student age)
def countSort(a,maxnumber):
    d=[0]*maxnumber
    for i in range(0,len(a)):
        d[a[i]]=d[a[i]]+1
    res=[]
    for j in range(0,len(d)):
        if d[j]!=0:
            for k in range(0,d[j]):
                res.append(j)
    return res


if __name__=='__main__':
    a=[9,8,7,2,2,1,0,9]
    print(countSort(a,10))
