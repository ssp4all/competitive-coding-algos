def process(line: str) -> str:
    # Return 'VALID' or 'INVALID'
    try:
        if not line: return "INVALID"
        to_check = line[2:]
        checksum = line[:2]
        if not to_check or len(to_check) != 6 or not checksum or len(checksum) != 2:
            return "INVALID"
        # print(to_check, checksum)
        dec = int(to_check, 16)
        # print("->", list(str(dec)))
        sum_dec = sum(list(map(int, list(str(dec)))))

        to_hex = hex(sum_dec).split("x")[-1]
        # print(sum_dec, to_hex)
        if (to_hex and c
            hecksum) and to_hex.lower() == checksum.lower():
            return "VALID"
        return "INVALID"
    except ValueError:
        return "INVALID"


from math import acos, sin, cos, radians, floor, pi
from collections import defaultdict
RADIUS_MILES = 3963

class Data:
    def __init__(self, city="", lat="0.0", lon="0.0"):
        self.city = city
        self.lat = self.convert_to_rad(float(lat))
        self.lon = self.convert_to_rad(float(lon))
        
    def convert_to_rad(self, deg):
        return (deg * pi) / 180

class DestinationCalculator:
    def __init__(self):
        self.cache = defaultdict(Data)

    def process(self, line: str) -> str:
        ip = line.split(":")
        if ip[0] == "LOC":
            cityname, lat, lon = ip[1], ip[2], ip[3]
            if cityname not in self.cache:
                self.cache[cityname] = Data(cityname, lat, lon)
            return cityname #acknowledgement
        else:
            accno, start, end = ip[1], ip[2], ip[3]
            if start in self.cache and end in self.cache:
                return self.calculate_dist(accno, self.cache[start], self.cache[end])
        
        
    def calculate_dist(self, accno, d1, d2):
        #helper to calculate distance
        diff = abs(d1.lon - d2.lon)
        a = sin(d1.lat) * sin(d2.lat)
        b = cos(d1.lat) * cos(d2.lat) * cos(diff)
        
        angle = acos(a + b)
        dis = angle * RADIUS_MILES
        
        
        ans = accno + ":" + d1.city + ":" + d2.city + ":" + str(floor(dis))
        return ans
            
            
from collections import defaultdict
ip = ["CHI:NYC:100", "NYC:CHI:100", "NYC:LA:2000", "NYC:RDU:1000"]
g = defaultdict(set)
for i in ip:
    st, des, dis = i.split(":")
    g[st].add((des, int(dis)))
    g[des].add((st, int(dis)))
print(g)

ans = []
st, mid, end, dis = "", "", "", 0
for i in g:
    print("i ", i)
    # find farthest dest for start
    if not g[i]:    continue
    c1, d1 = max(g[i], key=lambda x:x[1])
    print("->", c1, d1) 
    c2, d2 = max(g[c1], key=lambda x:x[1])
    print("# ", c2, d1 + d2)
    if c1 == c2: continue
    d = d1 + d2
    if dis < d1:
        st, mid, end, dis = i, c1, c2, d
        print(f"{st}:{mid}:{end}:{d}")

