# Modules
import pandas as pd 
import datetime
from greedy import prepare_data # to get the data from csv file

'''
QuickSort is a Divide and Conquer algorithm
it works by picking an element as pivot and partitions
the given array around the picked pivot. Here we pick the last element as a pivot
Partition:
the target of the 'Partition' function: given an array and an element x
as pivot, put x in its corret position in sorted array and put all smaller elements
before x and all greater elements after x.
'''

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 



def closest_events():
    # get the data from csv file and process it
    data = prepare_data()

    # getting a list of the Start_time values in the csv file
    arr = list(data.Start_time)

    # sort the data in increasing order by Start_time
    arr = list(data.Start_time) # get the starting time of all the events
    n = len(arr) # get the number of events
    quickSort(arr,0,n-1)  # sort the events

    # Setting the needed variables
    length = len(data) # the lenght of the events
    min_difference = datetime.timedelta(days=10000) # variable holding the min difference between events

    # looping through the data
    for i in range(1, length):
        # get the difference between the two consequtive events starting time
        difference = arr[i] - arr[i-1]

        # if the current difference is less than the minimum difference
        # set the min_difference to the new current difference
        if difference < min_difference:
            min_difference = difference
            closest_events = [] # list holding the 2 closest events
            # get the info about the events
            out = data[data.Start_time == arr[i]]
            closest_events.append(out.iloc[0])
            out = data[data.Start_time == arr[i-1]]
            closest_events.append(out.iloc[0])

    # return the minumum difference and the info about the 2 closest events
    return min_difference, closest_events