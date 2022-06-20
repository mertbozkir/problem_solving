class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        
        return max([len(i.split(" ")) for i in sentences])

        
        """max = 0
        for sentence in sentences:
            if len(sentence.split(" ")) > max:
                max = len(sentence.split(" "))
                
        return max"""