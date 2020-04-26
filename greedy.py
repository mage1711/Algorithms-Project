# Modules
import pandas as pd # to load csv files
import datetime # to enable us to work with time variables
from data import prepare_data


'''
Greedy Algorithm - Maximum number of events in given duration
- given the number of hours, how many solar events can happen in this duration

- Steps
    1. Sort the Durations in increasing order
    2. Select each duration item one-by-one
    3. Add the time of the event to currentTime 
    4. Add one to number of things
    5. Stop if the currentTime exceed the maxTime

- Input
    - the solar flares events data
    - the number of hours - the period duration in hours
- Output
    - Info about the events that can be fitted in the time period
    - The number of events
    - The percise total time taken 
'''
# input: the number of hours
def maxNoOfEvnets(hours=1):

    # prepare the data for processing
    data = prepare_data()

    # Sort the Data in increasing order by Durations
    # Pandas sort algorithm uses QuickSort O(n^2)
    data = data.sort_values('Duration')

    # Setting the needed variables
    maxTime = datetime.timedelta(hours=hours) # maxTime for all the events
    currentTime = datetime.timedelta(0) # variable holding the sum of durations
    numberOfEvents = 0 # the maximum number of events that can occur in the period given
    out_df = [] # the events info the can occur in the given duration


    # Loop through the durations of the solar flare events
    for _, row in data.iterrows():
        # add the current duration to the currentTime
        currentTime += row['Duration']

        # Break if exceeded the maxTime allowed for the events
        if currentTime > maxTime:
            # remove the last duration to get the correct currentTime
            currentTime -= row['Duration']
            break
        # increase the number of events by 1
        numberOfEvents += 1
        # add data about the event to the output dataframe
        out_df.append(row)

    # return the number of events, the total time they took and the events themselves
    return out_df, numberOfEvents, currentTime
