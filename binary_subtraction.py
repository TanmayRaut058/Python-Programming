def binary_subtraction(num1, num2):
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    num2_one_comp = ones_complement(num2)
    num2_two_comp = binary_addition(num2_one_comp, '1')
    res = binary_addition(num1, num2_two_comp)

    if len(res) > max_len:  
        res = res[1:]  
    else:
        res = binary_addition(ones_complement(res), '1')
        res = '-' + res

    res = res.lstrip('0')
    return res if res else '0'

def binary_addition(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    ans = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
        bitSum = carry
        bitSum += 1 if a[i] == '1' else 0
        bitSum += 1 if b[i] == '1' else 0
        ans = ('1' if bitSum % 2 == 1 else '0') + ans
        carry = 0 if bitSum < 2 else 1

    if carry:
        ans = '1' + ans

    return ans

def ones_complement(binary):
    temp = ''
    for bit in binary:
        temp += '1' if bit == '0' else '0'
    return temp

print(binary_subtraction("01", "1111")) 
