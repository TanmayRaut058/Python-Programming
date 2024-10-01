def get_odd_even_count(l):
	even_count = 0; odd_count = 0
	for n in l:
		even_count += n%2 == 0
		odd_count += n%2 != 0

	return odd_count, even_count

l = [1,2,3,4,5,6,7,8,9]
print(get_odd_even_count(l))