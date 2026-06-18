class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = minutes * 6
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        
        angle_diff = abs(hour_angle - minute_angle)
        
        return min(angle_diff, 360 - angle_diff)
