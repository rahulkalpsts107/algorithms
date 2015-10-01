#selection sort
a=[9,8,7,6,5,4]

for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[j] <= a[i]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
print(a)