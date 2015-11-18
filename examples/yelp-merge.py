import sys
import math
a=[]#contain BIds
b=[]#priority

def ins_sort():
    for j in range(1,len(a)):
        i = j-1
        temp1 = b[j]
        temp = a[j]
        print(str(temp)+" "+str(i))
        while(i>=0 and a[i]>temp ):
            a[i+1]=a[i]
            b[i+1]=b[i]
            i-=1
        i+=1
        a[i]= temp
        b[i]= temp1
        j+=1
    print('insertion')

def merge(array,start,mid,end):
    llen=mid-start+1
    l=[None]*(llen)
    for i in range(0,mid+1):
        l[i]=array[i+start]
    mid=mid+1
    rlen=end-mid+1
    r=[None]*(rlen)
    for i in range(mid,end+1):
        r[i-mid]=array[i]
    i=0
    j=0
    while(1):
        print(i,j)
        if(i>llen-1):
            for k in range(j,rlen):
                array[i+k]=r[k]
            break
        if(j>rlen-1):
            for k in range(i,llen):
                print(array)
                array[j+k]=l[k]
            break
        if l[i] < r[j]:
            array[i] = l[i]
            i+=1
        if r[j] < l[i]:
            array[j] = r[j]
            print(array)
            j+=1


def merge_sort(array,start,end):
    if(end-start <=1):
        array[start],array[end]=array[end],array[start]
    else:
        mid = math.floor((start + end)/2)
        merge_sort(array,start,mid)
        merge_sort(array,mid+1,end)
        merge(array,start,mid,end)

def run():
    for x in range(1,len(sys.argv)):
        if(x%2 == 1):
            b.append(int(sys.argv[x]))
        else:
            a.append(int(sys.argv[x]))
    print(a)
    merge_sort(a,0,len(a)-1)
    print(a)
    #for x in range(1,len(a)):
        #print(str(a[x])+" "+str(b[x]))

if __name__ == '__main__':
    run()
