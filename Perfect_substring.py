#Find the number of substring that contain all digits exactly k times or 0 times.

def perfectstring(a):
    i=0
    res=[]
    target=0
    while i<len(a):
        target=a[i]
        j=i
        cnt=1
        while j<len(a)-1 and a[j]==a[j+1]:
            cnt+=1
            j+=1
        if cnt==target:
            res.append(target)
        i=i+cnt
    return res
    
if __name__=="__main__":
    a=[0,0,1,1,1,2,2,3,3,3,4,5]
    print(perfectstring(a))
