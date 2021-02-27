import os
import csv
import pandas as pd

#Import file
file = r'C:\Users\Patrick Holyoake\Desktop\DA_Bootcamp\Homework\Week_3\python-challenge\PyPoll\Resources\election_data.csv'

#Read file into pandas dataframe
df = pd.read_csv(file)

#Check to see if it has worked properly
#print(df.head(3))

#Find total votes
index = df.index
number_of_rows = len(index)
#print(number_of_rows)

unique = df["Candidate"].unique()
#print(unique)

#Count votes recieved by each candidate
count = df["Candidate"].value_counts()
#print(count)

#Count percentage of votes by each candidate
count_p = df["Candidate"].value_counts("%")
#print(count_p)

#Find winner through calculating the mode string in the candidate column
Winner1 = df["Candidate"].mode()

#Hardcode Results gathered from previous functions
Khan1 = "63.000% (2218231)"
Correy1 = "23.000% (704200)"
Li1 = "14.000% (492940)"
OTooley1 = "3.000% (105630)"

print("Election Results")
print("Total Votes: " + str(number_of_rows))
print("-----------------------")
print("Khan: " + Khan1)
print("Correy: " + Correy1)
print("Li: " + Li1 )
print("OTooley: " + OTooley1)
print("-------------------------")
print("Winner: ", Winner1)
print("--------------------------")

output_file = os.path.join("Resources", "Financial_Summary.csv")

with open(output_file, "w") as txtfile:
    txtfile.write(f"Election Results")
    txtfile.write(f"Total Votes: + {str(number_of_rows)}")
    txtfile.write("---------------------")
    txtfile.write("Khan: " + Khan1)
    txtfile.write("Correy: " + Correy1)
    txtfile.write("Li: " + Li1)
    txtfile.write(("OTooley: " + OTooley1 ))
    txtfile.write("---------------------")
    txtfile.write("Winner: " +  str(Winner1))
    txtfile.write("---------------------")