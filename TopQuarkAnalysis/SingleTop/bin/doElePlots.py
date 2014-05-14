#!/usr/bin/python                                                                                                                                                      
#Functions
from macroFunctions import *

#Default
categories = ["2J_1T","3J_1T","3J_2T","2J_0T"]
cuts = ["","SR","SB",
        "Plus","SRPlus","SBPlus",
        "Minus","SRMinus","SBMinus",
        ]
cuts = [""]

#To use:
categories = ["2J_2T","3J_2T"]
categories = ["2J_0T"]

variables = ["eta","metPt","topMass"]

#Add data-driven normalization:
addDDNormalization =0 
addDDNormalization = 1

#Leptons to consider:
Leptons = ["Mu","Ele"]
Leptons = ["Ele"]

#Main plots
#variables = ["topMass","topMass_best","costhetalj","costhetalj_best","leptonPt","mtwMass","metPt","Pt_lepton_secondJet","Pt_lepton_firstJet",
#             "DeltaR_lepton_secondJet","DeltaR_firstJet_secondJet","HT","Pt_firstJet_secondJet","BDT",
#			 "Mlb2","Mlb1","topEta_best","topPt","topEta"]
#variables = ["DeltaR_firstJet_secondJet","thirdJetPt","metPt","Pt_firstJet_secondJet","DeltaR_lepton_secondJet","costhetalj_best","leptonDeltaCorrectedRelIso","leptonRhoCorrectedRelIso"]

variables = ["mtwMass","metPt","top_recoiledb_deltaPhi","Mlb2","costhetalj_best","b1b2Pt", "first_secondJetsDeltaR",
             "leptonPt","topMass_best","recoiledb_leptonDeltaR","HT"]

variables = ["fJetEta","HT","mtwMass","b1b2Pt","Mlb2","first_secondJetsDeltaR"]
variables = ["metPt","leptonPt" ,"mtwMass" ,"topMass_best" ,"leptonRhoCorrectedRelIso", "cosLepMetPhi"]
addDDNormalization = 1
#Test
#categories = ["2J_1T"]#cuts = ["SR","SB"]#variables = ["eta"]


#Script running:
#Initialization
filesToRun = []

import os
import re
import sys
import commands

categoryOld = "3J_2T"
variableOld = "eta"

for lepton in Leptons:
	command_ls = "ls *.C | grep Plots | grep Template | grep "+lepton+" | grep " + categoryOld + " | grep " + variableOld 
	fileNames = commands.getoutput(command_ls).split('\n')
	
	for fileName in fileNames:
	    if "inclusive" in fileNames: continue
	    for categoryNew in categories:
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
	                    if addDDNormalization and "bool scaleToData" in line:
	                        newLine = line + listNormalizations(cut,categoryNew,lepton)
	                    if "SaveAs" in line and cut !="":
	                        print line
	                        newLine = line.replace("sample","sample"+"+\"_" +cut + "\"")
	                        print newLine
	                    if "SaveAs" in line and addDDNormalization==1:
	                        print line
	                        newLine = newLine.replace("sample","sample"+"+\"_DDNorm\"")
	                        print newLine
			    if "stringCharge=TString" in word:
				print line
				newLine = stringCharge(cut)
				print newLine
	                    newFile.write(str(newLine) )   
	                    #if "tex->Draw()" in line:
	                    #    newFile.write(CompatibilityTests);
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
