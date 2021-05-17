https://www.geeksforgeeks.org/inserting-m-into-n-such-that-m-starts-at-bit-j-and-ends-at-bit-i-set-2/

"""

Given two 32-bit numbers, N and M, and two-bit 
positions, i and j. Write a method to insert
 M into N such that M starts at bit j and ends at bit i. 
 You can assume that the bits j through i have enough space 
 to fit all of M. Assuming index start from 0.

Examples:

a)  N = 1024 (10000000000),
    M = 19 (10011),
    i = 2, j = 6 
    Output : 1100 (10001001100)
"""


def Solution(M, N, i, j):


	"""
	psuedocode
				. .	
	index =  6543210
	number = 0101010
	
	1)
	save all bits from i + 1 to 0 
	capture_mask = (1 << i) - 1
	saved_bits = N & capture_mask 

	2)
	clear bits from j to 0 
	clear_mask = -1 << (j + 1)

	clear_bits = N & clear_mask 

	3) 
	align M then insert it 
	M = M << i 
	N |= M 

	4) add saved bits 
	N |= saved_bits 

	"""

	def insertion(n, m, i, j):
	  
	    clear_mask = -1 << (j + 1)
	    capture_mask = (1 << i) - 1
	  
	    # Capturing bits from i-1 to 0
	    captured_bits = n & capture_mask 
	  
	    # Clearing bits from j to 0
	    n &= clear_mask
	  
	    # Shiftng m to align with n
	    m = m << i
	  
	    # Insert m into n
	    n |= m 
	  
	    # Insert captured bits
	    n |= captured_bits
	  
	    return n