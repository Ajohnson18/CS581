#	Author: Alex Johnson
#	Create a program that analyzes facebook data
#	To run type python3 analyze_fb_data.py then enter the name of the FB data csv file

import csv	# needed to read and write csv
import matplotlib.pyplot as plt # needed for creating graph
import sys # needed for ending program

under20 = []
a20to30 = []
a30to40 = []
a40to50 = []
a50to60 = []
a60andgreater = [] 	# arrays for storing data by age

def readFile(filename):
	with open(filename, 'r') as csvfile:
		csvreader = csv.reader(csvfile) # opens and reads csv file
		for row in csvreader: 	# parse through rows of csv file
			try:
				if int(row[1]) < 20:
					under20.append(row)
				elif int(row[1]) >= 20 and int(row[1]) < 30:
					a20to30.append(row)
				elif int(row[1]) >= 30 and int(row[1]) < 40:
					a30to40.append(row) 
				elif int(row[1]) >= 40 and int(row[1]) < 50:
					a40to50.append(row)
				elif int(row[1]) >= 50 and int(row[1]) < 60:
					a50to60.append(row)
				else:
					a60andgreater.append(row) 	# append the row to the correct age group
			except:
				continue
	analyzeData()

def analyzeData():
	numU20 = num2030 = num3040 = num4050 = num5060 = num60 = 0
	f20 = f2030 = f3040 = f4050 = f5060 = f60 = 0
	lg20 = lg2030 = lg3040 = lg4050 = lg5060 = lg60 = 0
	ml20 = ml2030 = ml3040 = ml4050 = ml5060 = ml60 = 0
	wl20 = wl2030 = wl3040 = wl4050 = wl5060 = wl60 = 0 	#initialize variables which will be analyzed
	for row in under20:
		numU20 += 1
		f20 += int(row[7])
		lg20 += int(row[9])
		ml20 += int(row[11])
		wl20 += int(row[13])
	for row in a20to30:
		num2030 += 1
		f2030 += int(row[7])
		lg2030 += int(row[9])
		ml2030 += int(row[11])
		wl2030 += int(row[13])
	for row in a30to40:
		num3040 += 1
		f3040 += int(row[7])
		lg3040 += int(row[9])
		ml3040 += int(row[11])
		wl3040 += int(row[13])
	for row in a40to50:
		num4050 += 1
		f4050 += int(row[7])
		lg4050 += int(row[9])
		ml4050 += int(row[11])
		wl4050 += int(row[13])
	for row in a50to60:
		num5060 += 1
		f5060 += int(row[7])
		lg5060 += int(row[9])
		ml5060 += int(row[11])
		wl5060 += int(row[13])
	for row in a60andgreater:
		num60 += 1
		f60 += int(row[7])
		lg60 += int(row[9])
		ml60 += int(row[11])
		wl60 += int(row[13]) 	# for each array go through and collect the data by age and put it into the variables

	print("")
	print("Total Number of Users by Age")
	print("----------------------------------")
	print("Under 20: %s" % numU20)
	print("20 - 29:  %s" % num2030)
	print("30 - 39:  %s" % num3040)
	print("40 - 49:  %s" % num4050)
	print("50 - 59:  %s" % num5060)
	print("Over 60:  %s" % num60)
	print("")
	print("Average Number of Friends by Age")
	print("----------------------------------")
	print("Under 20: %.2f" % (f20 / numU20))
	print("20 - 29:  %.2f" % (f2030 / num2030))
	print("30 - 39:  %.2f" % (f3040 / num3040))
	print("40 - 49:  %.2f" % (f4050 / num4050))
	print("50 - 59:  %.2f" % (f5060 / num5060))
	print("Over 60:  %.2f" % (f60 / num60))
	print("")
	print("Total Number of Likes Given by Age")
	print("----------------------------------")
	print("Under 20: %.2f" % (lg20))
	print("20 - 29:  %.2f" % (lg2030))
	print("30 - 39:  %.2f" % (lg3040))
	print("40 - 49:  %.2f" % (lg4050))
	print("50 - 59:  %.2f" % (lg5060))
	print("Over 60:  %.2f" % (lg60))
	print("")
	print("Mobile Likes Given : WWW Likes Given by Age")
	print("----------------------------------")
	print("Under 20: %.2f:1" % (ml20 / wl20))
	print("20 - 29:  %.2f:1" % (ml2030 / wl2030))
	print("30 - 39:  %.2f:1" % (ml3040 / wl3040))
	print("40 - 49:  %.2f:1" % (ml4050 / wl4050))
	print("50 - 59:  %.2f:1" % (ml5060 / wl5060))
	print("Over 60:  %.2f:1" % (ml60 / wl60)) 			# Print out the data by age with the performed operations

	with open('fb_analysis_results.csv', mode='w') as results:
		results = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 	#open a new csv file for writing
		results.writerow(["Age Range", "Total Users", "Avg # of Friends", "Total likes Given", "Mobile Likes / WWW Likes"]) 	#write header row
		results.writerow(["Under 20", numU20, (f20/numU20), lg20, (ml20/wl20)])
		results.writerow(["20 - 30", num2030, (f2030/num2030), lg2030, (ml2030/wl2030)])
		results.writerow(["30 - 40", num3040, (f3040/num3040), lg3040, (ml3040/wl3040)])
		results.writerow(["40 - 50", num4050, (f4050/num4050), lg4050, (ml4050/wl4050)])
		results.writerow(["50 - 60", num5060, (f5060/num5060), lg5060, (ml5060/wl5060)])
		results.writerow(["Over 60", num60, (f60/num60), lg60, (ml60/wl60)])	# write a row for each age group and the analyzed dara

	print("")
	print("")
	print("Select a graph or type STOP to finish:")
	print(" (1): Total Users by Age")
	print(" (2): Average Number of Friends by Age")
	print(" (3): Total Likes Given by Age")
	print(" (4): Mobile Likes : WWW Likes by Age") 	# print options in order to select the graph to be shown
	p = 0
	while True: 	# loop unil a correct number is picked
		p = input("Select a number: ") 	#take input of the number
		if p.upper() == "STOP": 	#if input is stop kill the program
			sys.exit()
		try:
			p = int(p) 	#try to convert the input to an integer
		except:
			print("Error: Please enter a integer between 1 and 4") #if failed to convert print error an try again
			continue
		if p < 5 and p > 0: 	#if correct number then continue
			break
		else:
			print("Error: Invalid input")
			continue

	plt_names = ['Under 20', '20 - 30', '30 - 40', '40 - 50', '50 - 60', 'Over 60'] 	#set x values for graph
	x_title = "Age" 	#assign x title
	y_title = plt_title = "" 	
	if p == 1: 	#for each graph input the data into plt_data and then change the ytitle and title
		plt_data = [numU20, num2030, num3040, num4050, num5060, num60]
		plt_title = "Total Users by Age"
		y_title = "Total Users"
	elif p == 2:
		plt_data = [(f20/numU20), (f2030/num2030), (f3040/num3040), (f4050/num4050), (f5060/num5060), (f60/num60)]
		plt_title = "Average # of Friends by Age"
		y_title = "Avg Friends"
	elif p == 3:
		plt_data = [lg20, lg2030, lg3040, lg4050, lg5060, lg60]
		plt_title = "Total Likes Given by Age"
		y_title = "Total likes"
	else:
		plt_data = [(ml20/wl20), (ml2030/wl2030), (ml3040/wl3040), (ml4050/wl4050), (ml5060/wl5060), (ml60/wl60)]
		plt_title = "Mobile Likes Given / WWW Likes Given"
		y_title = "Mobile Likes / WWW Likes"
	plt.bar(plt_names, plt_data) # put names and values into the bar graph
	plt.title(plt_title) # change the title of graph
	plt.ylabel(y_title)
	plt.xlabel(x_title) # change the x and y title of the graph
	plt.show()	 	#show graph

def stop():
	sys.exit() 	#exit systen if stopped

file = input("Filename: ") 	#get filename
try:
	readFile(file)
except:
	print("Error: Invalid filename") #if invalid end program

