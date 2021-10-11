import math

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
    list.append(key)        # Add the sentinel to list

    while(key != list[i]):  # Continue until key is found, which is always at end of list. (n)
        i+=1            

    list.pop()

    if (i < len(list)):   # If element was found within original list return index. (1)
        return i                   
    else: 
        return -1           # Index of -1 since unsuccessful. 

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
        return binary_recurse(list, i+1, r, key)        # If it is perform binary search on right half, discarding left.
    return binary_recurse(list, l, i-1, key)            # Otherwise, perform binary search on left half, discarding right.


# Jump search
#
# Precondition: Collection is sorted
#
# Input: collection, key 
# Output: Index of key within collection, -1 if unsuccessful
#
# This is an interval search like the binary search. The 
# principal feature of this algorithm is that it quickly
# moves past data that is far from the key, then refines 
# its search when it gets closer. The algorithm accomplishes
# this by performing a linear search with a step size greater 
# than one and the reduces the step size to one after surpassing
# the key.
# 
# Worst case: O((n/m)+m-1) with step size m.
# Best case: O(1)
# Average case: 

def jump(list, key):
    i = 0
    m = int(math.sqrt(len(list)))                   # The sqrt of n is the optimal step size.

    while(i+m < len(list) and list[i+m] < key):     # Continue steps until we either exceed the length of the list
        i += m                                      # or pass the element we're looking for.

    if(key == list[i]):                             # After breaking from the loop, check the current
        return i

    while(i < len(list) and list[i] < key):
        i += 1

    if(i == len(list)):
        return -1
    return i
        
# Interpolation search
#
# Preconditions: Uniformly spaced, ordered array. 
#
# Input: collection, key
# Output: Index of key in collection, -1 if unsuccessful.
#
# Models collection as a line in the form of y = mx + b, 
# then solves for x. Requires that collection has uniformly
# spaced, ordered values. This implementation underestimates
# the index to account for floating point error, then steps 
# until the key value is exceeded in order to verify the entry
# doesn't exists.
def interpolation(list, key):

    delta = (list[len(list)-1] - list[0]) / (len(list)-1)
    i = int((key - list[0]) // delta)
    
    while(i < len(list)-1 and list[i] < key):
        i += 1
    
    if(list[i] == key):
        return i

    return -1

# Exponential Search
# 
# Preconditions: Collection is sorted.
# 
# Input: Sorted Collection, Key
# Output: Index of key within colletion, -1 if unsuccessful.
# 
# The exponential search is a binary search with this algorithm
# preceding it. The first step finds the bounds of the collection
# for the binary search to act upon by increasing the upper bound
# by powers of 2 until the the target is below the bound. After 
# setting the upper bound, the lower bound is the last tested
# power of two, since it was not found within it. The region
# defined can now be binary searched. This method is ideal for
# unbounded/infinite sorted data. 
#
# Worst Case: O(logn)
# Best Case: O(1)
# Average Case: O(logn)

def exponential(list, key): 
    
    i = 0
    while(2**i < len(list) and list[2**i] < key):
        i += 1

    return binary_recurse(list,min(0,2**(i-1)),min(2**i,len(list)-1),key)
 
    