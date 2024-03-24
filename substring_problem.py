def result(l,t):
    new_l = [0]*len(l)
    indices = []
    for i in range(len(l)):
        if i!=0:
            for j in range(i):
                # print(j, new_l[j])
                if new_l[j]+l[i]<=t:
                    new_l[j]+=l[i]
                    if new_l[j]==t:
                        indices.append([j,i])
                else:
                    continue
        new_l[i] = l[i]
        print(new_l)
    print(new_l, indices)
    if len(indices)==0:
        return [-1,1]
    elif len(indices)>1:
        max_v = 0
        max_i = -1
        for i in range(len(indices)):
            v = indices[i][1]-indices[i][0]
            if v>max_v:
                max_v = v
                max_i = i
        return indices[max_i]

    else:
        return indices[0]


l = [4, 3, 5, 7, 8]
t = 12
print(result(l,t))