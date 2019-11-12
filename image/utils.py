


# Reads txt file and returns list of lines
def readFile(filePath):
	file = open(filePath, "r")
	retList = []
	for line in file.read().split('\n'):
		retList.append(line)
	return retList