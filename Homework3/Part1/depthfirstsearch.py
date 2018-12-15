import xlrd
import datetime
import traceback
from collections import defaultdict


visited_dfs = [] 
visited_bfs = [] 

graph = {}
def readGraphFromWorksheet():
    workbook = xlrd.open_workbook('F:/GitKrakenRepository/CSE_321/CSE_321/Homework3/Part1/Graph_data.xls')
    worksheet = workbook.sheet_by_name('Sheet1')

    rootVertex = int(worksheet.cell(0, 1).value)
    print("root vertex:", rootVertex,"\n")

    for row_index in range(3, worksheet.nrows):
        _from = int(worksheet.row(row_index)[0].value)
        _to = int(worksheet.row(row_index)[1].value)
        if _from in graph:
            graph[_from].append(_to)
        else:
            graph[_from] = [_to]
    
    return (rootVertex, graph)

def dfs(graph,node):    
    if node not in visited_dfs:
        visited_dfs.append(node)
        for n in graph[node]:
            dfs(graph,n)
    return visited_dfs
    
def bfs(graph, start):
    visited_bfs, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited_bfs:
            visited_bfs.add(vertex)
            queue.extend(graph[vertex] - visited_bfs)
    return visited_bfs
    
if __name__ == "__main__":
    result = readGraphFromWorksheet()
    try:
        visited = dfs(graph,4)
    except Exception as exception:
        print("Depth-First Search (DFS) result")
        print(visited_dfs)   
        print("Breadth-First Search (BFS) result")
        print(visited_bfs)
        print(readGraphFromWorksheet())
    pass