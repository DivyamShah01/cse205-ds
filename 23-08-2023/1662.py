class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        x=""
        y=""
        for i in range(len(word1)):
            x=str(x)+str(word1[i])

        for j in range(len(word2)):
            y=str(y)+str(word2[j])

        return (x==y)