class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calculateWaviness(num):
            # Convert number to string to work with individual digits
            s = str(num)
            # Numbers with fewer than 3 digits have waviness 0
            if len(s) < 3:
                return 0
            
            waviness = 0
            # Check each digit except first and last
            for i in range(1, len(s) - 1):
                left_digit = int(s[i-1])
                current_digit = int(s[i])
                right_digit = int(s[i+1])
                
                # Check if current digit is a peak
                if current_digit > left_digit and current_digit > right_digit:
                    waviness += 1
                # Check if current digit is a valley
                elif current_digit < left_digit and current_digit < right_digit:
                    waviness += 1
                    
            return waviness
        
        total = 0
        # Calculate waviness for each number in the range
        for num in range(num1, num2 + 1):
            total += calculateWaviness(num)
            
        return total
