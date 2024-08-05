n = int(input())
m = int(input())

nums = [i for i in range(1, n + 1)] * (2 * m)
path = []
k = 0

for i in range(0, len(nums), m):
    if i != 0:
        curr_int = nums[i-k:m+(i-k)]
        k += 1
    else:
        curr_int = nums[i:m+i]
        k += 1
    if curr_int[-1] == 1 and i != 0:
        path.append(curr_int)
        break
    else:
        path.append(curr_int)

print(path)

first_elements = [sublist[0] for sublist in path]
result_string = "".join(map(str, first_elements))

print(result_string)


