import csv 

with open("Resources/election_data.csv","r") as e:
    reader = csv.reader(e,delimiter=",")
    for row in reader: 
        print(row)