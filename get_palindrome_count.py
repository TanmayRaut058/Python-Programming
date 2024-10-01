import time as t

def fun1(L):
	count = 0
	
	for object in L:
		if isinstance(object, str):
			if len(object)%5 == 3:
				temp = object[::-1]
				if temp == object:
					count += 1
		elif isinstance(object, int):
			temp = str(object)
			count += fun1([temp])
		elif isinstance(object, set) or isinstance(object, list) or isinstance(object, tuple):
			count += fun1(object)
		else:
			pass

	return count

def isPalindrome(s) :
    return s == s[ : : -1]

def fun2(l) :
    count = 0
    for object in l:
        if isinstance(object, str) and len(object) % 5 == 3:
            count += isPalindrome(object)
        elif isinstance(object, int) :
            temp = str(object)
            if len(temp) % 5 == 3:
                count += isPalindrome(temp)
        elif isinstance(object, (list, tuple, set)):
            count += fun2(object)
    return count

def fun3(l) :
    count = 0
    for object in l:
        count += type(object) == str and len(object) % 5 == 3 and isPalindrome(object)
        if isinstance(object, int):
            temp = str(object)
            count += len(temp) % 5 == 3 and isPalindrome(temp)
        elif isinstance(object, (list, tuple, set)):
            count += fun3(object)
    return count

def fun4(l) :
    count = 0
    for object in l:
        count += type(object) == str and len(object) % 5 == 3 and object == object[ : : -1]
        if isinstance(object, int):
            temp = str(object)
            count += len(temp) % 5 == 3 and temp == temp[ : : -1]
        elif isinstance(object, (list, tuple, set)):
            count += fun4(object)
    return count



l = [
    ["racecar", "level", "1234321", "78987", "abcdefedcba", "11111111111", "abcde"],  # Strings, including some palindromes with len % 5 == 3
    (121, 451154, 78987, 12321, 111122111),  # Integers, some palindromic
    [
        "aaaaaaaaa", "xyzzyx", "aba", "12321", "abcdefg", "xyyx",  # More strings
        [55555, 7777777, 88888888, "xyzyx"],  # Nested lists of ints and strings
        (
            "11211", "99999999", "87654345678", "123321123",  # Nested tuple with palindromes
            [13531, "xyzxyzxyz", "abcdefgfgfedcba", (121, "zzzzz", "abcdedcba")],  # Deeply nested list/tuple
            {1234321, "noon", "fizzbuzz", "98789", "naman", "6543456"}  # Nested set
        )
    ],
    {111222111, "tacocat", 543212345, "levelup", 1221, "lol", "madam"}  # Top-level set
]

start1 = t.time()
print(start1)
print(fun1(l))
end1 = t.time()
print(end1)

start2 = t.time()
print(start2)
print(fun2(l))
end2 = t.time()
print(end2)

start3 = t.time()
print(start3)
print(fun3(l))
end3 = t.time()
print(end3)

start4 = t.time()
print(start4)
print(fun4(l))
end4 = t.time()
print(end4)

