def pattern(n):
    m = n*2
    mid = n 

    # Top of Pyramid
    for i in range(mid):
        for j in range(mid-i):
            print(" ", end = "")

        for j in range(n-i , n+i+1):
            if (j == n-i) or (j == n+i):
                print("+" , end = "")
            else:
                print(" ", end = "")

        print()

    # Middle line 
    for j in range(0 , n*2+1):
        if (j == 0) or (j == n*2):
            print("+" , end = "")
        elif j == n:
            print("*" , end="")
        else:
            print(" ", end = "")

    print()

    # Bottom Pattern 
    for i in range(mid+1 , m):
        for j in range(i-mid):
            print(" ", end="")
        for j in range(i-n, m-(i-n)+1):
            if j == i-n or j == m-(i-n) :
                print("-", end="")
            else:
                print(" ", end="")
        print()
	
    

    for j in range(0 , n*2+1):
        if j == n:
            print("-" , end="")
        else:
            print(" ", end = "")

   



    return ""
    

def print_pattern(len):
	f = str(len)
	if len <= 0:
		return "Enter +ve number"

	if(not(len.is_integer())):
		return "enter +ve integer"
	else:
		pattern(int(len))
		return ""

print(print_pattern(3.0000))


