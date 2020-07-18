# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, artifacts, searched):
    if N == 0:
        return [0, 0]
    if not artifacts or not searched:
        return [0, 0]
        
    found, incomp = 0, 0 #answers
    
    n = len(artifacts.split(",")) #no of squares
    
    locations = [set() for _ in range(n)] #idea is to store cordinates in sets for each set of artifact
    
    for index, artifact in enumerate(artifacts.split(",")):
        x, y = artifact.split(" ")
        x1, y1 = int(x[0]) - 1,  int(ord(x[1]) - ord('A')) #start co-ord
        x2, y2 = int(y[0]) - 1, int(ord(y[1]) - ord('A')) #end co-ord
        if (x1, y1) == (x2, y2):  #single square
            locations[index].add((x1, y1))
        elif x1 == x2: #same row
            for i in range(y1, y2 + 1):
                locations[index].add((x1, i))
        elif y1 == y2: #same column
            for i in range(x1, x2 + 1):
                locations[index].add((i, y1))
        else: #complete square
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    locations[index].add((i, j))
    # print(locations)              
    original_pieces = [len(locations[index]) for index in range(len(locations))]  
    
    for loc in searched.split(" "):
        x, y = int(loc[0]) - 1, int(ord(loc[1]) - ord('A'))
        for index, artifact in enumerate(locations):
            if (x, y) in artifact:
                locations[index].remove((x, y)) #piece found
                if len(locations[index]) == 0:  #artifact found
                    found += 1

                break 
    #search for incomplete artifact    
    i = 0
    while i < len(locations):
        if len(locations[i]) != 0 and len(locations[i]) < original_pieces[i]:
            incomp += 1
        i += 1
    return [found, incomp]


print(solution(3, '1A 1B,2C 2C', '1B 1A 2C'))