class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_count = {}
        for char in text:
            char_count[char] = char_count.get(char, 0) + 1
        
        balloon_count = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1
        }
        
        max_instances = float('inf')
        for char, required_freq in balloon_count.items():
            available_freq = char_count.get(char, 0)
            max_instances = min(max_instances, available_freq // required_freq)
        
        return max_instances
