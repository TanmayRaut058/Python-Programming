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

