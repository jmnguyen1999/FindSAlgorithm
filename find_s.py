
#-------------------------------------------------------------------------
# AUTHOR:  Josephine Nguyen
# FILENAME:  find_s.py
# SPECIFICATION:  This program freads a .csv file called "contact_lens.csv" that contains a data table of values. From this given file, the program uses the Find-S algorithm to find a maximally specific hypothesis.
# FOR: CS 4200- Assignment #1
# TIME SPENT: 30 min
# #-----------------------------------------------------------*/
#
# #IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays
#
# #importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            db.append (row)
            print(row)

print("\n The initial value of hypothesis: ")

hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the first positive training data in db and assign it to the vector hypothesis
for i, row in enumerate(db):
    #if "Reccommended Lenses" is yes --> save it and break
    if row[num_attributes] == "Yes":
        hypothesis = row
        break


#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")

#if hypothesis is stil == [0, 0, 0, 0], then there are no "Yes" instances for "Reccommended Lenses" --> don't bother looking.
if hypothesis != [0, 0, 0, 0]:
    for row in db:
        #If positive instance --> loop every attribute:
        if row[num_attributes] == "Yes":

            for i, curr_attribute in enumerate(row):
                #If current attribute value != corresponding attribute in hypothesis AND is not "?", change it
                if curr_attribute != hypothesis[i] and hypothesis != "?":
                    hypothesis[i] = "?"             #We can do this because we already know that hypothesis is initialized to the first "yes" instance.

print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)