# Search algorithms.

# Linear search (sequential search)
#
# Preconditions: none.
#
# Inputs: collection, key
# Output: Index of key within collection, -1 if unsuccessful.
#
# Compares the key with every element in the list until key
# is found and returns the index. The best case is the key 
# being searched for is the first element. The worst is
# the key is not in the list at all, having compared every
# item in the list.
#
# Often is the simplest method to search in unsorted collections.
#
# Worst case O(2n)
# Best case O(2)
# Average case O(n+1)

def sequential(list, key):
    i = 0                   # Set i to 0
    while(i < len(list)):   # Continue list runs out. (n)

        if key == list[i]:  # Check if key is found (n)
            return i        # Break and return index when successful

        i += 1              # Iterate
    return -1               # Return index of -1 when unsuccessful

# Linear search (sequential search) with sentinel.
# 
# Preconditions: none.
#
# Inputs: collection, key
# Output: Index of key within collection, -1 if unsuccessful. 
#
# Same as linear search, although, has a minor optimization that
# reduces the number of comparisons necessary in the iterative 
# loop. Instead of the index comparison stop condition, the
# algorithm continues searching for the key until its found, which
# is appended to the end of the list. 
#
# Often is the simplest method to search in unsorted collections.
#
# Worst case: O(n+1)
# Best case: O(2)
# Average case: O(n+2/2)

def sequential_sentinel(list, key):
    i = 0                   # Set i to 0
    act = len(list)         # Store length of list for return purposes
    list.append(key)        # Add the sentinel to list

    while(key != list[i]):  # Continue until key is found, which is always at end of list. (n)
        i+=1                # Iterate

    if (i < act):           # If element was found within original list return index. (1)
        return i                   
    else: 
        return -1               # Index of -1 since unsuccessful. 

# Binary search.
#
# Preconditions: Collection is sorted.
#
# Input: collection, key
# Output: Index of key within collection, -1 if unsuccessful.
#
# This is an interval search, as opposed to sequential, meaning
# It breaks the list into intervals and acts on smaller subproblems.
# It necessarily requires the list to be sorted, however, it is
# much more efficient with the worst case being O(logn), so
# it plays well with a larger amount of data. 
#
# Worst case: O(logn)
# Best case: O(1)
# Average case: O(logn)

def binary(list, key):
    return binary_recurse(list, 0, len(list)-1, key)

def binary_recurse(list, l, r, key):
    i = (l+r)//2                                        # Set index to midpoint of collection.
    if(l > r):                                          # Exit condition: when collection cannot be split further. Return -1
        return -1                                       
    if(key == list[i]):                                 # Success condition: key found. Return index
        return i
    if(key > list[i]):                                  # Continue condition: determine if key is larger than current element.
        return binary_recurse(list, i+1, r, key)        # If it is discard left half and pass new endpoints of list.
    return binary_recurse(list, l, i-1, key)            # Otherwise, discard right half



