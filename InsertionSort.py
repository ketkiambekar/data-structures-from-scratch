## Insertion Sort

def insertionSort(arr):
    """
    Iteratively performs Insertion Sort with Average runtime = O (n^2)
    """
    if len(arr)<=1:
        return arr

    #To begin with, sort the first and second elements
    if arr[0]> arr[1]:
        arr[0], arr[1]= arr[1], arr[0]

    print(arr)

    #loop through elements 2 to n for insertion sort
    for i in range(2, len(arr)):
        
        if arr[i]<arr[i-1]:
            #Loop to insert ith element at it's correct position
            for j in range(0, i):
                
                if arr[i] <= arr[j]:
                    
                    temp = arr[i]

                    #insert element in jth position by moving subsequent elements ahead by one position
                    k = i
                    while k-1 >=j:
                        arr[k]=arr[k-1]
                        k-=1
                    arr[j]= temp 
            print(arr)
    

    return arr



def main():
    arr = [39,12,1,44,23,19,21,77,89]

   
    print(insertionSort(arr))

main()


##### OUTPUT ######

# Original Array:
# [39,12,1,44,23,19,21,77,89]

# Insertion Sort Output:
# [12, 39, 1, 44, 23, 19, 21, 77, 89]
# [1, 12, 39, 44, 23, 19, 21, 77, 89]
# [1, 12, 23, 39, 44, 19, 21, 77, 89]
# [1, 12, 19, 23, 39, 44, 21, 77, 89]
# [1, 12, 19, 21, 23, 39, 44, 77, 89]
# [1, 12, 19, 21, 23, 39, 44, 77, 89]