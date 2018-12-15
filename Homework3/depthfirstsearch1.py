import xlrd
import traceback
from collections import defaultdict

workbook = xlrd.open_workbook(
    'F:/GitKrakenRepository/CSE_321/CSE_321/Homework3/Part1/Graph_data.xls')
worksheet = workbook.sheet_by_name('Sheet1')

print("First Column", "Second Coulmn")

try:
    index = 3
    rowCount = 0
    graph = {}
    firstColumn = worksheet.cell(index, 0).value
    secondColumn= worksheet.cell(index, 1).value
    
    while worksheet.cell(index, 0).value != None:
        firstColumn = worksheet.cell(index, 0).value
        secondColumn= worksheet.cell(index, 1).value
        if graph[firstColumn] == None:
            graph[firstColumn].add(secondColumn)
        elif graph[firstColumn] != None:
            tempList = list()
            tempList.append(graph[firstColumn])
            tempList.append(secondColumn)                
            graph[firstColumn] = tempList
        print (index)        
        rowCount += 1
        index += 1
except Exception as exception:
    print(exception)
    for keys, values in graph.items():
        print(keys, values)