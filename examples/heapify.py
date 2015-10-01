import math
a = [4,1,3,2,16,9,10,14,8,7]
heapsize = len(a)
length = 15
def LEFT(i):
    return (2*i)+1

def RIGHT(i):
    return (2*i)+2

def maxi_heapify(i):
    l = LEFT(i)
    r = RIGHT(i)
    while(l<heapsize):
        l = LEFT(i)
        r = RIGHT(i)
        if l< heapsize and a[l]>a[i] and l!=-1:
            largest =l
        else :
            largest =i
        if r < heapsize and a[r]>a[largest] and r!=-1:
            largest =r
        if largest != i:
            print("New largest ")
            print(largest)
            temp =a[i]
            a[i] = a[largest]
            a[largest] = temp
            i =largest
        else :
            break

# maintains the max and min heap property
def max_heapify(i):
    l = LEFT(i)
    r = RIGHT(i)

    if l< heapsize and a[l]>a[i] and l!=-1:
        largest =l
    else :
        largest =i
    if r < heapsize and a[r]>a[largest] and r!=-1:
        largest =r
    if largest != i:
        print("New largest ")
        print(largest)
        temp =a[i]
        a[i] = a[largest]
        a[largest] = temp
        max_heapify(largest)

def build_max_heap(a):
    i = math.floor(heapsize/2)
    i=i-1
    while(i>=0):
        print(i)
        #max_heapify(i)
        maxi_heapify(i)
        i=i-1

build_max_heap(a)
print(a)















