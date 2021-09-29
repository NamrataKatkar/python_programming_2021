#Enumerate all possible binary strings of length n . (meaning, create all possible combinations of 0 and 1 of length n). ck

#approach 1
#using recursion - More job to do in logic section
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
    
#approach 2
#using recursion - Less job to do in logic section   
def binaryString(n):
    binaryStringhelper("",n)
    
def binaryStringhelper(slate,n):
    if n==0:
        print (slate)
    else:
        binaryStringhelper(slate+'0',n-1)
        binaryStringhelper(slate+'1',n-1)
         

#main function
if __name__=='__main__':
    binaryString(3)
    
 
