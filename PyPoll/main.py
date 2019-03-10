import os 
import csv

elections_file = os.path.join ("election_data.csv")

with open(elections_file) as csvfile:
    reader = csv.reader(csvfile)
    content = csvfile.read()

votes = []
county = []
candidate = []
review_percent = []
total_votes = 0
winning_candidate = ""
candidate_count = 0 


for row in csvreader:

    if row[0] = votes 

    
    total_votes = total_votes + 1

    candidate = row["Candidate"]



#A complete list of candidates who received votes


#The percentage of votes each candidate won
def getPercentages(candidateData):

totalvotes = int(candidateData) 

winPercent = 




#The total number of votes each candidate won

#The winner of the election based on popular vote.