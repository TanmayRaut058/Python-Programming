import time

def ss(l):
	first_min = float('inf')
	sec_min = first_min

	for n in l:
		if n < first_min:
			sec_min = first_min
			first_min = n
		elif n > first_min and n < sec_min:
			sec_min = n
		else : pass
	return sec_min

def sl(l):
	first_max = float('-inf')
	sec_max = first_max

	for n in l:
		if n > first_max:
			sec_max = first_max
			first_max = n
		elif n < first_max and n > sec_max:
			sec_max = n
		else: pass
	return sec_max

def get_list(l):
	arr = []
	for object in l:
		if isinstance(object, int):
			arr.append(object)
		elif isinstance(object, (list, tuple, set)):
			arr.extend(get_list(object))
		elif isinstance(object, dict):
			val_list = list(object.values())
			key_list = list(object.keys())
			arr.extend(get_list(key_list))
			arr.extend(get_list(val_list))
		elif isinstance(object, str):
			pass

	return arr

def get_sl_ss(l):	
	arr = get_list(l)
	return sl(arr) , ss(arr)


l = [
    4, 52, 
    [17, '-45', 8, '123', 6, 9, [12, -34, '100'], {1, 2, 3, 'abc'}, [-9, 'xyz']], 
    7, 
    {5, '70', 3, 1}, 
    'tan', 'a', 
    4, [-4, -5, -10], 
    {'a': 1, 'b': -6, 45: -100, 99: 7}, 
    (8, 5, [-50, 120, 'abcd', {1, 2, 3}], 6), 
    {10, 'abc', -1}, 
    [{'nested_list': [100, '200', -300, 400]}, (-200, 300)], 
    (101, [201, -301, '401', (501, -601)], 701), 
    111, -11, 
    {'invalid_key': 'string', -999: 'test', 500: 100, 'another_invalid_key': -500}, 
    [[[-1, -2, -3], [4, 5, 6], {'set1', 7, 8}], (9, 10, 11)], 
    [1, 2, 'bad_entry', [3, 'nested_str', [-4, 5, [-6, 'deep_str']]]]
]
# l=[1,1,2,2]

s = time.time()
print(get_sl_ss(l))
e = time.time()
print(e-s)






