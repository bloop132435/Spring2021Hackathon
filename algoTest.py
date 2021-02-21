import os
from parse import parse
from time import sleep
testData = parse()
algoIn = open("algoIn.txt","w")
algoIn.write(str(len(testData)) + " " + "\n")
for entry in testData:
    for i in range(0,49):
        algoIn.write(str(entry[i]) + " ")
    algoIn.write("\n")
algoIn.close()
os.system("./a.out < algoIn.txt")
