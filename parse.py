def parse():
	dataIn = open("data.txt","r")
	data = []
	for line in dataIn:
		thisLine = line.split(" ")
		for i in range(0,len(thisLine)):
			if thisLine[i]=='':
				thisLine[i] = 0
				pass
			elif not thisLine[i].isdigit():
				pass
			else:
				thisLine[i] = int(thisLine[i])
		if thisLine[len(thisLine)-1]=='\n':
			thisLine.pop()
		for i in range(0,20):
			thisLine.append(0)
		data.append(thisLine)

	return data
