
def myAtoi( s: str) -> int:
    result = 0
    sign = "+"
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    if s == "":
        return 0
    print(len(s))
    for i in range(len(s)):
        if s[i]!= " ":
            break
    

    if i==len(s)-1:
        return 0
    
    if s[i] ==  "-" or s[i]=="+":
        sign = s[i]
        i = i+1
        
    
    for j in range(i, len(s)):
        if s[j] in numbers:
            result = result*10 + int(s[j])
        else:
            break

    
    if sign == "-":
        result = -result
    
    if result>2**31-1:
        result = 2**31 -1
    elif result < -2**31:
        result = -2**31
    
    return result
    
myAtoi("        ")