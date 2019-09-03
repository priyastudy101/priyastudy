def plusone(A):
    for i in range(len(A)-1,-1,-1):
        if A[i] != 9:
           A[i] += 1
           return A
        else:
           A[i] = 0
    A.insert(0,1)
    return A
