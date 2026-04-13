# n = number of nodes
# d = distance
# a = sorted list of node locations
n, d = map(int, input().split())
a = list(map(int, input().split()))

# given two locations, are they in range?

def in_range(loc1, loc2, d):
    if abs(loc1 - loc2) <= d:
        return True
    else:
        return False

# given a specific node, find how many nodes are within distance d of it?
# calculate the total range [node location - d, node location + d]
# then check how many nodes are within that range

def brute_force(n, d, a):
    for node in a:
        count = 0
        for other_node in a:
            if in_range(node, other_node, d):
                count += 1
        print(count)

# This is a brute-force solution
# somehow we must use binary search to find the range of nodes within distance d more efficiently.

# for optimized solution we will use binary search to find the furthers node still in the range
# Then the number of nodes is simply the difference in indices
# we will use two binary searches to find the left and the right cases

def optimized_solution(n, d, a):
    # check to the left of the current node
    for i in range(0,n):
        #print(f"\ni: {i} a[i]: {a[i]}")
        # binary search to find the furthest left index still in range
        left = 0
        right = i

        while(left < right):
            mid = (left + right)//2

            if a[mid] >= a[i] - d:
                right = mid
            else:
                left = mid+1

        left_index = left
        #print(f"left index: {left_index}")
        # binary search to find the right furthest index in range

        left = i
        right = n - 1
        while(left < right):
            mid = -(-(left + right)//2)

            if a[mid] <= a[i] + d:
                left = mid
            else:
                right = mid - 1
        
        right_index = right
        #print(f"right index: {right_index}")
        print(right_index - left_index + 1)

optimized_solution(n, d, a)

def optimal_placement(n, d, a):
    # the number of nodes only changes once you move the range over the next node.
    # so we really only care about whether the ends are touching a node
    # every possible best solution is one that can also be reached by at least one edge touching a node
    # start the search a[0] + d and end the search a[n-1] - d. Thats the range of the possible placements
    # count the number of nodes at the start and just keep track of how many lost and gained
    # when the count reaches a new high, record the location and the count.

    
    
    return