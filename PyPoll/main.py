import os
import csv

#Path to csv file
sourceData1 = os.path.join('raw_data','election_data_1.csv')
sourceData2 = os.path.join('raw_data','election_data_2.csv')

fileList = [sourceData1,sourceData2] # add additional files when needed

#offsets
candidate = 2

#vars
totalNumberOfVotes = 0
localVoteCount = 0
rowCount = 0
outDictionary = {}
prev = 0

##algo
for file in fileList:
  localVoteCount = 0
  with open ( file, 'r', newline='', encoding='UTF-8') as sd:
    sourceReader = csv.reader(sd,delimiter=',')
    for row in sourceReader:
      if localVoteCount > 0:   #remove header
            outDictionary[row[candidate]] = outDictionary.get(row[candidate],0) + 1
        
      localVoteCount = localVoteCount + 1
  totalNumberOfVotes = (totalNumberOfVotes + localVoteCount) - 1 #remove header count


##Print output
outFile = open('./pyPoll.txt', 'w+')
print("Election Results")
outFile.write("Election Results\n")
print("---------------------------")
outFile.write("---------------------------\n")

print("Total Votes: " + str(totalNumberOfVotes))
outFile.write("Total Votes: " + str(totalNumberOfVotes)+"\n")
print("---------------------------")
outFile.write("---------------------------\n")
for cand, val in outDictionary.items():
    print(cand + ":\t{0:3.1f}% ({1:5d})".format( (100 * (val/totalNumberOfVotes)), val))
    outFile.write(cand + ":\t{0:3.1f}% ({1:5d})\n".format( (100 * (val/totalNumberOfVotes)), val))
    if val > prev:
        winner = cand
        prev = val
        
print("----------------------")
print("Winner: " + winner)

print("-----------------------------")
outFile.close()


