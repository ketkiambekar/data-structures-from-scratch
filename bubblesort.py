def bubble_sort(arr):
    l=len(arr)

    #print the initial array
    print(arr)

    #bubble sort loops
    for i in range(l):
        for j in range(l-1):

            #swap adjacent elements if they are unsorted
            if arr[j]>arr[j+1] :
                arr[j],arr[j+1]=arr[j+1],arr[j]
                print(arr)
    return arr


if __name__=="__main__":
    arr = [5,4,3,2,1]
    bubble_sort(arr)


