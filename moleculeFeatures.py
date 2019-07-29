#Determines all molecules inbetween and surrounding the two chosen molecules by one hot encoding them between C,O,N,H,F
#this feature doesn't given XYZ coordinates, but it provides the primary connections between the molecules
#Soroush June 2019

import pandas as pd
import numpy as np
import ast


train = open("train.csv", "r")

file1 = open("file1.csv", "w")

bonds = pd.read_csv("withBonds.csv")

file1.write("Name,1JHC,1JHN,2JHC,2JHH,2JHN,3JHC,3JHH,3JHN,Ca1,Oa1,Na1,Ha1,Fa1,Cb1,Ob1,Nb1,Hb1,Fb1,Cb2,Ob2,Nb2,Hb2,Fb2,Cb3,Ob3,Nb3,Hb3,Fb3,Cb4,Ob4,Nb4,Hb4,Fb4,Cca1,Oca1,Nca1,Hca1,Fca1,Ccb1,Ocb1,Ncb1,Hcb1,Fcb1,Cca2,Oca2,Nca2,Hca2,Fca2,Ccb2,Ocb2,Ncb2,Hcb2,Fcb2,Cca3,Oca3,Nca3,Hca3,Fca3,Ccb3,Ocb3,Ncb3,Hcb3,Fcb3,Cda1,Oda1,Nda1,Hda1,Fda1,Cda2,Oda2,Nda2,Hda2,Fda2,Cda3,Oda3,Nda3,Hda3,Fda3,x1,y1,z1,x2,y2,z2,distance\n")

#print bonds

dictionaryForCONHF = {
		"C" : "1,0,0,0,0",
		"O" : "0,1,0,0,0",
		"N" : "0,0,1,0,0",
		"H" : "0,0,0,1,0",
		"F" : "0,0,0,0,1",
	}

def findFirstFor2Jand3J(indexTrain, nameTrain, bondsPD):
    bondsPD2 = bondsPD.loc[bondsPD['molecule_name'] == nameTrain]
    bondedTo = str((bondsPD2.loc[bondsPD2['atom_index'] == int(indexTrain)]).iloc[0][3])[1]
    moleculeFound = str(bondsPD2.loc[bondsPD2['atom_index'] == int(bondedTo)].iloc[0][1])

    if(moleculeFound == "C"):
        return("1,0,0,0,0")
    elif(moleculeFound == "O"):
        return("0,1,0,0,0")
    elif(moleculeFound == "N"):
        return("0,0,1,0,0")
    elif(moleculeFound == "H"):
        return("0,0,0,1,0")
    else:
        return("0,0,0,0,1")

def oneJtwoJTail():
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
# whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']])

def printerRemainder3HException(bondedTo, bondsPD2):
    for x in bondedTo:
        nextToIt = ((bondsPD2.loc[bondsPD2['atom_index'] == int(x)])).iloc[0][1]
        print dictionaryForCONHF[nextToIt]

    if (len(bondedTo) == 0):
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
    elif (len(bondedTo) ==1):
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
    elif(len(bondedTo) == 2):
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
    elif(len(bondedTo) == 3):
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
    elif(len(bondedTo) == 4):
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
    elif(len(bondedTo) == 5):
        print ("0,0,0,0,0")


def printerRemainder(bondedTo, bondsPD2):
    for x in bondedTo:
        nextToIt = ((bondsPD2.loc[bondsPD2['atom_index'] == int(x)])).iloc[0][1]
        print dictionaryForCONHF[nextToIt]

    if (len(bondedTo) == 0):
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
    elif(len(bondedTo) ==1):
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
    #    print ("\n")
    elif(len(bondedTo) == 2):
        print ("0,0,0,0,0")
        #print ("\n")
#    print ("0,0,0,0,0")
#    print ("0,0,0,0,0")
#    print ("0,0,0,0,0")
#    print "\n"
    #elif (len(bondedTo) ==3):
        #print("3")
    #    print ("\n")'''

def whatTheNextOrLastMoleculeIsBoundTo(typeOfBond,theHydrogenIndex, whatItIsConnectedToIndex, nameOfIt, bondsPandas):
    bondsPD2 = bondsPandas.loc[bondsPandas['molecule_name'] == nameOfIt]
    whatHydrogenIsConnectedTo = str(((bondsPD2.loc[bondsPD2['atom_index'] == int(theHydrogenIndex)])).iloc[0][3])[1]
    bondedTo = str(((bondsPD2.loc[bondsPD2['atom_index'] == int(whatHydrogenIsConnectedTo)])).iloc[0][3])
    bondedTo = ast.literal_eval(bondedTo)
    #XYZDist = str(((bondsPD2.loc[bondsPD2['atom_index'] == int(theHydrogenIndex)])).iloc[0][3])[1]
    #InCommon


#    if(typeOfBond == "3JHC" or typeOfBond == "3JHN" or typeOfBond == "3JHH"):
#        bondedTo.remove(int(theHydrogenIndex))
#        print(bondedTo)

    if (typeOfBond == "1JHC" or typeOfBond == "1JHN"):
        # print bondsPD2
    #    print "\n"
        bondedTo.remove(int(theHydrogenIndex))
        #print bondedTo
        '''
        for x in bondedTo:
            nextToIt = ((bondsPD2.loc[bondsPD2['atom_index'] == int(x)])).iloc[0][1]
            print dictionaryForCONHF[nextToIt]

        if (len(bondedTo) ==1):
            print ("0,0,0,0,0")
            print ("0,0,0,0,0")
        #    print ("\n")
        elif(len(bondedTo) == 2):
            print ("0,0,0,0,0")
            #print ("\n")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print ("0,0,0,0,0")
        print "\n"
        #elif (len(bondedTo) ==3):
            #print("3")
        #    print ("\n")'''
        printerRemainder(bondedTo, bondsPD2)
        print("0,0,0,0,0")
        print("0,0,0,0,0")
        print("0,0,0,0,0")

        #printerRemainder(bondedTo, bondsPD2)

    elif(typeOfBond == "2JHC" or typeOfBond == "2JHN" or typeOfBond == "2JHH"):
    #    print len(bondedTo)
        if(len(bondedTo) > 2):
            bondedTo.remove(int(theHydrogenIndex))
            bondedTo.remove(int(whatItIsConnectedToIndex))
            '''
            for x in bondedTo:
        else:
                nextToIt = ((bondsPD2.loc[bondsPD2['atom_index'] == int(x)])).iloc[0][1]
                print dictionaryForCONHF[nextToIt]

            if(len(bondedTo) == 1):
                print ("0,0,0,0,0")
                print ("0,0,0,0,0")
            else:
                print ("0,0,0,0,0")
        else:
            print ("0,0,0,0,0")
            print ("0,0,0,0,0")
            print ("0,0,0,0,0")'''
            printerRemainder(bondedTo, bondsPD2)
        #Now need to take last C, remove main C, print rest

        #print typeOfBond
        theTailList = str(((bondsPD2.loc[bondsPD2['atom_index'] == int(whatItIsConnectedToIndex)]).iloc[0][3]))
        theTailList = ast.literal_eval(theTailList)

    #    print theTailList
        if(len(theTailList) <2):
            print ("0,0,0,0,0")
            print ("0,0,0,0,0")
            print ("0,0,0,0,0")
    #        print("")
        else:
            theTailList.remove(int(whatHydrogenIsConnectedTo))
        #    print theTailList        print("0,0,0,0,0")

            printerRemainder(theTailList, bondsPD2)
    elif(typeOfBond == "3JHC" or typeOfBond == "3JHN" or typeOfBond == "3JHH"):
        whatEndIs = str(((bondsPD2.loc[bondsPD2['atom_index'] == int(whatItIsConnectedToIndex)])).iloc[0][3])
        whatEndIs = ast.literal_eval(whatEndIs)
        #So we have whatEndis. And we have whatHydrogenIsConnectedTo
        inCommon = list(set(whatEndIs).intersection(bondedTo))
        printerRemainder(inCommon, bondsPD2)

        theTailList = str(((bondsPD2.loc[bondsPD2['atom_index'] == int(whatItIsConnectedToIndex)]).iloc[0][3]))
        theTailList = ast.literal_eval(theTailList)
        for x in inCommon:
            if (x in theTailList):
                theTailList.remove(int(x))
        printerRemainder(theTailList, bondsPD2)

    #    print inCommon
        listerino = []
        for x in inCommon: #remaining ones on atom right before  secondIndex/connected molecule
            remainingList = str(((bondsPD2.loc[bondsPD2['atom_index'] == int(x)]).iloc[0][3]))
    #        print str(((bondsPD2.loc[bondsPD2['atom_index'] == int(x)])))
            listerino = ast.literal_eval(remainingList)
        listerino.remove(int(whatItIsConnectedToIndex))
        listerino.remove(int(whatHydrogenIsConnectedTo))
        printerRemainder3HException(listerino, bondsPD2)

    #        for y in remainingList:
    #            rest = str(((bondsPD2.loc[bondsPD2['atom_index'] == int(y)]).iloc[0][3]))
    #            rest = ast.literal_eval(rest)
    #            listerino.append(rest)
#        flat_list = []
#        for sublist in listerino:
#            for item in sublist:
#                flat_list.append(item)
#        uniqued = list(set(flat_list))
    #    print listerino
        #    listerino = listerino.append(remainingList)
    #        remainingList.remove(int(whatItIsConnectedToIndex))
    #        remainingList.remove((bondedTo))
    #        print remainingList
    #    print uniqued
    #    print whatItIsConnectedToIndex
    #    uniqued.remove(int(whatItIsConnectedToIndex))
    #    print
#        print uniqued



y =0
for x in train:
    #Condition1 to skip first line
        if y == 0:
            y = y+1
            continue
    #    print bonds#[['molecule_name', 'atom_index', 'molecule_name', 'bonds']]
        #split by ,
        line = x.split(",")
        print(str(line[1]))
        print(str(line[2]))
        print(str(line[3]))
        print(str(line[4]))


        #check for type of connection
        if((str(line[4]) == '1JHC')):  ##If this, then it's auto connected to carbon
    #        file1.write("1,0,0,0,0,0,0,0,")
            print ("1,0,0,0,0,0,0,0,")
    #        file1.write("1,0,0,0,0") #Show it's connected to Carbon
            print("1,0,0,0,0") #Show it's connected to Carbon
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']])
            oneJtwoJTail()

        elif((str(line[4]) == '1JHN')): ##If this, then it's auto connected to Nitrogen
        #    file1.write("0,1,0,0,0,0,0,0,")
            print("0,1,0,0,0,0,0,0,")
        #    file1.write("0,0,1,0,0") #Show it's connected to Nitrogen
            print("0,0,1,0,0")
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']])
            oneJtwoJTail()

        elif((str(line[4]) == '2JHC')):
        #    file1.write("0,0,1,0,0,0,0,0,")
            print ("0,0,1,0,0,0,0,0,")
        #    file1.write(findFirstFor2Jand3J(line[2], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']]))
            print findFirstFor2Jand3J(line[2], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']])
        #Testing her out
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']])
            oneJtwoJTail()

        elif((str(line[4]) == '2JHH')):
        #    file1.write("0,0,0,1,0,0,0,0,")
            print ("0,0,0,1,0,0,0,0,")
        #    file1.write(findFirstFor2Jand3J(line[2], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']]))
            print (findFirstFor2Jand3J(line[2], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']]))
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']])
            oneJtwoJTail()

        elif((str(line[4]) == '2JHN')):
        #    file1.write("0,0,0,0,1,0,0,0,")
            print("0,0,0,0,1,0,0,0,")
        #    file1.write(findFirstFor2Jand3J(line[2], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']]))
            print (findFirstFor2Jand3J(line[2], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']]))
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']])
            oneJtwoJTail()

        elif((str(line[4]) == '3JHC')):
        #    file1.write("0,0,0,0,0,1,0,0,")
            print("0,0,0,0,0,1,0,0,")
        #    file1.write(findFirstFor2Jand3J(line[2], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']]))
            print file1.write(findFirstFor2Jand3J(line[2], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']]))
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']])

        elif((str(line[4]) == '3JHH')):
        #    file1.write("0,0,0,0,0,0,1,0,")
            print("0,0,0,0,0,0,1,0,")
        #    file1.write(findFirstFor2Jand3J(line[2], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']]))
            print(findFirstFor2Jand3J(line[2], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']]))
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']])

        elif((str(line[4]) == '3JHN')):
        #   file1.write("0,0,0,0,0,0,0,1,")
            print("0,0,0,0,0,0,0,1,")
        #    file1.write(findFirstFor2Jand3J(line[2], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']]))
            print (findFirstFor2Jand3J(line[2], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']]))
            whatTheNextOrLastMoleculeIsBoundTo(line[4],line[2],line[3], line[1], bonds[['atom_index', 'atom', 'molecule_name', 'bonds']])


        print("\n")
        #file1.write("\n\n")
        if y == 100 :
            break
        y = y+1

##For x in train go through each line
