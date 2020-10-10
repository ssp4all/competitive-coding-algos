from functools import lru_cache
from urllib.request import urlopen
import urllib

@lru_cache(maxsize=32)
def get_info(num):
	link = "https://ssp4all.github.io"
	print(link)
	try:
		s = urlopen(link)
		# print(s.read())
		s.close()
	except urllib.error.HTTPError:
		print('404')
for i in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
	get_info(i)
	x = get_info.cache_info()
	print(x)