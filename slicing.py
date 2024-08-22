def slice(obj, slicing_parameter):
	start, stop, step = None, None, None

	if len(slicing_parameter) == 1:
		start = slicing_parameter[0]
	elif len(slicing_parameter) == 2:
		start, stop = slicing_parameter
	elif len(slicing_parameter) == 3:
		start, stop, step = slicing_parameter

	if stop is None:
		stop = len(obj)

	if start < 0:
		start += len(obj)
	if stop < 0:
		stop += len(obj)

	if step is None:
		step = -1 if start > stop else 1

	if stop > len(obj):
		stop = len(obj)

	return helper(obj, start, stop, step)

def helper(obj, start, stop, step):
	ans = []
	for i in range(start, stop, step):
		ans.append(obj[i])
	
	if isinstance(obj, str):
		return "".join(ans)

	return ans

temp = "TanmayRaut"
print(slice(temp , [4]))
print(slice(temp , [2, 8, 2]))
print(slice(temp , [-5]))
print(slice(temp , [-2, 10]))
print(slice(temp , [3, 40]))
print(slice(temp , [-1, -6, 3]))
print(slice(temp , [-1, -6, -3]))
print(slice(temp , [-5, -3]))
print(slice(temp , [4, -9, 3]))
print(slice(temp , [-9, -6, -1]))


