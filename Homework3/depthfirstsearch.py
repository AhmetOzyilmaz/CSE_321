import xlrd
import traceback
from collections import defaultdict
import collections

graph = {}
def readGraphFromWorksheet():
    workbook = xlrd.open_workbook('Graph_data.xls')
    worksheet = workbook.sheet_by_name('Sheet1')

    rootVertex = int(worksheet.cell(0, 1).value)
    edgelist = []
    for row_index in range(3, worksheet.nrows):
        _from = int(worksheet.row(row_index)[0].value)
        _to = int(worksheet.row(row_index)[1].value)

        if not _from in edgelist: edgelist.append(_from)
        if not _to in edgelist: edgelist.append(_to)

        if _from in graph:
            graph[_from].append(_to)
        else:
            graph[_from] = [_to]
    
    for edge in edgelist:
        print("edge:", edge)
        if not edge in graph:
            graph[edge] = []

    return (rootVertex, graph)


visited_dfs = []

def dfs(graph,node):
    global visited_dfs
    if node not in visited_dfs:
        visited_dfs.append(node)
        for n in graph[node]:
            dfs(graph,n)
    return visited_dfs
    
def breadth_first_search(graph, root):
    visited, queue = [root], collections.deque([root])
    while queue: 
        vertex = queue.popleft()
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.append(neighbour) 
                queue.append(neighbour) 
    return visited

if __name__ == "__main__":
    result = readGraphFromWorksheet()

    print("root vertex:", result[0],"\n")  

    print("Breadth-First Search (BFS) result")
    result = breadth_first_search(graph,1)
    print(result)

    visited_dfs = dfs(graph,1)
    print("Depth-First Search (DFS) result")
    print(visited_dfs)
    pass