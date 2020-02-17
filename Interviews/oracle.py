ip = {
    "Jon": "Smith",
    "Adam": ["Jake", None, "Nancy"],
    "Alex": {
        "Muller": [ None, "Sam" ],
        "Phil": None,
        "Xav": ["Mike", "Tom"]
        },
    "Lex": None,
}
op = []

def bt(ip, path):
    if not ip:
        op.append(path)
    elif type(ip) == list:
        for i in range(len(ip)):
            bt(ip[i], path + "." +str(i))
    elif type(ip) == dict:
        for i in ip:
            bt(ip[i], path + str(["." if path else ""][0]) + str(i))
bt(ip, "")
print(op)
# Output : [ Adam.1, Alex.Muller.0, Alex.Phil, Lex ]