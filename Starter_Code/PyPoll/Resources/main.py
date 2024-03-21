import os
import csv
csvpath= "/Users/graceshi/Desktop/Data Science Boot Camp/python-challenge/Starter_Code/PyPoll/Resources/election_data.csv"

#with open and csvreader written using learning assistance and course materials
with open(csvpath, 'r') as csvfile:
    csvreader= csv.reader (csvfile, delimiter=',')
    
    #reads the header row 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    totalvotes=[]
    Stockham=[]
    Degette=[]
    Doane=[]

    #function appending 
    for row in csvreader:
        totalvotes.append(row[0])
        if row[2]== "Charles Casper Stockham":
            Stockham.append(row[2])
        elif row[2]== "Diana DeGette":
            Degette.append(row[2])
        elif row[2]== "Raymon Anthony Doane":
            Doane.append(row[2])

    #print(len(Stockham))
    percent_stockham= (len(Stockham)/len(totalvotes))*100
    percent_degette= (len(Degette)/len(totalvotes))*100
    percent_doane= (len(Doane)/len(totalvotes))*100
    
    finalstockham=round(percent_stockham,3)
    finaldegette= round(percent_degette,3)
    finaldoane= round(percent_doane,3)

    total_vote_result = f"total votes:{len(totalvotes)}"
    total_stockham_result= f"Charles Casper Stockham: {finalstockham}% ({len(Stockham)})"
    total_degette_result= f"Diana DeGette: {finaldegette}% ({len(Degette)})"
    total_doane_result= f"Raymon Anthony Doane: {finaldoane}% ({len(Doane)})"
    print (total_vote_result)
    print(total_stockham_result)
    print(total_degette_result)
    print(total_doane_result)
    
    #print(round(max(percent_degette,percent_doane,percent_stockham),3))
    #print(finaldegette)

    #if statement returning the winner using max function
    if round(max(percent_degette,percent_doane,percent_stockham),3) == finalstockham:
        result="Winner: Charles Casper Stockham"
    elif round(max(percent_degette,percent_doane,percent_stockham),3) == finaldegette:
        result="Winner: Diana DeGette"
    elif round(max(percent_degette,percent_doane,percent_stockham),3) == finaldoane:
        result="Winner: Raymon Anthony Doane"
    print(result)

#code written to export results into .txt file was written with help from ChatGPT

filepath="/Users/graceshi/Desktop/Data Science Boot Camp/python-challenge/Starter_Code/PyPoll/Resource"
filepath="pypollresults.txt"
output_string= f"{total_vote_result}\n{total_stockham_result}\n{total_degette_result}\n{total_doane_result}\n{result}"
with open(filepath,"w") as file:
    file.write(output_string)
print("results exported to:",filepath)
