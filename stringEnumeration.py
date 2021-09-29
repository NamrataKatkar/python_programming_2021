#Print all permutation of given array items of length n . (meaning, create all possible combinations array items of length n). ck
#repetation allowed

def StringEnumeration(a,n):
    return StringEnumerationhelper("",a,n)
    
def StringEnumerationhelper(slate,a,n):
    if n==0:
        print (slate)
    else:
        for i in a:
            StringEnumerationhelper(slate+str(i),a,n-1)
        
if __name__=='__main__':
    a=['a','b','c']
    StringEnumeration(a,5)
