import numpy as np
import plotly.express as px
import csv

def getDataSource(dataPath):
    coffee = []
    sleep = []
    with open(dataPath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return {"x":coffee,"y":sleep}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Cups of coffee in ml vs Hours of sleep : \n--->", correlation[0,1])

def setup():
    dataPath = "cups of coffee vs hours of sleep.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

setup()