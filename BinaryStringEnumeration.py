#Enumerate all possible binary strings of length n . (meaning, create all possible combinations of 0 and 1 of length n). ck

#using recursion
def binaryString(n):
    if n==1:
        return ['0','1']
    else:
        prev=binaryString(n-1)
        res=[]
        for s in prev:
            res.append(s+'0')
            res.append(s+'1')
        return res
        
if __name__=='__main__':
    print(binaryString(3))
    
 
