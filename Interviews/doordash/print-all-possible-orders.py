# generate all possible pickup and delivery ways 

def get_count(pickup, dropoff):
    print(pickup, dropoff)
    if dropoff < pickup or pickup < 0 or dropoff < 0:    return 0 
    if dropoff == pickup == 0:    return 1
    count = 0 
    count += pickup * get_count(pickup - 1, dropoff)
    count += (dropoff - pickup) * get_count(pickup, dropoff - 1)
    return count 


def backtrack(path):
    if len(path) == 2 * n: # all orders added
        print(path)
        return
    for i in range(n):
        if pu[i] == 0:
            pu[i] = 1
            backtrack(path + ['p' + str(i + 1)])
            pu[i] = 0
        if do[i] == 0 and pu[i] == 1:
            do[i] = 1
            backtrack(path + ['d' + str(i + 1)])
            do[i] = 0
   
n = 3
pu = [0] * n
do = [0] * n
backtrack([])
