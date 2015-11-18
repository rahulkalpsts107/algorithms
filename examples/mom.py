a=[2, 3, 5, 4, 1, 12, 11, 13, 16, 7, 8, 6, 10, 9, 17, 15, 19, 20, 18, 23, 21, 22, 25, 24, 14]
top = 3
def select(L, j):
    if len(L) < 10:
        L.sort()
        return L[j]
    S = []
    lIndex = 0
    while lIndex+5 < len(L)-1:
        S.append(L[lIndex:lIndex+5])
        lIndex += 5
    S.append(L[lIndex:])
    print('divide by 5 lists')
    print(S)
    Meds = []
    for subList in S:
        Meds.append(select(subList, int((len(subList)-1)/2)))
    med = select(Meds, int((len(Meds)-1)/2))
    print('medians are')
    print(Meds)
    print('median of median is '+str(med))
    L1 = []
    L2 = []
    L3 = []
    for i in L:
        if i < med:
            L1.append(i)
        elif i > med:
            L3.append(i)
        else:
            L2.append(i)
    print('L1')
    print(L1)
    print('L2')
    print(L2)
    print('L3')
    print(L3)
    if j < len(L1):
        return select(L1, j)
    elif j < len(L2) + len(L1):
        return L2[0]
    else:
        return select(L3, j-len(L1)-len(L2))

def run():
    b=select(a,top+1)
    print(b)
    #print(a)

if __name__=="__main__":
    run()