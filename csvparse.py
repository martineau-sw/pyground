import csv

def write_to_csv(list, filename=''):
    if(filename == ''):
        return
    with open(filename + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerows(list)

def retrieve_from_csv(filename=''):
    if(filename == ''):
        return
    with open(filename + '.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
