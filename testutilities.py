import os
import csv
import random
    
# An object to make testing easier by generating lists.

class MetaTest:

    def MetaTest(self):
        self.expected
        self.actual
        self.data


# Generates 

def generate_unordered_ints(size, min=0, filename=''):
    l = [x for x in range(min,size)]
    random.shuffle(l)
    write_to_csv(l,filename)
    return l

def generate_ordered_ints(self, size, min=0, filename=''):
    l = [x for x in range(size)]
    self.write_to_csv(l, filename)
    return l

def write_to_csv(self, list, name):
    if(name == ''):
        return
    with open( name + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerow(list)
        

    