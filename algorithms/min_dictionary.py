stats = {'a':1000, 'b':3000, 'c': 10000}

#find min/max in given array
a = min(stats.keys(), key = lambda x:stats[x] )

# Sort in decreasing order
x = sorted(stats, key=lambda x:stats[x], reverse=1)

print(a)