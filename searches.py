# Search algorithms.

# Linear search (sequential search)
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
# Inputs: collection, key
# Output: Index of key within collection, -1 if unsuccessful. 
#
# Same as linear search, although, has a minor optimization that
# reduces the number of comparisons necessary in the iterative 
# loop. Instead of the index comparison stop condition, the
# algorithm continues searching for the key until its found, which
# is appended to the end of the list. 
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

