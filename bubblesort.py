
import numpy as np

arr = np.arange()

def bubble_sort(arr):
    l=len(arr)

    #print the initial array
    print(arr)

    #bubble sort loops
    for i in range(l-1):
        for j in range(l-i-1):

            #swap adjacent elements if they are unsorted
            if arr[j]>arr[j+1] :
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print(arr)
    return arr


if __name__=="__main__":
    arr = [5,4,3,2,1]
    bubble_sort(arr)


##############Output##############
#   [5, 4, 3, 2, 1]
#   [4, 5, 3, 2, 1]
#   [4, 3, 5, 2, 1]
#   [4, 3, 2, 5, 1]
#   [4, 3, 2, 1, 5]
#   [3, 4, 2, 1, 5]
#   [3, 2, 4, 1, 5]
#   [3, 2, 1, 4, 5]
#   [2, 3, 1, 4, 5]
#   [2, 1, 3, 4, 5]
#   [1, 2, 3, 4, 5]


>>>>>>> 47fb5dd8b93b179590926214b9938cf35452105a
