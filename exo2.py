"""
==========
Partie Python
Exercice 2
==========

"""


# Define the graph 
graph = {
    '7' : ['3','15','16'],
    '3' : ['1','8','7'],
    '1' : ['0','4','3'],
    '8' : ['17','18','3'],
    '15': ['7'],
    '16': ['7'],
    '0' : ['1'],
    '4' : ['1'],
    '17': ['8'],
    '18': ['8'],
}


def find_path(start_node):
    """
    Find the path from a start node

    :param start_node: The starting node for the path
    :return: A list containing the nodes in the order they were visited.
    """
    result = [start_node]
    temp = [start_node]
    while temp:
        node = temp.pop(0)
        for neigh in graph[node]:
            if neigh not in result:
                result.append(neigh)
                temp.append(neigh)
    return result


if __name__ == "__main__":
    start_node = '7'
    print(find_path(start_node))