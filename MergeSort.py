def mergeSort(arr):
    """
    Function to perform mergeSort recursively.
    """

    if len(arr)<=1: #terminating condition
        return arr
    else:
        mid = len(arr)//2
        Left = mergeSort(arr[:mid])
        Right = mergeSort(arr[mid:])

        return merge(Left, Right)


def merge(Left, Right):
    """
    Function to merge two arrays in non decreasing order
    """
    
    mergedArray=[]
    i=j=0

    while i < len(Left) and j< len(Right):
        if Left[i]<= Right[j]:
            mergedArray.append(Left[i])
            i+=1
        else:
            mergedArray.append(Right[j])
            j+=1
    
    #Append the remaining Array
    if j < len(Right):
        mergedArray+=Right[j:]
    
    if i < len(Left):
        mergedArray+=Left[i:]

    return mergedArray


def main():
    arr=[2,77,3,25,12,44,87,32,11]

    print(mergeSort(arr))

    print(mergeSort([0]))
    
    print(mergeSort([]))
    
    print(mergeSort([2,1]))

main()


######### OUTPUT ########

# [2, 3, 11, 12, 25, 32, 44, 77, 87]