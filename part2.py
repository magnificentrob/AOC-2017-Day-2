import csv
checkSumSheet = []
x = 0
with open('input.txt', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter='\t')
	for row in reader:
		checkSumSheet.append(row)
		for i in range(len(row)):
			row[i] = int(row[i])
		checkSumSheet[x] = sorted(checkSumSheet[x], reverse=True)
		x+=1

checkSum = 0

for i in checkSumSheet:
	for j in i:
		x
print(checkSum)