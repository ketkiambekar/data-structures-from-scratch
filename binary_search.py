# In a nutshell, this search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison. 

# Compare x with the middle element.
# If x matches with the middle element, we return the mid index.
# Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
# Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.

def main():
    arr = [5,1,2,9,3,4,54,12,43,65,76,34]
    arr.sort()

    print(binary_search_recursive(arr, 4))
    print(binary_search_recursive(arr, 34))
    print(binary_search_recursive(arr, 19))

def binary_search_recursive(arr=[], x=0):
    '''
    Args: x: an element in to be searched in arr
    '''
    #Terminal condition
    l =len(arr)
    if l in (0,1):
        return False

    
    #recursive call
    mid = l//2
    if x==arr[mid]:
        return True
    elif x> arr[mid]:
        return binary_search_recursive(arr[mid:], x)
    else:
        return binary_search_recursive(arr[:mid], x)


    
if __name__=="__main__":
    main()