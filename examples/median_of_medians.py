a= [25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

def split(array):
    lists={}
    counter=0
    i=0
    begin=0
    limit=0
    while(counter<5):
        begin=limit
        limit=limit+4
        for b in range(begin,limit+1):
            if(counter in lists):
                lists[counter].update({array[i]})
            else:
                lists[counter]={array[i]}
            b+=1
            i+=1
        limit+=1
        counter+=1
    return lists

def run(arr,k):
    split_array = split(arr)
    medians=[]
    for i in split_array:
        ai={}
        ai=list(split_array[i])
        ai.sort()
        medians.append(ai[2])
    print(medians)

if __name__ =='__main__':
    run(a,10)