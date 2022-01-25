# Find the givene substring in the string
def FindSubstring(string,substring):
    if len(substring)>len(string):
        return False
    for i in range(0,1+len(string)-len(substring)):
        matched=True
        j=0
        while j<len(substring):
            if string[i+j]==substring[j]:
                j+=1
            else:
                matched=False
                break
        if j==len(substring):
            break
        #print(string[i]+":" +str(matched))
    return matched
    
if __name__=="__main__":
  string='abcde'
  substring='bc'
  print("Is substring present ? " + str(FindSubstring(string,substring)))
