import xlrd
import datetime
import traceback

workbook = xlrd.open_workbook(
    'F:/GitKrakenRepository/CSE_321/CSE_321/Homework3/Part1/Graph_data.xls')
worksheet = workbook.sheet_by_name('Sheet1')

print("First Column", "Second Coulmn")

try:
    index = 0
    rowCount = 0
    graph = {}
    firstColumn = worksheet.cell(index, 0).value
    secondColumn= worksheet.cell(index, 1).value
    
    while worksheet.cell(index, 0).value != None:
        firstColumn = worksheet.cell(index, 0).value
        secondColumn= worksheet.cell(index, 1).value
        if index == 0:
            root_node = secondColumn
        if index >= 3:
            if graph[firstColumn] == None:
                graph[firstColumn] = secondColumn
            elif graph[firstColumn] != None:
                graph[firstColumn] = graph[firstColumn].append(secondColumn)
        rowCount += 1
        index += 1
except Exception as exception:
    for keys, values in graph.items():
        print(keys, values)
