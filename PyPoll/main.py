import os
import csv

#Initialising dictionary
candidate_dict={}

winner_count=0

electionfile=os.path.join('.','election_data.csv')
with open(electionfile, newline="") as electiondata:
    electionreader=csv.reader(electiondata, delimiter=',')
    electionheader=next(electionreader)
    # looping through rows in election file
    for election in electionreader:

        # setting the key: value pair in dictionary
        cand_exist=candidate_dict.get(election[2],False)
        if( cand_exist):
            candidate_dict[election[2]]=cand_exist+1
        else:
            cand_exist=1
            candidate_dict.setdefault(election[2],cand_exist)
    total_votes=sum(candidate_dict.values())
    print("Election Results")
    print("-----------------------------------------------")
    print("Total Votes: "+str(total_votes))
    print("--------------------------------------")
    # Below snippet loops through the dictionary and calculates the winner candidate count and %
    for i in range (0,len(candidate_dict)):
        if (list(candidate_dict.values())[i]>winner_count):
            winner_count=list(candidate_dict.values())[i]
            winner_name=list(candidate_dict.keys())[i]
        vote_percent=(list(candidate_dict.values())[i]/total_votes)*100
        print(list(candidate_dict.keys())[i]+": "+"%.3f%% " % vote_percent+"("+str(list(candidate_dict.values())[i])+")")
    print("------------------------------------------------------")
    print("Winner is: "+winner_name)
    print("------------------------------------------------------")
