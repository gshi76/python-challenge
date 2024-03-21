import os
import csv
csvpath= "/Users/graceshi/Desktop/Data Science Boot Camp/python-challenge/Starter_Code/PyBank/Resources/budget_data.csv"

#opens and reads csv file
with open(csvpath, 'r') as csvfile:
    csvreader= csv.reader (csvfile, delimiter=',')
    
    #reads the header row 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#create new lists
    months=[]
    profitloss= []
    
    #adds values into sorted lists
    for row in csvreader:
        months.append(row[0])
        profitloss.append(int(row[1]))
    

    totalmonths= len(months)
    nettotal= sum(profitloss)
    
    total_month_result=f"total months:{totalmonths} months"
    print(total_month_result)
    net_total_result=f"Total: ${nettotal}"
    print(net_total_result)

    
    #new list created. Range starts with 1 because it takes the difference of the months starting from the 2nd value
    monthchange= []
    for i in range(1,len(profitloss)):
        difference= profitloss[i]-profitloss[i-1]
        monthchange.append(difference)
    
    averagechange= (sum(monthchange)/len(monthchange))
    totalaverage=f"Total Average: ${round(averagechange,2)}"
    print(totalaverage)

    greatestincrease= max(monthchange)
    greatestdecrease= min(monthchange)
    # print(greatestincrease)
    # print(greatestdecrease)

#index +1 because there is 1 less value in differences than months 
    index_increase= monthchange.index(greatestincrease)
    month_increase= months[index_increase+1]

    index_decrease= monthchange.index(greatestdecrease)
    month_decrease = months[index_decrease+1]

    greatestincrease=f"Greatest Increase in Profits: {month_increase} (${greatestincrease})"
    print (greatestincrease)

    greatestdecrease=f"Greatest Decrease in Profits:{month_decrease}(${greatestdecrease})"
    print(greatestdecrease)

#code written to export results into .txt file was written with help from ChatGPT
filepath="/Users/graceshi/Desktop/Data Science Boot Camp/python-challenge/Starter_Code/PyBank"
filepath="pybankresults.txt"
output_string= f"{total_month_result}\n{net_total_result}\n{totalaverage}\n{greatestincrease}\n{greatestdecrease}"
with open(filepath,"w") as file:
    file.write(output_string)
print("results exported to:",filepath)

   
