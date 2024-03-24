l = [1, 1, 1]

def lucky_triples(l):
    if len(l)<=2:
        return 0
    divides = [0]*len(l)
    count = 0
    for i in range(len(l)):
        divides[i] = []
        for j in range(0,i):
            if l[i]%l[j]==0:
                divides[i].append(j)
                if len(divides[i])>0:
                    if divides[i][-1]!=0 and len(divides[divides[i][-1]])>0:
                        print('counting', divides)
                        count+=1
    

    print('divides', divides, count)

lucky_triples(l)