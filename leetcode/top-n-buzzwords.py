"""
Input:
numToys = 6
topToys = 2
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
numQuotes = 6
quotes = [
"Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
"The new Elmo dolls are super high quality",
"Expect the Elsa dolls to be very popular this year, Elsa!",
"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
"For parents of older kids, look into buying them a drone",
"Warcraft is slowly rising in popularity ahead of the holiday season"
];

Output:
["elmo", "elsa"]

Explanation:
elmo - 4
elsa - 4
"elmo" should be placed before "elsa" in the result because "elmo" appears in 3 different quotes and "elsa" appears in 2 different quotes.

"""


from heapq import heappush, heappop
import re
quotes = [
"elsa is the hottest of the season! Elmo will be on every kid's wishlist!",
"The new Elmo dolls are super high quality",
"Expect the Elsa dolls to be very popular this year, Elsa!",
"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
"For parents of older kids, look into buying them a drone",
"Warcraft is slowly rising in popularity ahead of the holiday season"
]
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
n = 3
toyss  = set(toys)
toy_freq = {toy:[0, 0] for toy in toys}
for q in quotes:
    toy_quote = {toy:0 for toy in toys}
    for w in q.split():
        w = w.lower()
        w = re.sub(r"\W", "", w)
        if w in toyss:
            toy_freq[w][0] += 1
            if not toy_quote[w]:
                toy_freq[w][1] += 1
# x = toy_freq.items()

# x = sorted(x, key = lambda x:(-x[1][0], -x[1][1], x[0]))
# print(x)

class Toy:
    def __init__(self, name, freq, fquote):
        self.name = name
        self.count = freq
        self.fquote = fquote

    def __lt__(self, other):
        if not self.count == other.count:
            return self.count < other.count
        if not self.fquote == other.fquote:
            return self.fquote < other.fquote
        return self.name > other.name

heap = []
for toy in toy_freq.items():
    print(toy)
    t = Toy(toy[0], toy[1][0], toy[1][1])
    heappush(heap, t)
    if len(heap) > n:
        heappop(heap)
print([i.name for i in heap])