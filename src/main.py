import solver
import point

class DimensionError(Exception):
    "raised when dimension lower than one.\n"
    pass

class AmountError(Exception):
    "raised when amount lower than one.\n"
    pass

print("selamat datang pada program mencari jarak terdekat...\n")
dimension = -1
while True:
    try:
        dimension = int(input("silahkan menentukan banyak dimensi ruang titik : \n"))
        if(dimension < 1):
            raise DimensionError
        break
    except ValueError:
        print("Invalid number")
    except DimensionError:
        print("not enough dimension to find shortest distance!")


amount = -1
while True:
    try:
        amount = int(input("tentukan banyak titik pada ruang : \n"))
        if(amount < 2):
            raise AmountError
        break
    except ValueError:
        print("Invalid number")
    except AmountError:
        print("this much points won't make a line!")

print("input recoreded. . .\n")
print("processing . . .\n")

space = point.pointSpace(dimension, amount)

minDistanceBF, p1BF, p2BF, countProcBF = solver.findNearestPairBF(space, dimension)
minDistanceDNC, p1DNC, p2DNC, countProcDNC = solver.findNearestPairDNC(space, dimension)

print("a solution found using brute force are :\n")
print("point", p1BF, "\nand point", p2BF)
print("which was", minDistanceBF, "units appart")
print("and took", countProcBF, "process.\n\n")

print("another solution found using divide and conquer are :\n")
print("point", p1DNC, "\nand point", p2DNC)
print("which was", minDistanceDNC, "units appart")
print("and took", countProcDNC, "process.\n\n")
