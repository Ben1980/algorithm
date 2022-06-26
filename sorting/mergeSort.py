# Merge-Sort is sorting a set A by recursivly dividing the set into subsets until one of the subsets has length 1.
# Then Merge-Sort is comparing the subsets and merges them together
#           [3 4 2 6 8 7 9 1]
#         [3 4 2 6]   [8 7 9 1]
#       [3 4] [2 6]   [8 7] [9 1]
#   [3] [4] [2] [6]   [8] [7]  [9] [1]
#       [3 4] [2 6]   [7 8] [1 9]
#         [2 3 4 6]   [1 7 8 9]
#           [1 2 3 4 6 7 8 9]
# Computational Complexity: O(n log n)

def MergeSort(A):
    if len(A) > 1:
        mid = len(A)//2
        L = A[:mid]
        R = A[mid:]

        MergeSort(L)
        MergeSort(R)
        _Merge(A, L, R)

def _Merge(A, L, R):
    i = 0
    j = 0
    k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1




def _MergeSort(A, p, r):
    if p < r:
        q = int(0.5 * (p + r))
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        _Merge(A, p, q, r)

def __Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = []
    R = []

    print(n1)
    print(n2)

    for i in range(n1):
        L.append(A[p + i - 1])
    for i in range(n2):
        R.append(A[q + 1 - 1])

    i = 0
    j = 0
    for k in range(p-1, r):
        print(i, j)
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1