import csv
checkSumSheet = []
x = 0
with open('input.txt', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter='\t')
	for row in reader:
		anew =[]
		for i in range(len(row)):
			anew.append(int(row[i]))
		checkSumSheet.append(row)
		checkSumSheet[x] = sorted(checkSumSheet[x], reverse=True)
		x+=1

checkSum = 0

for i in checkSumSheet:
	for j in i:
		x
print(checkSum)
