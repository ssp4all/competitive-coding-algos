https://leetcode.com/problems/mirror-reflection/

"""
There is a special square room with mirrors on each of the four walls.  
Except for the southwest corner, there are receptors on each of the 
remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest 
corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed 
that the ray will meet a receptor eventually.)


"""
class Solution(object):
    def mirrorReflection(self, p, q):
        def gcd(a, b):
            if not a or not b:   return a or b
            return gcd(b % a, a)
            
        g = gcd(p, q)
        p = (p / g) % 2
        q = (q / g) % 2

        return 1 if p and q else 0 if p else 2