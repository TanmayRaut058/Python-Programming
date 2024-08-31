def base(text, text_base, output_base):
    base10 = int(text, text_base)

    if output_base == 'r' or output_base == 'R':
        return rom(text, text_base)

    if output_base == 10:
        return str(base10)


    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    ans = ""
    while base10 > 0:
        rem = base10 % output_base
        d = digits[rem]
        ans = d + ans
        base10 = int(base10 / output_base)


    return ans 

def rom(text, text_base):
    num = int(text, text_base)

    ones = ['','I','II','III','IV','V','VI','VII','VIII','IX']
    tens = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    hundred = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    thousand = ['','M','MM', 'MMM']
    
    return '' + thousand[int(num/1000)] + hundred[int((num%1000)/100)] + tens[int((num%100)/10)] + ones[int(num%10)]


print(base('100', 2, 5))
print(base('ABF', 16, 4))
print(base('524', 8, 'r'))
print(base('014', 8, 2))
print(base('AC4', 16, 10))