'''Analyzes data for the hierarchical model study.'''

import math
from collector import *

def readData(ID):
    '''Loads the data for one test subject into memory. Returns a dataPoints
    object.'''
    filename = 'test' + str(ID)
    f = open(filename, 'r')
    data = []
    # Each test subject responded 60 times.
    for i in range(60):
        prompt = f.readline()
        number = int(f.readline())
        reactionTime = float(f.readline())
        truth = int(f.readline())
        correct = int(f.readline())
        distance = int(f.readline())
        f.readline()
        data.append(dataPoint(prompt, number, reactionTime, truth, correct,
                              distance))
    return dataPoints(ID, data)

def readAllData(maxID):
    '''Loads all data into memory.'''
    global allData
    allData = []
    for ID in range(1, maxID + 1):
        allData.append(readData(ID))

def analyze(numberList=[1, 2, 3, 4], truthList=[0, 1],
             correctList=[0, 1], distanceList=[0, 1, 2, 3]):
    '''Looks at all the data points and filters them according to their 
    characteristics. Returns the average of the relevant response times.'''
    sumTimes = 0.0
    sumTimesSquared = 0.0
    numTimes = 0
    for dataPoints in allData:
        data = dataPoints.getData()
        for dataPoint in data:
            (prompt, number, time, truth, correct, distance) = \
                dataPoint.getInfo()
            if (number in numberList) and\
               (truth in truthList) and\
               (correct in correctList) and\
               (distance in distanceList) and\
               time > 0.05:
                sumTimes += time
                sumTimesSquared += time ** 2
                numTimes += 1
    average = sumTimes / numTimes
    averageSquare = sumTimesSquared / numTimes
    standardDeviation = math.sqrt(averageSquare - (average ** 2))
    return (numTimes, average, standardDeviation)

def saveBasicInfo():
    '''Saves same basic statistics to a text file.'''
    f = open('results.txt', 'w')
    f.write("All responses with time > 0.05\n")
    for distance in range(4):
        f.write("Distance " + str(distance) + ": ")
        num = analyze(distanceList=[distance])
        f.write(str(num) + "\n")
    f.write("\n")
    f.write("Only correct responses with time > 0.05\n")
    for distance in range(4):
        f.write("Distance " + str(distance) + ": ")
        num = analyze(correctList=[1], distanceList=[distance])
        f.write(str(num) + "\n")
    f.close()