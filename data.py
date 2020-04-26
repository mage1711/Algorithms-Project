# Modules
import pandas as pd # to load csv files
import datetime # to enable us to work with time variables

def prepare_data():
    # load the csv file 
    data = pd.read_csv('space.csv', index_col=0)

    # convert Start_time, End_time to datetime datatype
    data.Start_time = pd.to_datetime(data.Start_time)
    data.End_time = pd.to_datetime(data.End_time)

    # get the duration of each event in Duration column
    data['Duration'] = data.End_time - data.Start_time
    
    return data

