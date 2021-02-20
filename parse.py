def parse():
	dataIn = open("data.txt","r")
	data = []
	for line in dataIn:
		thisLine = line.split(" ")
		print(thisLine)
		for i in range(0,len(thisLine)):
			if thisLine[i]=='':
				thisLine[i] = 0
				pass
			else:
				thisLine[i] = int(thisLine[i])
		data.append(thisLine)
	print(data)

parse()