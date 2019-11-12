


# Reads txt file and returns list of lines
def readFile(filePath):
	file = open(filePath, "r")
	retList = []
	for line in file.read().split('\n'):
		retList.append(line)
	return retList

# Writes a list into a file
def writeFile(tempList, fileName):
	with open(fileName, 'w') as f:
	    for item in tempList:
	        f.write("%s\n" % item)