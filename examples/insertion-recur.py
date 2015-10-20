#insertion-sort-recur
a = [9,8,7,6,5,4]

def swap(i,j):
    print(i,j)
    if(i >= 0):
        print(a[i],a[j])
        if(a[i] > a[j]):
            a[j] = a[i]
        swap(i-1,j)


def main():
    for j in range(1,len(a)):
        key = a[j]
        swap(j-1,j)

        print(a)
    print(a)

if __name__ == '__main__':
    main()