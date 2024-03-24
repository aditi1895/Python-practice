print(0^1^2^3^4^6)
print(5^7)

def answer(start, length):
    answer_v = -1
    counter = length+1
    for i in range(length):
        k = 0
        for j in range(start, start+length):
            k+=1
            if k<counter:
                # print(i,j,k, counter)
                if answer_v==-1:
                    answer_v = j
                else:
                    # print(answer_v, j)
                    answer_v = answer_v ^ j
        start = start+length
        counter-=1
    return answer_v


print(answer(17,4))