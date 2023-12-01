import csv
checkSumSheet = []

with open('input.txt', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter='\t')
	for row in reader:
		anew =[]
		for i in range(len(row)):
			anew.append(int(row[i]))
		checkSumSheet.append(anew)

checkSum = 0
for i in range(len(checkSumSheet)):
	lowest_value = min(checkSumSheet[i])
	higest_value = max(checkSumSheet[i])
	difference = higest_value - lowest_value
	checkSum = checkSum+difference
print(checkSum)
