class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m=len(word1)
        n=len(word2)
        max_len=max(m,n)
        pointer,merged_word=0,""
        while pointer< max_len:
                if pointer < m and pointer < n:
                    merged_word+=word1[pointer]+word2[pointer]
                elif pointer >= n and pointer < m :
                    merged_word+=word1[pointer]
                else:
                    merged_word+=word2[pointer]        
                pointer+=1
        return merged_word