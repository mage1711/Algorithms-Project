import csv

data = []


with open('space.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        data.append(dict.fromkeys(['Rank',
                                   'X_class',
                                   'Region',
                                   'Start_time',
                                   'Max_time',
                                   'End_time']))

        data[int(line[""])]['Rank'] = line["Rank"]
        data[int(line[""])]['X_class'] = line["X_class"]
        data[int(line[""])]['Region'] = line["Region"]
        data[int(line[""])]['Start_time'] = line["Start_time"]
        data[int(line[""])]['Max_time'] = line["Max_time"]
        data[int(line[""])]['End_time'] = line["End_time"]

print(data)
