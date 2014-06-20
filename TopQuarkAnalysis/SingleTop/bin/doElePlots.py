#!/usr/bin/python                                                                                                                                                      
#Functions
from macroFunctionsEle import *

#Default
categories = ["2J_0T","2J_1T","2J_2T","3J_1T","3J_2T","4J_2T"]
#categories = ["2J_0T"]
#cuts = ["","SR","SB",
#        "Plus","SRPlus","SBPlus",
#        "Minus","SRMinus","SBMinus",
#        ]
cuts = ["noQCDCut"]

#To use:
#categories = ["2J_2T","3J_2T"]
#categories = ["2J_0T"]

#variables = ["eta","metPt","topMass","costhetalj"]
variables = ["topMass","metPt","costhetalj","mtwMass","leptonPt","bJetPt","topPt","DeltaR_lep_leadingjet","firstJetPt","secondJetPt","thirdJetPt","leptonRelIso"]

#Add data-driven normalization:
addDDNormalization =0 
#addDDNormalization = 1
addNormalization = 1

#Leptons to consider:
#Leptons = ["Mu","Ele"]
#Leptons = ["Ele"]

lepton = "Ele"


#Initialization
filesToRun = []

import os
import re
import sys
import commands

categoryOld = "mysample"
variableOld = "eta"

command_ls = "ls *.C | grep Plots | grep Template | grep "+lepton+" | grep " + categoryOld + " | grep " + variableOld 
fileNames = commands.getoutput(command_ls).split('\n')
	
for fileName in fileNames:
    if "inclusive" in fileNames: continue
    for categoryNew in categories:
        os.system("mkdir "+ categoryNew + "_" + lepton)
	for variableNew in variables:
	    for cut in cuts:
	        fileNameNew = fileName.replace("Template_","")  
		fileNameNew = fileNameNew.replace(categoryOld,categoryNew)
		if (cut != ""):
		   fileNameNew = fileNameNew.replace(categoryNew,categoryNew+"_"+cut)
		fileNameNew = fileNameNew.replace(variableOld,variableNew)
		print fileName  
		print fileNameNew 
		file = open(fileName)
		lines = file.readlines()
		newFile = open(fileNameNew,"w")
		for line in lines:
		    newLine = line
		    words = line.split()
		    for word in words:
		        if categoryOld in word:
			    print "line before categ "+str(line)
			    newLine = line.replace(word,word.replace(categoryOld,categoryNew))
			    print "line after categ "+str(newLine)
			variableInLine = "\"" + variableOld + "\""
			if variableInLine in word and "observable" in line:
			    print "line before obs " + str(line)
			    newLine = listSamples(variableNew,categoryNew)
			    print "line after obs " + str(newLine)
		    if "TString KinCut=\"\"" in line:
		       print "line before cut "+line
		       newLine = listCuts (cut,categoryNew,lepton)
		       print "line after cut " +newLine
                    if "TString KinCutQCDDD=\"\"" in line:
                        print "line before cut "+line
                        newLine = listCutsQCD (cut,categoryNew,lepton)
                        print "line after cut " +newLine
		    if addDDNormalization and "bool scaleToData" in line:
		       newLine = line + listNormalizations(cut,categoryNew,lepton)
                    if addNormalization and "TTBarScale"  in line:
                        print "line before cut "+line
                        newLine = line + listNormalizations(cut,categoryNew,lepton)
                        print "line after cut " +newLine
		    if "SaveAs" in line and cut !="":
		       print line
		       newLine = line.replace("sample","sample"+"+\"_" +cut + "\"")
		       print newLine
		    if "SaveAs" in line and addDDNormalization==1:
		       print line
		       newLine = newLine.replace("sample","sample"+"+\"_DDNorm\"")
		       print newLine
#		    if "stringCharge=TString" in word:
#		       print line
#		       newLine = stringCharge(cut)
#		       print newLine
		    newFile.write(str(newLine) )   
		newFile.close()    
		filesToRun.append(fileNameNew)
print "files to run:"
	
nSimultaneous = 8
nstart = 0
for file in filesToRun:
    nstart = nstart + 1
    if nstart % nSimultaneous ==0 :
        command_root = "root -q -b -l " + file 
    else: command_root = "root -q -b -l " + file + " &"
    print command_root
    os.system(command_root)

#for file in filesToRun:
#    command_rm = "rm " + file
#    print command_rm
#    os.system(command_rm)
