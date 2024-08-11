def count(str , sub_str, overlap):
    if overlap:
        cnt = 0
        i = 0
        while True:
            i = str.find(sub_str, i)
            if i == -1:
                break
            cnt += 1
            i += 1
        
    else:
        cnt = 0
        i = 0
        while True:
            i = str.find(sub_str, i)
            if i == -1:
                break
            cnt += 1
            i = i+len(sub_str) 

    return cnt

str = "gggg"
print(count(str , "gg" , True))
