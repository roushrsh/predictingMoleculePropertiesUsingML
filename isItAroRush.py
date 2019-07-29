#Script to determine if the H is on an aromatic molecule, if the other molecule is on an aromatic molecule, or if the other molecule is part of an aromatic molecule
#Specifically a benzene ring
#Roush
import pandas as pd
toGoThrough = open("specificWithBonds.csv", "r")
isItAro2 = pd.read_csv("specificWithBonds.csv")

fileToWrite = open("AroOrNot.csv", "w")

bonds =0
import ast

count = 0
partOfRing = False

def recursiveCheck(atomNameStart, atomPositionStart, isItAroDF, listToAddTo, count, partOfRing, atomName, lastAtomPosition, isAro, FINALAPPEND, actualpositionStart, lastGodDamnList):
	Found = False
	ActualAppend = []
	if(partOfRing == False):
		if(atomNameStart == "C"):
			partOfRing = True
	count = count+1



	if (len(listToAddTo) == 6):
		connectionsTres = (isItAroDF.loc[isItAro['atom_index'] == int(listToAddTo[5])].iloc[0][3]).strip("[]").split(",")
		connectionsTres = map(int, connectionsTres)

		if (int(actualpositionStart) in connectionsTres):
			Found = True
			lastGodDamnList.append("Aromatic")

	if (len(listToAddTo) == 7):
		connectionsTres = (isItAroDF.loc[isItAro['atom_index'] == int(listToAddTo[6])].iloc[0][3]).strip("[]").split(",")
		connectionsTres = map(int, connectionsTres)

		if (listToAddTo[1] in connectionsTres):
			Found = True
			lastGodDamnList.append("OnRing")

	atomConnections = (isItAroDF.loc[isItAro['atom_index'] == int(atomPositionStart)].iloc[0][3])
	atomConnections = ast.literal_eval(atomConnections)
	for x in atomConnections:
		if (x not in listToAddTo or (x == actualpositionStart & count > 7)):
			if (count > 7):

				break
			atom2 = (isItAroDF.loc[isItAro['atom_index'] == int(x)]).iloc[0][1]	
			stringAtomName = str(atom2)
			position2 = (isItAroDF.loc[isItAro['atom_index'] == int(x)]).iloc[0][2]

			listToAddTo.append(x)
			a = (recursiveCheck(atomNameStart, position2, isItAro, listToAddTo, count, partOfRing, stringAtomName, position2, isAro, FINALAPPEND, actualpositionStart, lastGodDamnList))
			listToAddTo.remove(x)

				
			if (Found == True):
				return ActualAppend
	return (lastGodDamnList)



#toGoThrough.next()
for x in toGoThrough: 
#	print x
	isItAro = isItAro2.loc[isItAro2['molecule_name'] == (str(x.split(",")[0]))]
 	listerinoA= (recursiveCheck(str(x.split(",")[1]), str(x.split(",")[2]), isItAro, [int(x.split(",")[2])], 0, partOfRing, "Z", -1, "Not Aroooooo", [], int(x.split(",")[2]), [] ))
#	print listerinoA

	if ('Aromatic' in listerinoA):
		fileToWrite.write("Aromatic,1,0,0\n")
	elif('OnRing' in listerinoA):
		fileToWrite.write("OnRing,0,1,0\n")
	else:
		fileToWrite.write("Neither,0,0,1\n")

#	print " "

