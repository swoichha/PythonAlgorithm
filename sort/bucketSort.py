# bucket sort algorithm
# theory:
# create an empty array
# iterate through the array
# add the element to the empty array
# sort the empty array
# return the empty array

def bucketSort(arr):
    # create an empty array
    result = []
    # iterate through the array
    for i in range(len(arr)):
        # add the element to the empty array
        result.append(arr[i])
    # sort the empty array
    result.sort()
    # return the empty array
    return result

def main():
    print(bucketSort([1, 3, 5, 7, 2, 4, 6, 8]))
    print(bucketSort([1, 3, 5, 7, 2, 4, 6, 8, 9]))
    print(bucketSort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(bucketSort([1, 2, 3, 4, 5, 6, 7, 8, 9]))

if __name__ == '__main__':
    main()