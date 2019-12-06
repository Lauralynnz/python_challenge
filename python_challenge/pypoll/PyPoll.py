#!/usr/bin/env python
# coding: utf-8

# In[2]:


# PyPoll

# Modules
import csv
import os

# ID input/output files
file_to_load = os.path.join("election_data.csv")
file_to_output = os.path.join("election_analysis.txt")

# Create var to tally total num votes
total_votes = 0

# Create list to store candidates
candidate_options = []

# Create dict to tally num votes per candidate
candidate_votes = {}

# Create winning candidate vars
winning_candidate = ""
winning_count = 0

# Read the input file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    # Read the header
    header = next(reader)
    
    for row in reader:
        
        # Run the loader animation
        #print(". ", end="")
        
        # Add to total vote count
        total_votes = total_votes + 1
        
        # Extract candidate name from each row
        candidate_name = row[2]
        
        #If candidate name is not on list
        if candidate_name not in candidate_options:
        
            #Add to list of candidates
            candidate_options.append(candidate_name)
        
            # track candidates voter count
            candidate_votes[candidate_name] = 0 
    
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(file_to_output, "w") as txt_file:
        #print final vote count
        
    election_results = (
        "\n\nElection Results\n" +
        "--------------------\n" +
        "Total Votes: " + str(total_votes) + "\n" +
        "--------------------\n"
    )
    print(election_results)
    
    # Save final vote count to txt file
    txt_file.write(election_results)
    
    # Find the winner
    for candidate in candidate_votes:
        
        # Determine num votes and perct per candidate
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Determine winner
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        # Print each candidate's voter count and percentage
        voter_output = f"{candidate}: {vote_percentage:3f}% ({votes})\n"
        
        print(voter_output, end="")
        
        txt_file.write(voter_output)

    #Print winning candidate
    winning_candidate_summary = (
    f"--------------------\n"
    f"Winner: {winning_candidate}\n"
    f"--------------------\n"
    )
         
    print(winning_candidate_summary)
    
    #Save the winning candidate name to text file
    txt_file.write(winning_candidate_summary)


# In[ ]:





# In[ ]:




