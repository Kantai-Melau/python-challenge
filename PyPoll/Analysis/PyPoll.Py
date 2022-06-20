import os
import csv
import sys

elections_csv= os.path.join("..","Resources","election_data.csv")
with open(elections_csv) as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=",", skipinitialspace=True)
    csv_header= next(csv_file)

    file_path = 'Pybank.txt'
    sys.stdout = open(file_path, "w")

    total_votes=0; count_charles=0; count_diana=0; count_raymon=0
    candidate_list=[]
    for row in csv_reader:
#Total votes cast
        total_votes += 1
#A complete list of candidates who received votes
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
#Count of votes won by each candidate
        if row[2] == "Charles Casper Stockham":
            count_charles += 1
        elif row[2] == "Diana DeGette":
            count_diana += 1
        else:
            count_raymon +=1
    winner=max(count_charles,count_diana,count_raymon)
    
#Percentage won by each candidate
    charles_percent = "{:.3%}".format(count_charles / total_votes)
    diana_percent = "{:.3%}".format(count_diana / total_votes)
    raymon_percent = "{:.3%}".format(count_raymon / total_votes)

#Print output
print("Election Results")
print("-"*25)
print("Total Votes: ", total_votes)
print("-"*25)
print(f"{candidate_list[0]}: {charles_percent} {count_charles}")
print(f"{candidate_list[1]}: {diana_percent} {count_diana}")
print(f"{candidate_list[2]}: {raymon_percent} {count_raymon}")
print("-"*25)
print("Winner: ", candidate_list[1])
print("-"*25)

sys.stdout.close()
