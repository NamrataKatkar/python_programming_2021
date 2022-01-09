#write a code to find positions of 2 elements whose sum is equal to target 
def twoSumPositions(a,target):
    d={}
    for i in range(0,len(a)):
        num2=target-a[i]
        if a[i] not in d.keys():
            d[num2]=i
        else:
            return [d[a[i]],i]
    return
            
            

if __name__=='__main__':
    a=[9,1,11,5]
    print(twoSumPositions(a,14))
