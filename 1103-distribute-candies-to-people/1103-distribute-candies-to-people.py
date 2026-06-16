class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        person_index = 0
        candies_to_give = 1
        
        while candies > 0:
            actual_candies = min(candies, candies_to_give)
            result[person_index] += actual_candies
            
            candies -= actual_candies
            
            person_index = (person_index + 1) % num_people
            
            candies_to_give += 1
        
        return result
