class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones_left = n
        remove_count = 10 
        alice_turn = True
        
        while stones_left >= remove_count:
            stones_left -= remove_count
            remove_count -= 1
            alice_turn = not alice_turn
            
        return not alice_turn
