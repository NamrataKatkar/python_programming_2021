#Enumerate all possible decimal strings of length n . (meaning, create all possible combinations of 0 and 9 of length n). ck

def DecimalString(n):
    return DecimalStringhelper("",n)
    
def DecimalStringhelper(slate,n):
    if n==0:
        print (slate)
    else:
        for i in range (0,10):
            DecimalStringhelper(slate+str(i),n-1)
        
if __name__=='__main__':
    DecimalString(3)
