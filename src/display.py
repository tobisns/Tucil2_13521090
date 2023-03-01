import matplotlib.pyplot as plt
from typing import List


def plot_3d(listOfPoints, Point1, Point2) :
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')


    for point in listOfPoints:
        if (all(a1==a2 for a1, a2 in zip(point, Point1)) or all(a1==a2 for a1, a2 in zip(point, Point2))):
            color = '#FF0000'
        else:
            color = '#000000'
        ax.scatter(point[0], point[1], point[2], marker='o', c=color)


    plt.show()