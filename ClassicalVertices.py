#Write here your graph
K4 = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]] #example

graph = K4
max_node = 5 #Maximum node assignment
dimension = 6 #Number of edges of the graph
cycles = []
classical_assignments = 0

#Return all cycles for a given graph
def get_cycles(graph):
    cycles = []
    for edge in graph:
        for node in edge:
            findNewCycles([node], graph, cycles)
    return cycles
#Finding cycles 
#Subrouting found in stackoverflow
def findNewCycles(path, graph, cycles):
    start_node = path[0]
    next_node= None
    sub = []

    #visit each edge and each node of each edge
    for edge in graph:
        node1, node2 = edge
        if start_node in edge:
                if node1 == start_node:
                    next_node = node2
                else:
                    next_node = node1
                if not visited(next_node, path):
                        # neighbor node not on path yet
                        sub = [next_node]
                        sub.extend(path)
                        # explore extended path
                        findNewCycles(sub, graph, cycles);
                elif len(path) > 2  and next_node == path[-1]:
                        # cycle found
                        p = rotate_to_smallest(path);
                        inv = invert(p)
                        if not any(sorted(p) == sorted(c) for c in cycles):
                            cycles.append(p)


def invert(path):
    return rotate_to_smallest(path[::-1])

def rotate_to_smallest(path):
    n = path.index(min(path))
    return path[n:]+path[:n]

def isNew(path):
    return not path in cycles

def visited(node, path):
    return node in path

# Check if an assignment is classical or not
# Checks if there is a single 0 assignment in a given cycle
def check_assignment(overlap, cycles):
    for cy in cycles:
        path = [str(node) for node in cy]
        number_zeros = 0
        cycle_len = len(path)
        for k in range(0, cycle_len):
            if overlap[int(path[k]), int(path[(k+1)%cycle_len])] == '0':
                number_zeros += 1
        if number_zeros == 1:
            return False
    return True

def main():
    import numpy as np
    #Create an overlap matrix
    overlap = np.zeros((2*dimension, 2*dimension), dtype='<U1')
    cycles = get_cycles(graph)
    
    for i in range(0, 2**dimension):
        #Create all assignments possible
        assignment = bin(i)[2:].zfill(dimension)
        count = 0
        #Write the overlaps in terms of the assignments
        for edge in graph:
            for u in edge:
                for v in edge:
                    if v != u:
                        overlap[u,v] = assignment[count]
                        overlap[v,u] = assignment[count]
            count += 1
        #Check if is a classical assignment
        if check_assignment(overlap, cycles):
            global classical_assignments
            classical_assignments += 1
            result = " ".join(assignment)
            print(f'({classical_assignments}) {result}')

main()
