#find the top n elements (in terms of rank based on index)
#wrong-doesnot work!
import math
import random
a=[9,8,7,6,5,4]
top = 3

def partition(X,l,r,pivot):
    print('pivot= '+str(X[pivot]))
    insert_index=l
    X[pivot],X[r]=X[r],X[pivot]
    j=l
    while(j<r):
        if(X[j]<X[pivot]):
            X[j],X[insert_index]=X[insert_index],X[j]
            insert_index+=1
        j+=1
    X[r],X[insert_index]=X[insert_index],X[r]
    print(X)
    return insert_index

def topK(X,l,r,k):
    if(l>r):#stop here once we reach end of recursion
        print(l,r)
        print('end')
        return
    pivot=math.floor((l+r)/2)
    insert_index = partition(X,l,r,pivot)
    print(insert_index)
    if(insert_index == k):
        print('found')
    elif insert_index<k:
        topK(X,l,insert_index-1,k)
    else:
        topK(X,insert_index+1,insert_index-k,k)


def run():
    topK(a,0,len(a)-1,top)
if __name__=="__main__":
    run()