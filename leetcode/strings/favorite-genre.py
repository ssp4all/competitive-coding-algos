https://leetcode.com/discuss/interview-question/373006

from collections import defaultdict

userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}
songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

s2g = {}
for i in songGenres.keys():
	for j in songGenres[i]:
		s2g[j] = i

ans = defaultdict(list)

for i in userSongs:
	freq = defaultdict(int)
	for j in userSongs[i]:
		freq[s2g[j]] += 1
	for z in freq:
		if freq[z] == max(freq.values()):
			ans[i].append(z)
	# if len(ans[i]) == 0:
	# 	ans[i] += freq.keys()
print(ans)


"""More optimized"""
def favGenres(userSongs, songGenres):
    output = {}
    for user in userSongs:
        song_list = userSongs[user]
        count = {}

        for song in song_list:
            for genre in songGenres:
                if(song in songGenres[genre]):
                    count[genre] = count.get(genre,0) + 1

        output[user] = [key for key, val in count.items() if val == max(count.values())]
    
    return output