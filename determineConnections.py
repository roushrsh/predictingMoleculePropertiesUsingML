#Determines all molecules inbetween and surrounding the two chosen molecules by one hot encoding them between C,O,N,H,F
#this feature doesn't given XYZ coordinates, but it provides the primary connections between the molecules
#Soroush June 2019


import pandas as pd
import numpy as np
import ast

train = open("train8.csv", "r")
file1 = open("lastPieces.csv", "w")
bonds = pd.read_csv("withBonds3.csv")
bonds['atom_index'] = bonds['atom_index'].astype('category')
bonds['atom'] = bonds['atom'].astype('category')
bonds['molecule_name'] = bonds['molecule_name'].astype('category')
bonds['bonds'] = bonds['bonds'].astype('category')
#file1.write("Name,HydrogenIndex,AttachedToIndex,BondType,1JHC,1JHN,2JHC,2JHH,2JHN,3JHC,3JHH,3JHN,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99\n")
importantBond = bonds[['atom_index', 'atom', 'molecule_name', 'bonds']]




dictionaryForCONHF = {
              "C" : "1,0,0,0,0,",
              "O" : "0,1,0,0,0,",
              "N" : "0,0,1,0,0,",
              "H" : "0,0,0,1,0,",
              "F" : "0,0,0,0,1,",
       }

def findFirstFor2Jand3J(indexTrain, nameTrain, bondsPD):
    bondsPD2 = bondsPD.loc[bondsPD['molecule_name'] == nameTrain]
    bondedTo = str((bondsPD2.loc[bondsPD2['atom_index'] == int(indexTrain)]).iloc[0][3]).strip("[]")
    moleculeFound = str(bondsPD2.loc[bondsPD2['atom_index'] == int(bondedTo)].iloc[0][1])

    return(dictionaryForCONHF[moleculeFound])


def oneJtwoJTail():
        file1.write ("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

# whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], importantBond)

def printerRemainder3HException(bondedTo, bondsPD2):
    for x in bondedTo:
        nextToIt = ((bondsPD2.loc[bondsPD2['atom_index'] == int(x)])).iloc[0][1]
        file1.write (dictionaryForCONHF[nextToIt])

    if (len(bondedTo) == 0):
        file1.write ("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
    elif (len(bondedTo) ==1):
        file1.write ("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
    elif(len(bondedTo) == 2):
        file1.write ("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
    elif(len(bondedTo) == 3):
        file1.write ("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
    elif(len(bondedTo) == 4):
        file1.write ("0,0,0,0,0,0,0,0,0,0")
    elif(len(bondedTo) == 5):
        file1.write ("0,0,0,0,0")


def printerRemainder(bondedTo, bondsPD2):
    for x in bondedTo:
        nextToIt = ((bondsPD2.loc[bondsPD2['atom_index'] == int(x)])).iloc[0][1]
        file1.write (dictionaryForCONHF[nextToIt])

    if (len(bondedTo) == 0):
        file1.write ("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,")
    elif(len(bondedTo) ==1):
        file1.write ("0,0,0,0,0,0,0,0,0,0,")
    elif(len(bondedTo) == 2):
        file1.write ("0,0,0,0,0,")

def whatTheNextOrLastMoleculeIsBoundTo(typeOfBond,theHydrogenIndex, whatItIsConnectedToIndex, nameOfIt, bondsPandas):
    bondsPD2 = bondsPandas.loc[bondsPandas['molecule_name'] == nameOfIt]
    whatHydrogenIsConnectedTo = (str(((bondsPD2.loc[bondsPD2['atom_index'] == int(theHydrogenIndex)])).iloc[0][3])).strip("[]")
    bondedTo = str(((bondsPD2.loc[bondsPD2['atom_index'] == int(whatHydrogenIsConnectedTo)])).iloc[0][3])
    #print whatHydrogenIsConnectedTo
    bondedTo = ast.literal_eval(bondedTo)

    if (typeOfBond == "1JHC" or typeOfBond == "1JHN"):
        if theHydrogenIndex in bondedTo:
             bondedTo.remove(int(theHydrogenIndex))
        printerRemainder(bondedTo, bondsPD2)
        file1.write("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,")


    elif(typeOfBond == "2JHC" or typeOfBond == "2JHN" or typeOfBond == "2JHH"):
    #    print bondedTo
    #    print theHydrogenIndex
    #    print whatItIsConnectedToIndex
        if theHydrogenIndex in bondedTo:
           bondedTo.remove(int(theHydrogenIndex))
        if whatItIsConnectedToIndex in bondedTo:
           bondedTo.remove(int(whatItIsConnectedToIndex))

        printerRemainder(bondedTo, bondsPD2)

        theTailList = str(((bondsPD2.loc[bondsPD2['atom_index'] == int(whatItIsConnectedToIndex)]).iloc[0][3]))
        theTailList = ast.literal_eval(theTailList)
        if(len(theTailList) <2):
            file1.write ("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,")
        else:
            if whatHydrogenIsConnectedTo in theTailList:
                   theTailList.remove(int(whatHydrogenIsConnectedTo))
            printerRemainder(theTailList, bondsPD2)


    elif(typeOfBond == "3JHC" or typeOfBond == "3JHN" or typeOfBond == "3JHH"):
        ## I forgot to add what on the one hydrogen connected to is.?
        connectedToH = bondedTo
    #    print connectedToH
        if theHydrogenIndex in connectedToH:
           connectedToH.remove(int(theHydrogenIndex)) #now setup

        whatEndIs = str(((bondsPD2.loc[bondsPD2['atom_index'] == int(whatItIsConnectedToIndex)])).iloc[0][3])
        whatEndIs = ast.literal_eval(whatEndIs)


        #So we have whatEndis. And we have whatHydrogenIsConnectedTo
        inCommon = list(set(whatEndIs).intersection(bondedTo))

        for x in inCommon:
            if x in connectedToH:
                connectedToH.remove(x)
        printerRemainder(connectedToH, bondsPD2)


        printerRemainder(inCommon, bondsPD2)

        theTailList = str(((bondsPD2.loc[bondsPD2['atom_index'] == int(whatItIsConnectedToIndex)]).iloc[0][3]))
        theTailList = ast.literal_eval(theTailList)

        for x in inCommon:
            if (x in theTailList):
                theTailList.remove(int(x))
        printerRemainder(theTailList, bondsPD2)

        listerino = []
        count = 0
        for x in inCommon:
             remainingList = str(((bondsPD2.loc[bondsPD2['atom_index'] == int(x)]).iloc[0][3]))
             remainingList = ast.literal_eval(remainingList)
             listerino = listerino + list(set(remainingList) - set(listerino))
#             print(whatItIsConnectedToIndex)
#             print(whatHydrogenIsConnectedTo)
#             print(listerino)

        if whatItIsConnectedToIndex in listerino:
                            listerino.remove(int(whatItIsConnectedToIndex))  #gave error
        if whatHydrogenIsConnectedTo in listerino:
               listerino.remove(int(whatHydrogenIsConnectedTo))

        printerRemainder3HException(listerino, bondsPD2)


y =0
#next(train)
for x in train:
        line = x.split(",")
        file1.write(str(line[1]) + "," + str(line[2]) + "," + str(line[3]) + "," + str(line[4]) + ",")


        #check for type of connection
        if((str(line[4]) == '1JHC')):  ##If this, then it's auto connected to carbon
            file1.write("1,0,0,0,0,0,0,0,")
            file1.write("1,0,0,0,0,") #Show it's connected to Carbon
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], importantBond)
            oneJtwoJTail()

        elif((str(line[4]) == '1JHN')): ##If this, then it's auto connected to Nitrogen
            file1.write("0,1,0,0,0,0,0,0,")
            file1.write("0,0,1,0,0,") #Show it's connected to Nitrogen
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], importantBond)
            oneJtwoJTail()


        elif((str(line[4]) == '2JHC')):
            file1.write("0,0,1,0,0,0,0,0,")
            file1.write(findFirstFor2Jand3J(line[2], line[1], importantBond))

        #Testing her out
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], importantBond)
            oneJtwoJTail()

        elif((str(line[4]) == '2JHH')):
            file1.write("0,0,0,1,0,0,0,0,")
            file1.write(findFirstFor2Jand3J(line[2], line[1], importantBond))
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], importantBond)

            oneJtwoJTail()

        elif((str(line[4]) == '2JHN')):
            file1.write("0,0,0,0,1,0,0,0,")
            file1.write(findFirstFor2Jand3J(line[2], line[1], importantBond))
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], importantBond)
            oneJtwoJTail()

        elif((str(line[4]) == '3JHC')):
            file1.write("0,0,0,0,0,1,0,0,")
            file1.write(findFirstFor2Jand3J(line[2], line[1], importantBond))
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], importantBond)

        elif((str(line[4]) == '3JHH')):
            file1.write("0,0,0,0,0,0,1,0,")
            file1.write(findFirstFor2Jand3J(line[2], line[1], importantBond))
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], importantBond)

        elif((str(line[4]) == '3JHN')):
            file1.write("0,0,0,0,0,0,0,1,")
            file1.write(findFirstFor2Jand3J(line[2], line[1], importantBond))
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], importantBond)


        file1.write("\n")
    #    y = y+1
    #    if (y==100):
    #        break
##For x in train go through each line
