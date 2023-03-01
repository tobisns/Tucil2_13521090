import point
import sort

def findNearestPairBF(pointSpace, dimension) :
    countProcess = 0
    point1 = pointSpace[0]
    point2 = pointSpace[1]

    distance = point.getEuclideanDistance(point1, point2, dimension)

    for i in range(0, len(pointSpace)) :
        for j in range(i+1, len(pointSpace)) :
            newDistance = point.getEuclideanDistance(pointSpace[i], pointSpace[j], dimension)
            if (newDistance < distance) :
                point1 = pointSpace[i]
                point2 = pointSpace[j]

                distance = newDistance
                
            countProcess+=1


    return distance, point1, point2, countProcess

def findNearestPairDNC(pointSpace, dimension) :
    
    
    if(len(pointSpace) > 3) :

        distance = 0
        point1 = []
        point2 = []
        countProcess = 0
        pointSpace = sort.sort(pointSpace)

        mid = len(pointSpace) // 2

        leftHalf = pointSpace[0:mid]
        rightHalf = pointSpace[mid:]

        distancel, point1l, point2l, countProcessl = findNearestPairDNC(leftHalf, dimension)
        distancer, point1r, point2r, countProcessr = findNearestPairDNC(rightHalf, dimension)

        countProcess+=countProcessl+countProcessr

        d = point.getEuclideanDistance(leftHalf[-1], rightHalf[0], dimension)

        if(distancel > distancer) :
            distance = distancer
            point1 = point1r
            point2 = point2r
        else :
            distance = distancel
            point1 = point1l
            point2 = point2l

        if(distance > d) :
            middle = leftHalf[-1][0] + rightHalf[0][0]
            middle /= 2
            stripSpace = point.getStripSpace(pointSpace, middle, d)
            
            distance, point1, point2, countProcesst = findNearestPairBF(stripSpace, dimension)

            # print(point2,3)
            return distance, point1, point2, countProcess+countProcesst
        else :
            # print(point2,2)
            return distance, point1, point2, countProcess
    else :
        # print(point2,1)
        return findNearestPairBF(pointSpace, dimension)


if __name__ == "__main__" :
    a = point.pointSpace(3, 16)
    print(findNearestPairBF(a, 3))
    print(findNearestPairDNC(a, 3))