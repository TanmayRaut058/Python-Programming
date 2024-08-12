def change_case(text, style):
	if style == 'c' or style == 'C':
		return cap(text)	
	elif style == 's' or style == 'S':
		return small(text)
	elif style == 'r' or style == 'R':
		return reverse(text)
	elif style == 'u' or style == 'U':
		return alter(text)
	else:
		return "Enter valid Input"


def cap(text):
	ans = ""
	for i in range(0 , len(text)):
		if ord(text[i]) >= 97:
			ans = ans + chr(ord(text[i])-32) 
		else:
			ans = ans + text[i]

	return ans

def small(text):
	ans = ""
	for i in range(0 , len(text)):
		if (ord(text[i]) >= 65) and (ord(text[i]) <= 90):
			ans = ans + chr(ord(text[i])+32) 
		else:
			ans = ans + text[i]

	return ans

def reverse(text):
	ans = ""
	for i in range(0 , len(text)):
		if ifUp(text[i]):
			ans = ans + chr(ord(text[i])+32) 
		elif ifLow(text[i]):
			ans = ans + chr(ord(text[i])-32) 
		else:
			ans += text[i]

	return ans

def alter(text):
	ans = ""
	flag = True

	j = 0
	while j < len(text)-1:
		if text[j].isalpha():
			break
		j+=1

	if ifLow(text[j]):
		flag = False
		
	for i in range(0 , len(text)):
		if text[i].isalpha():
			if flag:
				if ifLow(text[i]):
					ans += text[i]
				else:
					ans += chr(ord(text[i])+32)
			else:
				if ifUp(text[i]):
					ans += text[i]
				else:
					ans += chr(ord(text[i])-32)
			flag = not flag
		else:
			ans += text[i]
	return ans

def ifLow(c):
	if (ord(c) >= 97) and (ord(c) <= 122):
		return True
	return False

def ifUp(c):
	if (ord(c) >= 65) and (ord(c) <= 90):
		return True
	return False


print(change_case("*-+&&&543###" , 'u'))


