def listfunction(l):
    res=[]
    def helper(l):
        if len(l)==0:
            return
        for i in l :
            if type(i)==int:
                res.append(i)
            else:
                helper(i)
        return
    helper(l)
    return res
    
if __name__=="__main__":
    a=[5,-9,[1,2,[3,4]],0,0,0,[],87,4]
    print(listfunction(a))
    
