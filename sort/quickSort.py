# quick sort algorithm
# theory:
# pick a pivot
# create two empty arrays
# iterate through the array
# if the element is less than the pivot, add it to the first array
# if the element is greater than the pivot, add it to the second array
# recursively call quick sort on the first array
# recursively call quick sort on the second array
# concatenate the first array, the pivot, and the second array

def quickSort(arr):
    # base case
    if len(arr) < 2:
        return arr

    # pick a pivot
    pivot = arr[0]

    # create two empty arrays
    less = []
    greater = []

    # iterate through the array
    for i in range(1, len(arr)):
        # if the element is less than the pivot, add it to the first array
        if arr[i] < pivot:
            less.append(arr[i])
        # if the element is greater than the pivot, add it to the second array
        else:
            greater.append(arr[i])

    # recursively call quick sort on the first array
    less = quickSort(less)
    # recursively call quick sort on the second array
    greater = quickSort(greater)

    # concatenate the first array, the pivot, and the second array
    return less + [pivot] + greater

def main():
    print(quickSort([1, 3, 5, 7, 2, 4, 6, 8]))
    print(quickSort([1, 3, 5, 7, 2, 4, 6, 8, 9]))
    print(quickSort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(quickSort([1, 2, 3, 4, 5, 6, 7, 8, 9]))

if __name__ == '__main__':
    main()