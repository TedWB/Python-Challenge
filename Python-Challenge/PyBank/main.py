import csv 
import os

files_to_load=os.path.join("Resources", "budget_data.csv")
files_to_output=os.path.join("analysis", "budget_analysis")

total_months=0
months_of_change= []
net_change_list=[]
greatest_increase=["", 0]
greatest_decrease=["", 9999999999999999999]
total_net=0

with open(files_to_load) as financial_data:
    reader = csv.reader(financial_data)
    for row in reader: 
        print(row)
        