import math
#a=[1,3,4,2,1]

class Solution(object):
    def findDuplicate(self, nums):
        return run(nums)

#runs in nlogn 2T(n/2)+theta(n)
def search(a,s,e):
    if e-s<= 1:
        if(e>=0 and s>=0):
            if(a[e]==a[s] and e!=s):
                return a[s]
        return -1

    m=(int)(math.floor((s+e)/2))
    if(m<e) and (m>s):
        if(a[m-1]==a[m]) or (a[m+1]==a[m]):
            return a[m]
        else:
            b= search(a,s,m)
            c= search(a,m+1,e)
            return b if b!=-1 else c

def run(a):
    a.sort()
    b=search(a,0,len(a)-1)
    return b

#if __name__ == '__main__':
    #print(run(a))
