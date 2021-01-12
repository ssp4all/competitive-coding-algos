sep = " "
arr = [sep] + list("myself love my life") + [sep]
indexes = [i for i in range(len(arr)) if arr[i] == sep]
print(indexes)

def reverse(arr, st, end):
    while st < end:
        arr[st], arr[end] = arr[end], arr[st]
        st += 1
        end -= 1

start = indexes[0]
print(arr)
for end in indexes[1:]:
    reverse(arr, start + 1, end - 1)
    start = end

print("".join(arr[1:-1]))