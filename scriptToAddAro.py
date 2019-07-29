import pandas as pd

#Once the arrow file is generated, merging and adding it to each test/train file in clean
#columns so as to feed into learning model better
train = open("test.csv", "r")
newTrain = open("newTest.csv", "w")
pandaAro = pd.read_csv("wB3AroFToAdd.csv")
train.next()
newTrain.write("OnAromaticH,AromaticOther,OnAromaticOther\n")
temp = ""
for x in train:
    name = x.split(",")[1]
    atom_index = x.split(",")[2]
    otherAtom = x.split(",")[3]
    if(temp!= name):
        toWrite1 = pandaAro.loc[pandaAro['molecule_name'] == name]
#    toWrite2a = str(toWrite1.loc[toWrite1['atom_index'] == int(atom_index)].iloc[0][12])
    toWrite2b = str(toWrite1.loc[toWrite1['atom_index'] == int(atom_index)].iloc[0][13])

    toWrite3a = str(toWrite1.loc[toWrite1['atom_index'] == int(otherAtom)].iloc[0][12])
    toWrite3b = str(toWrite1.loc[toWrite1['atom_index'] == int(otherAtom)].iloc[0][13])


    newTrain.write((toWrite2b))
    newTrain.write(",")
    newTrain.write((toWrite3a))
    newTrain.write(",")
    newTrain.write((toWrite3b))
    newTrain.write("\n")
    temp = name




#print pandaAro


#    bondedTo = str((bondsPD2.loc[bondsPD2['atom_index'] == int(indexTrain)]).iloc[0][3]).strip("[]")
