#Add our dependencies
import csv
import os

#Assign a variable for the file to load a file from a path
file_to_load = "Resources\election_results.csv"

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#Open election results and read the file
with open(file_to_load) as election_data:

    #To do: read and analyze the data here.
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Print the header row
    headers = next(file_reader)
    print(headers)

    #for row in file_reader:
        #print(row)

    #using the open() function with the "w" mode we will write data to the file
    with open(file_to_save, "w") as txt_file:
    #Write some data to the file
        txt_file.write("Counties in the Election\n")
        txt_file.write("---------------------------------\n")
        txt_file.write("Arapahoe\nDenver\nJefferson")

    #Close the file
    txt_file.close()

    #Close the file
    election_data.close()
#1. The total number of votes cast
#2. The complete list of candidates who recieved votes
#3. The prentage of votes each candidates won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote