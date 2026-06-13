class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        
        for word in words:

            word_weight = 0
            for char in word:
                char_index = ord(char) - ord('a')
                word_weight += weights[char_index]
            
            mod_value = word_weight % 26
            
            mapped_char = chr(ord('z') - mod_value)
            result.append(mapped_char)
        
        return ''.join(result)
