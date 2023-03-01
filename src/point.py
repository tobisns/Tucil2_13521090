import random
import math

def pointSpace(dimension, amount) :
    pointSpace = []

    for i in range(0, amount):
        point = []

        for j in range(0, dimension):
            point.append(random.uniform(-100,100))

        pointSpace.append(point)

    return pointSpace

def getEuclideanDistance(point1, point2, dimension):
    distance = 0
    for i in range(0, dimension):
        distance += (point1[i]-point2[i])**2

    return distance**0.5


def getStripSpace(pointSpace, middle, d):
    result = []
    for point in pointSpace:
        if abs(point[0] - middle) <= d:
            result.append(point)
            
    return result