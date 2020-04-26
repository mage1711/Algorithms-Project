from data import prepare_data  # get data from csv file
import random

# main merge sort function


def _mergeSort(region):
    # divides array into two halfs recursively
    if len(region) > 1:
        middle = len(region)//2
        # split array
        right = region[middle:]
        left = region[:middle]
        # recursive call
        _mergeSort(right)
        _mergeSort(left)
        # clear array to append the data in it later
        region.clear()
        # loops unitl left and right are empty
        while len(right) > 0 and len(left) > 0:
            # checks who is bigger and appends it to main array
            if right[0] >= left[0]:
                region.append(left[0])
                left.pop(0)
            else:
                region.append(right[0])
                right.pop(0)
        # when the recursive call finishes append to the array
        for i in left:
            region.append(i)
        for i in right:
            region.append(i)


def mergeSort():
    # prepare data
    data = prepare_data()
    # get region data
    region = list(data.Region)
    # call sort function
    _mergeSort(region)
    return region

# Binary search method to find the element required


def findElementIndex(sortedRegions, lower, upper, location):
    # condtion if element does not exist
    if(upper < 1):
        return -1
    middle = (lower + upper)//2
    # check the index value if it is equal to the value required return the index
    if (sortedRegions[middle] == location):
        return middle
    # if more than go left
    elif(sortedRegions[middle] > location):
        return findElementIndex(sortedRegions, lower, middle-1, location)
    # if less than go right
    else:
        return findElementIndex(sortedRegions, middle+1, upper, location)


def numberOfFalresAtLocation(location=0):
    # sort to be able to search faster
    sortedRegions = mergeSort()
    # if the user does not enter a location
    if location == 0:
        location = random.choice(sortedRegions)
    # get index of element
    index = findElementIndex(sortedRegions, 0, len(sortedRegions)-1, location)
    # checks if element exists
    if index == -1:
        return"That location does not exist"

    count = 1
    rightSide = index + 1
    leftSide = index - 1
    # checks to the left and to the right of the element
    while(rightSide < len(sortedRegions) and sortedRegions[rightSide] == location):
        count += 1
        rightSide += 1

    while(leftSide > 0 and sortedRegions[leftSide] == location):
        count += 1
        leftSide -= 1
    # return the location and the count
    return location, count


if __name__ == '__main__':
    count = numberOfFalresAtLocation()
    print(count)
