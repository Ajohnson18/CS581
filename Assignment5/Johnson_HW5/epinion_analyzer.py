# Author: Alex Johnson
# Assignment 5 for CS581
# I pledge my honor that I have abided by the Stevens Honor System.
# Program can be run with python3 epinion_analyzer
# then entering the name of the csv file to analyze

import csv # needed for ouput of search result

import os.path	#needed to check for file existance
from os import path

import networkx as nx # needed to analyze graphs

G = nx.Graph()	# create a graph

rows = []	# used to store the csv file
edges = selfLoops = trusts = distrusts = triangles = 0	# variables to identify 

# This function reads in data from a csv file and stores it in 
# an array called rows. It also takes the first two integers
# from the row and creates an edge in graph G
def readData(file):
	with open(file, 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		for row in csvreader:
			rows.append(row)
			G.add_edge(int(row[0]), int(row[1]), weight=row[2])

# This function finds what type of triangle it is
# the input is a triangle clique from the graph G
# output is an integer value which is the sum of the 
# trusts on each edge.
def getType(tri):
	t0 = int(tri[0])
	t1 = int(tri[1])
	t2 = int(tri[2])	# convert each edge of the triangle into an integer
	track = 0
	count = 0
	for row in rows:	# parse through the array of rows
		if(count == 3):	# if all three are found break
			break
		r0 = int(row[0])
		r1 = int(row[1])	# covert the row into integer values
		w = int(row[2])
		if((r0 == t0) or (r0 == t1) or (r0 == t2)) and ((r1 == t0) or (r1 == t1) or (r1 == t2)) and (r1 != r0):
			track += w
			count += 1		# if the row has two of the nodes from the edge it is found
	if track == (3):
		return 3
	elif track == (1):
		return 1
	elif track == (-3):
		return (-3)
	elif track == (-1):
		return (-1)
	else:
		return

def parseData():
	countArr = []
	countEdges = 0
	countSelfLoops = 0
	countTrusts = 0
	countDistrusts = 0	# counting variables
	for row in rows:	# parse through rows
		if row[0] != row[1]:
			countEdges = countEdges + 1	# counts the number of edges 
		else:
			countSelfLoops = countSelfLoops + 1 
			countEdges = countEdges + 1
		if (int(row[2]) + 1) == 2:
			countTrusts = countTrusts + 1	# counts number of trusts
		else:
			countDistrusts = countDistrusts + 1	# counts number of distrusts
	countArr.append(countEdges)
	countArr.append(countSelfLoops)
	countArr.append(countTrusts)
	countArr.append(countDistrusts)
	return countArr					# append all the data to an array and return for analyzing


def findTriangles(G):
	count = 0
	cliques = nx.enumerate_all_cliques(G)	# find all the cliques in graph G
	for c in cliques:
		if len(c) == 3:
			count += 1	# check if the click is of size three and then increase counter
	return count

while True:	# check for file in the directory
	filename = input("Filename: ")
	if(path.exists(filename)):
		break
	else:
		print("Error: File not found.")
		continue

edges = selfLoops = 0	

readData(filename)
result = parseData()
edges = result[0]
selfLoops = result[1]
trusts = result[2]
distrusts = result[3]
triangles = findTriangles(G)	# run functions to collect data
print("Edges in network: " + str(edges))
print("Self-Loops: " + str(selfLoops))
print("Edges Used - Tot Edges: ", str(edges - selfLoops))
print("Trust Edges: " + str(trusts) + "		Probability p: %.2f" % (trusts / edges))
print("Distrust Edges: " + str(distrusts) + "		Probability 1-p: %.2f" % (distrusts / edges))
print("Triangles: " + str(triangles))
print("")	# formatting and printing of the data

pofT = trusts / edges
pofD = distrusts / edges 			#calculate the probability for each trust
	
cl = nx.enumerate_all_cliques(G)
TTTCount = TTDCount = TDDCount = DDDCount = 0 	# find all the different types of triangles
for c in cl:
	if len(c) == 3:
		t = getType(c)
		if t == 3:
			TTTCount += 1
		elif t == 1:
			TTDCount += 1
		elif t == -1:
			TDDCount += 1
		elif t == -3:
			DDDCount += 1
		else:
			continue

# formatting and printing of the data

print("Expected Distubution		Actual Distibution")
print("----------------------------------------------------")
print("Type Percent Number 	 	Type  Percent  Number")
print("----------------------------------------------------")
TTTProb = (pofT * pofT * pofT)
print("TTT  %.2f" % (TTTProb * 100) + "  %.2f" % (TTTProb * triangles) + "		TTT 	%.2f" % (TTTCount / triangles * 100) + "  " + str(TTTCount))
TTDProb = (pofT * pofT * pofD * 3)
print("TTD  %.2f" % (TTDProb * 100) + "  %.2f" % (TTDProb * triangles) + "		TTD 	%.2f" % (TTDCount / triangles * 100) + "  " + str(TTDCount))
TDDProb = (pofT *pofD *pofD * 3)
print("TDD  %.2f" % (TDDProb * 100) + "  %.2f" % (TDDProb * triangles) + "		TDD 	%.2f" % (TDDCount / triangles * 100) + "  " + str(TDDCount))
DDDProb = (pofD * pofD * pofD)
print("DDD   %.2f" % (DDDProb * 100) + "  %.2f" % (DDDProb * triangles) + "		DDD 	%.2f" % (DDDCount / triangles * 100) + "   " + str(DDDCount))
print("Total: 100  %.1f" % (TTTProb + TTDProb + TDDProb + DDDProb) + "			Total  	" + str(100) + "    " + str(triangles))	

