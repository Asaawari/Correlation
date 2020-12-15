import numpy as np
import plotly.express as px
import csv

def getDataSource(dataPath):
    daysPresent = []
    marks = []
    with open(dataPath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            daysPresent.append(float(row["Days Present"]))
            marks.append(float(row["Marks In Percentage"]))
    return {"x":daysPresent,"y":marks}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Days Present vs Marks In Percentage : \n--->", correlation[0,1])

def setup():
    dataPath = "Student Marks vs Days Present.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()