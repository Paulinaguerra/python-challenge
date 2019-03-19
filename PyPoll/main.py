import os 
import csv

elections_file = os.path.join ("election_data.csv")

with open(elections_file) as csvfile:
    csvreader = csv.reader(csvfile)
    content = csvfile.read()
    header = next(csvreader)

total_votes = 0
candidate = []
percentageV = []
individual_v = []
winner = []

#The total number of votes cast
    for row in csvreader:
    
        total_votes = total_votes + 1 

#A complete list of candidates who received votes and votes
    if row[2] 
    individual_v = len(candidate)

#The percentage of votes each candidate won
    for candidate in total_votes:
        def getPercentageV (candidateData):
        percentageV = round ((individual_v / total_votes) * 100)2

#The winner of the election based on popular vote.
    winner = max(individual_v)append.candidate


#prints
print ("Election Data")
print ("-----------------------")
print ("Total Votes:" total_votes))
print ("-----------------------")
print (candidate + percentageV + individual_v )
print ("-----------------------")
print ("Winner:" winner)
print ("-----------------------")

