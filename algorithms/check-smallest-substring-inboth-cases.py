https://www.geeksforgeeks.org/smallest-substring-with-each-letter-occurring-both-in-uppercase-and-lowercase/


"""
A string is balanced if every letter in the string appears in both uppercase and lowercase, i.e “AabB” is a balanced string whereas “Ab” is not a balanced string. 

Input: S = “azABaabba”
Output: ABaab
Explanation:
Substring {S[2], …, S[6]} (0-based indexing) is the smallest substring which is balanced.

Input: S = “Technocat”
Output: -1
"""

# Ideas:
#	- Use two-pointer technique
#	- Keep on shrinking on adding each characters whether substring is 
#		balanced or not
#	- Use mapping for charcter whter, it has not both cases ie upper and lowerß
#
#

# python 3 program for the above approach
import sys

def balanced(small, caps):

	for i in range(26):
		if (small[i] != 0 and (caps[i] == 0)):
			return 0

		elif((small[i] == 0) and (caps[i] != 0)):
			return 0
	return 1

# Function to find smallest length substring
# in the given string which is balanced
def smallestBalancedSubstring(s):

	# Store frequency of
	# lowercase characters
	small = [0 for i in range(26)]

	# Stores frequency of
	# uppercase characters
	caps = [0 for i in range(26)]

	# Count frequency of characters
	for i in range(len(s)):
		if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
			caps[ord(s[i]) - 65] += 1
		else:
			small[ord(s[i]) - 97] += 1

	# Mark those characters which
	# are not present in both
	# lowercase and uppercase
	mp = {}
	for i in range(26):
		if (small[i] and caps[i]==0):
			mp[chr(i + 97)] = 1

		elif (caps[i] and small[i]==0):
			mp[chr(i + 65)] = 1

	# Initialize the frequencies
	# back to 0
	for i in range(len(small)):
		small[i] = 0
		caps[i] = 0

	# Marks the start and
	# end of current substring
	i = 0
	st = 0

	# Marks the start and end
	# of required substring
	start = -1
	end = -1

	# Stores the length of
	# smallest balanced substring
	minm = sys.maxsize

	while (i < len(s)):
		if(s[i] in mp):
		
			# Remove all characters
			# obtained so far
			while (st < i):
				if (ord(s[st]) >= 65 and ord(s[st]) <= 90):
					caps[ord(s[st]) - 65] -= 1
				else:
					small[ord(s[st]) - 97] -= 1

				st += 1
			i += 1
			st = i
		else:
			if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
				caps[ord(s[i]) - 65] += 1
			else:
				small[ord(s[i] )- 97] += 1

			# Remove extra characters from
			# front of the current substring
			while (1):
				if (ord(s[st]) >= 65 and ord(s[st])<= 90 and caps[ord(s[st])- 65] > 1):
					caps[ord(s[st]) - 65] -= 1
					st += 1
				elif (ord(s[st]) >= 97 and ord(s[st]) <= 122 and small[ord(s[st]) - 97] > 1):
					small[ord(s[st]) - 97] -= 1
					st += 1
				else:
					break

			# If substring (st, i) is balanced
			if (balanced(small, caps)):
				if (minm > (i - st + 1)):
					minm = i - st + 1
					start = st
					end = i
			i += 1

	# No balanced substring
	if (start == -1 or end == -1):
		print(-1)

	# Store answer string
	else:
		ans = ""
		for i in range(start,end+1,1):
			ans += s[i]
		print(ans)

# Driver Code
if __name__ == '__main__':

	# Given string
	s = "azABaabba"
	smallestBalancedSubstring(s)
	
	# This code is contributed by bgangwar59.
