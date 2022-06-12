#program to Binary Search

def binary_search(array,target):
    #takes sorted array as input and finds index of target value
    length = len(arr)
    mid = length//2

    while(True):

        if target==array[mid]:
            return mid

        elif target>array[mid]:
            mid = (mid+length)//2

        elif target<array[mid]:
            mid = (0+mid)//2

