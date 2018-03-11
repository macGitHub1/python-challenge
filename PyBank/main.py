import os
import csv


#Path to csv file
sourceData1 = os.path.join('raw_data','budget_data_1.csv')
sourceData2 = os.path.join('raw_data','budget_data_2.csv')
fileList = [sourceData1,sourceData2] # add additional files when needed

#open csv files for reading
localNumberOfMonths = 0
numberOfMonths = 0
revenue = 0
totalRevenue = 0
avgRevenueChange = 0
revenueOffset = 1
prevRev = 0
currentChange = 0
currentChanges = []
highestRevMonth = ''
lowestRevMonth = ''


for file in fileList:
  localNumberOfMonths = 0
  with open ( file, 'r', newline='', encoding='UTF-8') as sd:
   sourceReader = csv.reader(sd,delimiter=',') 
  
   for row in sourceReader:
     if(localNumberOfMonths > 0):  # remove header
       revenue = int(row[revenueOffset])
       totalRevenue = totalRevenue + revenue
       currentChange = revenue - prevRev
     if( currentChange > max(currentChanges, default = 0)):
        highestRevMonth = row[0]
            
     if ( currentChange < min(currentChanges, default = 0)):
        lowestRevMonth = row[0]
            
     currentChanges.append( currentChange )
     prevRev = revenue
        
     localNumberOfMonths = localNumberOfMonths + 1

     
  numberOfMonths = (numberOfMonths + localNumberOfMonths) - 1 #header count

#calc avg revenue
avgRevenueChange = int(sum(currentChanges)/len(currentChanges))

##output
outFile = open('./pyBank.txt', 'w+')
print("Financial Analysis")
outFile.write("Financial Analysis\n")
print("---------------------------")
outFile.write("---------------------------\n")

print("Total Months: " + str(numberOfMonths))
outFile.write("Total Months: " + str(numberOfMonths)+"\n")

print("Total Revenue: $" + str(totalRevenue))
outFile.write("Total Revenue: $" + str(totalRevenue)+"\n")

print("Average Revenue Change: $" + str(avgRevenueChange))
outFile.write("Average Revenue Change: $" + str(avgRevenueChange)+"\n")

print("Greatest Increase in Revenue: " + highestRevMonth + " ($" + str(max(currentChanges)) + ")")
outFile.write("Greatest Increase in Revenue: " + highestRevMonth + " ($" + str(max(currentChanges)) + ")"+"\n")

print("Greatest Decrease in Revenue: " + lowestRevMonth + " ($" + str( min(currentChanges)) + ")")
outFile.write("Greatest Decrease in Revenue: " + lowestRevMonth + " ($" + str( min(currentChanges)) + ")"+"\n")

outFile.close()

  


