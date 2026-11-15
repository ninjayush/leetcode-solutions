class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                
                boo=False
                if i+len(needle) > len(haystack):
                    return -1
                p=i+1
                for j in range(1, len(needle)):
                    if haystack[p]==needle[j]:
                        p+=1
                        # if p>=len(haystack):
                        #     break
                    else:
                        break

                if p-i==len(needle):
                    return i
        
        return -1
