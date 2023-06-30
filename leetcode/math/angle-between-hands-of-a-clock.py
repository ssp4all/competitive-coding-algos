# https://leetcode.com/problems/angle-between-hands-of-a-clock

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        HOUR_ANGLE = 30 
        MINUTE_ANGLE = 6 

        min_angle = MINUTE_ANGLE * minutes 
        # we'll convert hour:minutes to hours only by 
        # adding minutes and then dividing by 60 bcoa 1hr = 60 min
        hr_angle = HOUR_ANGLE * (hour % 12) 
        # The hour hand of the clock moves 360 degree in 
        # 12 hours(12x60 min) which means (360/(12x60)) =0.5 degree in a minute
        hr_angle += minutes * 0.5
        diff = abs(min_angle - hr_angle)
        return min(diff, 360 - diff) # 01:57