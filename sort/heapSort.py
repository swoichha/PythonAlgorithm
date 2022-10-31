# heapsort algorithm in python
# theory: 
# create a max heap
# swap the first element with the last element
# remove the last element from the heap
# heapify the heap
# repeat until the heap is empty


def heapify(arr, n, i):
    # find the largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # if root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # build max heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # swap the root of the max heap with the last element of the heap
    # remove the last element from the heap
    # heapify the root of the tree
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

def main():
    print(heapSort([1, 3, 5, 7, 2, 4, 6, 8]))
    print(heapSort([1, 3, 5, 7, 2, 4, 6, 8, 9]))
    print(heapSort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(heapSort([1, 2, 3, 4, 5, 6, 7, 8, 9]))

if __name__ == '__main__':
    main()