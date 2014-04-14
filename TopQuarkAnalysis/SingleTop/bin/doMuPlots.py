#!/usr/bin/python                                                                                                                                                      
#Functions
from macroFunctions import *

#Default
#categories = ["2J_1T","3J_1T","3J_2T","2J_0T"]
#cuts = ["","SR","SB",
#        "Plus","SRPlus","SBPlus",
#        "Minus","SRMinus","SBMinus",
#        ]


#categories = ["2J_2T","3J_2T"]
#categories = ["2J_2T"]
#categories = ["3J_2T"]
categories = ["NJets"] 
cuts = ["noQCDCut"] ##,"noQCDCut_mtwCut"]
#cuts = [""] ##,"noQCDCut_mtwCut"]

#Main plots

#variables = ["leptonDeltaCorrectedRelIso","bJetDecPt","bJetFinPt","mtwMass","topMass","topMassLR","leptonPt","metPt","HT","costhetalbl_new","costhetalj_new","b1b2Pt","b1b2Mass","DeltaR_b1b2","Mlb2","Mlb1","cosLepMetPhi","DeltaPhi_topbJetFin","thirdJetPt"]

#variables = ["leptonDeltaCorrectedRelIso","mtwMass","topMass_best","leptonPt","metPt","cosLepMetPhi"]                                     ## for 2J0T NEW
#variables = ["cosLepMetPhi"]                                                                                                              ## for 2J0T NEW

#variables = ["mtwMass","topMassLR","leptonPt","metPt","HT","costhetalbl_new","b1b2Pt","DeltaR_b1b2","Mlb2","DeltaPhi_topbJetFin"]     ## for 2J2T

#variables = ["mtwMass","metPt","costhetalj_new","b1b2Pt","b1b2Mass","thirdJetPt","eta"]                                               ## for 3J2T

#variables = ["mtwMass","topMass_best","leptonPt","metPt","HT","costhetalbl_best","b1b2Pt","DeltaR_b1b2","Mlb2","DeltaPhi_besttopbJetRecoil"]     ## for 2J2T NEW
#variables = ["DeltaPhi_besttopbJetRecoil"]                                                                                                       ## for 2J2T NEW

#variables = ["mtwMass","metPt","costhetalj_bJet","b1b2Pt","b1b2Mass","thirdJetPt","eta"]                                                         ## for 3J2T NEW
#variables = ["eta"]                                                                                                                             ## for 3J2T NEW

#variables = ["mtwMass","metPt","fJetPt","bJetPt","leptonPt","leptonRelIso"]
variables = ["nJ"]



#variables = ["leptonPt","HT"] ##,"topMass_best","b1b2Pt"]     ## for 2J2T NEW


#variables = ["BDT","BDT3J2T"]
#variables = ["BDT"]


#variables = ["DeltaPhi_topbJetFin"]  #,"costhetalj_new","DeltaR_b1b2","metPt",,"mtwMass""Mlb1","Mlb2"]
#variables = ["mtwMass","metPt","topMassLR","eta","costhetalbl_new","topMass"]
#variables = ["metPt","mtwMass"]
#variables = ["Comb1","Comb2"]
#variables = ["costhetalj"]  ##,"b1b2Mass","b1b2Pt"]
#variables = ["DeltaPhi_topbJetFin"]  ##,"b1b2Mass","b1b2Pt"]
#variables = ["DeltaEta_b1b2","DeltaPhi_b1b2","b1b2Pt","b1b2Mass"]  ##,"b1b2Mass","b1b2Pt"]
#variables = ["b1b2Pt"]  ##,"b1b2Mass","b1b2Pt"]


addDDNormalization =0 
#addDDNormalization = 1
addNormalization = 1

lepton = "Ele"
lepton = "Mu"

Leptons = ["Mu"] ##,"Ele"]


#variables = ["topMass","eta","costhetalj","leptonPt","mtwMass","metPt"]


#Initialization
filesToRun = []

import os
import re
import sys
import commands

categoryOld = "3J_2T"
variableOld = "eta"


command_ls = "ls *.C | grep Plots | grep Template | grep "+lepton+" | grep " + categoryOld + " | grep " + variableOld 
#command_ls = "ls *.C | grep Plots | grep Template | grep "+lepton+" | grep " + categoryOld + " | grep " + variableOld + " | grep errbands "
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
                    if "TString KinCutQCDDD=\"\"" in line:
                        print "line before cut "+line
                        newLine = listCutsQCD (cut,categoryNew,lepton)
                        print "line after cut " +newLine
#                    if "TString cutData=\"1.\"" in line:
#                        print "line before cut "+line
#                        newLine = listCutsData (cut,categoryNew,lepton)
#                        print "line after cut " +newLine                            
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
