def rom(text, text_base):
    num = int(text, text_base)

    ones = ['','I','II','III','IV','V','VI','VII','VIII','IX']
    tens = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    hundred = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    thousand = ['','M','MM', 'MMM']
    
    return '' + thousand[int(num/1000)] + hundred[int((num%1000)/100)] + tens[int((num%100)/10)] + ones[int(num%10)]


print(rom("20", 10))