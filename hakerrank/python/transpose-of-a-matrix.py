matrix = [[1,2,3],
		[23,5,2],
		[3,5,1]]

transposed = []

for i in range(3):
	tran = []
	for row  in matrix:
		tran.append(row[i])
	transposed.append(tran)

print(transposed)