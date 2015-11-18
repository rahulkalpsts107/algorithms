a=[90,70,60,80,100]
def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[0:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        print(x,max_so_far)
    return max_so_far
print(max_subarray(a))
