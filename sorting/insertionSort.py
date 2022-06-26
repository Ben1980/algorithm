# Insertio-Sort is sorting a set A by selecting an element j of set A and adding
# it to a second sorted set at the correct position.
# Computational Complexity: O(n^2)

def InsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1

        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
