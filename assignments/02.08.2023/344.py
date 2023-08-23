class Solution:
    def reverseString(self, s: List[str]) -> None:
        i=0
        def func(s,i):
            if (i>=len(s)/2):
                return s
            s[i],s[len(s)-i-1]=s[(len(s))-i-1],s[i]
            func(s,i+1)
        func(s,i)