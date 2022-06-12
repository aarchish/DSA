"""
Code to run Linear Search on an Array/List
"""

def linear_search(list,target):

    if len(list)<=1:
        return list

    else:
        index = 0
        for item in list:
            if item == target:
                return index
            else:
                index += 1
