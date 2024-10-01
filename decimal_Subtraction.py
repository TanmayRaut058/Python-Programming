def str_to_int(text):
	text = text.lstrip('0')
	ans = 0
	mul = 1
	
	for i in range(len(text)-1, -1, -1):
		temp = ord(text[i]) - ord('0')
		ans += temp*mul
		mul = mul * 10

	return ans

def decimal_subtraction(num1, num2):
	result = 0
	mul = 1
	n1 = str_to_int(num1)
	n2 = str_to_int(num2)
	if n1 < n2:
		n1,n2 = n2,n1
	
	l = min(len(num1) , len(num2))
	i = -1
	while i >= 0:
		d1 = str_to_int(num1[1])
		d2 = str_to_int(num2[1])	
		print(d1)
		print(d2)
		print(d1-d2)
		result += (d1 - d2)*mul
		mul = mul*10
		i -= 1

	if n1 < n2:
		return -result
	
	return result
	

print(decimal_subtraction('12304' , '102'))