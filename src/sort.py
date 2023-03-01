def sort(arr, dimension=0) :
    if (len(arr) <= 1) :
        return arr

    mid = len(arr) // 2

    left = []
    right = []

    for i in range(0, mid) :
        left.append(arr[i])
    for i in range(0, len(arr)-mid):
        right.append(arr[mid + i])

    left = sort(left)
    right = sort(right)
    arr = mergeSort(left, right, arr, dimension)

    return arr

def mergeSort(left, right, arr, dimension=0) :

    arr = []

    nLeft = len(left)
    nRight = len(right)
    j = 0
    k = 0

    while (j < nLeft  and k < nRight) : 
        if (left[j][dimension] < right[k][dimension]) :
            arr.append(left[j])
            j+=1
        else :
            arr.append(right[k])
            k+=1
    while (j < nLeft) :
        arr.append(left[j])
        j+=1
    while (k < nRight) :
        arr.append(right[k])
        k+=1
    
    return arr

if __name__ == "__main__" :
    a = [[1,2],[3,2],[2,5]]

    a = sort(a)

    print(a)

