import pandas as pd
# import our functions
from transform import closestEvents
from greedy import maxNoOfEvnets
from conquer import numberOfFalresAtLocation
from dynamic import findLongestSequenceOfFlares

# load the solar flare data
data = pd.read_csv('space.csv', index_col=0)



if __name__ == "__main__":
    print('Sample of the Solar Flare Events data:')
    print(data.sample(5))

    print("List of Functions:")
    print('1. Max Number of Solar Flare events that can happen in the given period.')
    print('2. The closest 2 Solar Flare events')
    print('3. The Number of Solar Flares that occured at random location')
    print('4. The number of Solar Flares that happend with in the given number of days')
    print('5. Show sample of the data')
    print('6. Exit')
    print("Function Number:", end=' ')

    # read input
    i = int(input())
    
    options = [1, 2, 3, 4, 5, 6]
    if i in options:
        if i == 1:
            print('Max Number of Solar Flares in the given period')
            print('_'*100)
            print('Number of hours:', end=' ')
            h = int(input())
            if h > 0:
                out_df, numberOfEvents, currentTime = maxNoOfEvnets(h)
                print(f'Number of events: {numberOfEvents}')
                print(f'The exact time taken: {currentTime}')
                print('The events:')
                print(pd.DataFrame(out_df))
            else:
                print('The number of hours must be > 0')

        elif i == 2:
            print("The Closest 2 Solar Flare Events")
            print('_'*100)
            min_difference, closest_events = closestEvents()
            print('Min Difference between 2 events:', min_difference)
            print('The events:')
            for index, e in enumerate(closest_events):
                print(f'Event {index+1}:')
                print(e[1:])
                print('_'*50)

        elif i == 3:
            location, number = numberOfFalresAtLocation()
            print('The Number of Solar Flares that occured at random location')
            print('_'*100)
            print(f'Number of Flare Events: {number}')
            print(f'The Location: {location}')


        elif i == 4:
            print('The number of Solar Flares that happend with in the given number of days')
            print('_'*100)
            print('Number of days:', end=' ')
            d = int(input())
            number = findLongestSequenceOfFlares(d)
            print(f'Number of Solar Flares: {number}')

        elif i == 5:
            print('_'*100)
            print(data.sample(5))
        
        elif i == 6:
            pass
    else:
        print('Available Function Numbers are', options)