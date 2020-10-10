import os

def get_all_files(dir):
	files = []
	all_files = os.listdir(dir)
	for entry in all_files:
		full_path = os.path.join(dir, entry)
		if os.path.isdir(entry):
			files += get_all_files(full_path)
		else:
			files.append(full_path)
	return files


dir = "."
x = get_all_files(dir)
print(x)