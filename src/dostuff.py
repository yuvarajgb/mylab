
import remote
import csv
import os

def checkallstatus():
	'''it will update the status of each host into a csv file'''
	try:
		os.remove('temp.csv')
	except OSError:
		pass

	with open('hostlist.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile, delimiter = ',')
		for row in csvreader:
			hostname = row[0]
			status = remote.pingstatus(hostname)
			with open('temp.csv', 'a') as tempcsv:
				csvwriter = csv.writer(tempcsv, delimiter = ',')	
				if status == 0:
					row.append("ALIVE")
					csvwriter.writerow(row)
				else:
					row.append("DOWN")
					csvwriter.writerow(row)

	os.rename('temp.csv', 'hostlist.csv')
	return


def getlongestline(filename):
	'''find the longest line in the given file'''
	fopen = open(filename, 'r')
	max = 0
	for line in fopen.readlines():
		if len(line) > max:
			max = len(line)
			lline = line

	return (lline, max)

if __name__ == "__main__":
	#checkallstatus()

	flag = False
	while flag == False:
		filename = str(raw_input("Enter filename: "))
		if os.path.exists(filename):
			longestline, length = getlongestline(filename)
			print "Longest line => %s"%longestline.rstrip()
			print "Length of the longest line => %d"%length
			flag = True #File exists, break the loop
		else:
			print "Invalid file name. Please retry"




