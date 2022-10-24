def mergeSort(arr):
    # theory: divide and conquer
    # divide the array into two halves
    # sort the two halves
    # merge the two halves
    
    # base case
    if len(arr) == 1:
        return arr
    
    # divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # sort the two halves
    left = mergeSort(left)
    right = mergeSort(right)

    # merge the two halves
    return merge(left, right)

def merge(left, right):
    # create an empty array
    # while both left and right have elements
    # compare the first elements of left and right
    # append the smaller element to the empty array
    # remove the element from the array
    
    # create an empty array
    result = []
    
    # while both left and right have elements
    while len(left) > 0 and len(right) > 0:
        # compare the first elements of left and right
        if left[0] < right[0]:
            # append the smaller element to the empty array
            result.append(left[0])
            # remove the element from the array
            left = left[1:]
        else:
            # append the smaller element to the empty array
            result.append(right[0])
            # remove the element from the array
            right = right[1:]
    
    # append the remaining elements of left to the empty array
    result += left
    # append the remaining elements of right to the empty array
    result += right
    
    return result

def main():
    print(mergeSort([1, 3, 5, 7, 2, 4, 6, 8]))
    print(mergeSort([1, 3, 5, 7, 2, 4, 6, 8, 9]))
    print(mergeSort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(mergeSort([1, 2, 3, 4, 5, 6, 7, 8, 9]))

if __name__ == '__main__':
    main()