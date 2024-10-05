# The KMP (Knuth-Morris-Pratt) algorithm is a string matching algorithm used to find all occurrences 
# of a pattern in a text efficiently. It avoids redundant comparisons by preprocessing the pattern 
# using an auxiliary array called the LPS (Longest Prefix Suffix) array. 

# The time complexity of KMP is O(n+m), where n is the length of the text and 
# m is the length of the pattern.

# Text (txt): "ABABDABACDABABCABAB"
# Pattern (pat): "ABABCABAB"
# Output: [11]

# LPS = [0, 0, 1, 2, 0, 1, 2, 3, 4]

# Code:

class Solution:
    def LPSarray(self, pat,m):
        lps = [0]*m
        length,i = 0,1

        while i<m:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    def KMPsearch(self, pat, txt):
        m,n = len(pat),len(txt)
        lps = self.LPSarray(pat,m)
        result = []
        j,i = 0,0

        while i<n:
            if pat[j] == txt[i]:
                j += 1
                i += 1
            if j == m:
                result.append(i-j+1)
                j = lps[j-1]
            elif i < n and pat[j] != txt[i]:
                if j!=0: j = lps[j-1]
                else: i += 1
        return result
    
txt = "GuptaPrashant"
pat = "taP"
sol = Solution()
print(sol.KMPsearch(pat,txt))
            

