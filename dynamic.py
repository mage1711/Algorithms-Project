from data import prepare_data
from transform import quickSort

# function to find the longest sequence of flares


def _findLongestSequenceOfFlares(StartTime, days):
    size = len(StartTime)
    maximum = 0
    # initialize the table that will have the sequences
    tableOfSequences = [1]*size

    # loop over each sequence
    for i in range(1, size):
        for j in range(0, i):
           # condition checks if next element has a the day diference and a table sequence checker
            if tableOfSequences[i] < tableOfSequences[j] + 1 and ((StartTime[i] - StartTime[j]).days) <= days:
                tableOfSequences[i] = tableOfSequences[j]+1

    # get the max value from the table of sequences
    for i in range(size):
        maximum = max(maximum, tableOfSequences[i])

    return maximum

# function to prepare the data


def findLongestSequenceOfFlares(days=10):
    data = prepare_data()
    StartTime = list(data.Start_time)
    # sort array before use
    # quickSort(StartTime, 0, len(StartTime)-1)
    return _findLongestSequenceOfFlares(StartTime, days)


if __name__ == '__main__':
    print("max sequence is", findLongestSequenceOfFlares())
