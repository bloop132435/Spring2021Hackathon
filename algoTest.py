import os
from parse import parse

testData = parse()
algoIn = open("algoIn.txt","w")
algoIn.write(str(len(testData)) + " " + "\n")
for entry in testData:
    for i in range(0,49):
        algoIn.write(str(entry[i]) + " ")
    algoIn.write("\n")
os.system("./a.out < algoIn.txt")
