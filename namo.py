import csv

with open('Active_Employees_and_Contractors_report_20211210_214712.csv') as zen_users:
    csv_reader = csv.reader(zen_users)

    next(csv_reader)

    for line in csv_reader:
        print(line[1])

print('----Break----')

with open('users_12_13_2021 10 11 41 PM.csv') as ms_users:
    csv_reader = csv.reader(ms_users)

    next(csv_reader)

    for line in csv_reader:
        print(line[1])