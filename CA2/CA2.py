# Summary:
# the diameter of a tree is just the maximum distance you can traverse along a single continuous path.
# given any node on the tree, find the furthest node from it. Then, if you know the furthest node from that node, 
# that distance will be the diameter.
# a good data structure to keep track of the neighbors for each node is a bucket. we will have n number of buckets
# each containing their adjacent nodes
# start with a node and keep track of its neighbors. then keep going level by level until there is no more neighbors
# that will be the furthest node. do it one more time the other direction and that distance will be the diameter:
# the furthest distance you can travel.


# we'll place the adjacent vertices in the corresponding bucket

# using example: 
# 8
# 1 2
# 3 1
# 4 3
# 1 6
# 7 5
# 5 1
# 4 8
# the returned list will look like: 
# buckets = [
#            [2, 3, 6, 5],
#            [1],
#            [1, 4],
#            [3, 8],
#            [1, 7],
#            [1],
#            [5],
#            [4]
#           ]
def bucketize(n, edges):
    buckets = [[] for _ in range(n)]
    for u, v in edges:
        buckets[u - 1].append(v)
        buckets[v - 1].append(u)
    return buckets

# with the bucketized nodes, start with the first node
# check the babies (nodes below)
# iterate through the babies and make a new list of babies
# once you finally find babies that have no babies themselves
# you have found the furthest node
def compute_diamter(n, edges):
    # Input: `n` - the size of the tree
    # `edges` - a list of pairs of integers denoting ends of edges of the tree
    # Output: An integer - the diameter of the tree
    # Write code to compute the diameter
    
    buckets = bucketize(n,edges)

    babies = [1] # babies are nodes that possible have babies, we'll start by first checking node #1
    #print(f"first baby: {babies}")
    furthest = 1 # we will update furthest each time we descend a level. the node that exists lowest will be finally set as furthest
    visited = set([1]) # visited is a set so we can easily check if we have checked a node already

    while(babies): # as long as there are still babies we keep searching
        newBabies = [] # start with a fresh generation for the next level
        for node in babies: # look through the babies
            for neighbor in buckets[node - 1]: # check the buckets of each node which contain all the neigbors of that specific node.
                if neighbor not in visited: # if we have not already seen that neighbor then it is deeper in the tree and we will check if that neighbor has babies
                    visited.add(neighbor)
                    newBabies.append(neighbor)
                    furthest = neighbor
        babies = newBabies
    #print(furthest)

    # now we have found the first furthest node. now we will repeat the process to find the furthest furthest node
    # we'll count the levels as we descend and that will return the diameter

    babies = [furthest]
    #print(f"new baby: {babies}")
    visited = set([furthest])
    diameter = -1

    while(babies):
        newBabies = []
        for node in babies:
            for neighbor in buckets[node - 1]:
                #print(f"checking node: {neighbor}")
                if neighbor not in visited:
                    visited.add(neighbor)
                    newBabies.append(neighbor)
                    furthest = neighbor
                #print(f"visited: {visited}")
        babies = newBabies
        diameter += 1
    #print(furthest)


    return diameter


T = int(input())
for _ in range(T):
    n = int(input())
    edges = []
    for e in range(n-1):
        u, v  = map(int, input().split(' '))
        edges.append((u, v))
    print(compute_diamter(n, edges))


    
        
