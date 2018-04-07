A = [7,17,25,13,26,5,6,7,8,12]

while not(max(A) == A[len(A)-1] and min(A) == A[0]):
    for x in range(len(A)-1):
        item_1 = A[x]
        item_2 = A[x+1]

        if A[x]>A[x+1]:
            A[x]=item_2
            A[x+1]=item_1
        else:
            A[x]=item_1
            A[x+1]=item_2

print(A)
