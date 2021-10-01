'''Questtion:
Given a string S, we can ytransform every letter individually to be lowercase or uppercase to create another string. Return a list of all possible strings we could create
Examples:
Input: S="a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Input: S="3z4"
Output: ["3z4","3Z4"]

Input: S="12345"
Output: ["12345"]

Note: 
* S will be astring with length between 1 to 12.
* S will consist only of letters or digits.
'''

def CasePermutation(s):
    result=[]
    def CasePermutationHelper(s,i,slate):
        if i==len(s):
            result.append("".join(slate))
            return
        else:
            if s[i].isdigit():
                slate.append(s[i])
                CasePermutationHelper(s,i+1,slate)
                slate.pop()
            else:
                slate.append(s[i].lower())
                CasePermutationHelper(s,i+1,slate)
                slate.pop()
                slate.append(s[i].upper())
                CasePermutationHelper(s,i+1,slate)
                slate.pop()
    CasePermutationHelper(s,0,[])
    return result
            
if __name__=='__main__':
    #a=['a','1','2','b']
    a='a12b'
    print(CasePermutation(a))
    
