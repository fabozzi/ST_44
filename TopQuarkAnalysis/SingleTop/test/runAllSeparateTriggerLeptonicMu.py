#!/usr/bin/env cmsRun
import FWCore.ParameterSet.Config as cms
import os,sys,re,shutil


#Original config file
fileName = "SingleTopSystematicsWithTriggerLeptonicMu_cfg.py"
#fileName = "SingleTopPDFWithTrigger_cfg.py"
#fileName = "SingleTopSystematics_cfg.py"
#fileName = "SingleTopSystematics_split_cfg.py"
#fileName = "SingleTopNEvents_cfg.py"

nSimultaneous = 4


#Channels to include
channels = [

"Mu_2011A_08Nov_part_1",
"Mu_2011A_08Nov_part_2",
"Mu_2011A_08Nov_part_3",
"Mu_2011A_08Nov_part_4",
"Mu_2011A_08Nov_part_5",
"Mu_2011A_08Nov_part_6",
"Mu_2011A_08Nov_part_7",
"Mu_2011A_08Nov_part_8",
"Mu_2011A_08Nov_part_9",
"Mu_2011A_08Nov_part_10",
"Mu_2011A_08Nov_part_11",
"Mu_2011A_08Nov_part_12",
"Mu_2011A_08Nov_part_13",
"Mu_2011A_08Nov_part_14",
"Mu_2011A_08Nov_part_15",

  ### 
 ]

#Path to take data merged files
#dataPath = "rfio:/castor/cern.ch/user//m/mmerola/SingleTop_2012/MergedJune/"
dataPath = "file:/data3/scratch/users/fabozzi/SingleTop/ntp14apr14_Merged/"

#Choose if you want to run or just prepare the configuration files
#mode = ""
#mode = "cmsRun"
mode = "qsub"


#Use mu , ele or both

channel_instruction = "all"

#Implementation:

#Function to replace a sequence of characters channelOld to channelNew in a file 
def changeChannel(fileName,channelOld,channelNew,switch,isMC): 
    print " Channel test " + channelNew
    channelToReplace = channelNew
    if "Data" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "Data"
    if ("Mu" in channelNew or "Ele" in channelNew) and not "QCDMu" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "Data"
    if "WJets_wlight" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "WJets_wlight"
    if "WJets_wcc" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "WJets_wcc"
    if "WJets_wbb" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "WJets_wbb"
    if "WJetsQ2up" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "WJetsQ2up"
    if "WJetsQ2down" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "WJetsQ2down"
    if "WJets" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "WJets"
    if "W1Jet" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "W1Jet"
    if "W2Jets" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "W2Jets"
    if "W3Jets" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "W3Jets"
    if "W4Jets" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "W4Jets"                
    if "ZJets" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "ZJets"
    if "ZJets_wlight" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "ZJets_wlight"
    if "ZJets_wcc" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "ZJets_wcc"
    if "ZJets_wbb" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "ZJets_wbb"
    if "TTBar" in channelNew and not "Q2" in channelNew and not "Matching" in channelNew:  #=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "TTBar"
    if "TTBarQ2up" in channelNew : #=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "TTBarQ2up"
    if "TTBarQ2down" in channelNew : #=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "TTBarQ2down"
    if "TTBarMatchingup" in channelNew : #=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "TTBar_MatchingUp"
    if "TTBarMatchingdown" in channelNew : #=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "TTBar_MatchingDown"                
    if "TChannel" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "TChannel"        
    if "TbarChannel" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "TbarChannel"        
    if "QCDMu" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "QCDMu"
    if "WW" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "WW"        
    if "WZ" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "WZ"        
    if "ZZ" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "ZZ"        
          #if channelNew=="DataEle":
       # channelNew_2 = "Data"

    file = open(fileName)
    lines = file.readlines()
    o = open(channelNew+"_cfg.py","w") 
    for line in lines:
        print "THIS IS THE LINE: ", line
        if '"channel_instruction"' in line:
#            print "BEFORE ", line
            line = line.replace('"channel_instruction"','"'+switch+'"')
            print "AFTER REPLACE ", line
        if "MC_instruction" in line and "False" in line:
       #     if "False" in line:
#            print line
            line = line.replace("False",isMC)
            print "AFTER REPLACE: ", line
        words = line.split()
        for word in words:
            if channelOld in word:  
                #                print " line old " + line
                if (not switch == "all") and ("process.TFileService" in line):
                    line = line.replace(word,word.replace(channelOld,channelNew+"_HLT_IsoMu17"))
#                    line = line.replace(word,word.replace(channelOld,channelNew))
                    print "process.TFileService in line,switch " + switch +" line: \n" +line
                else:
                    line = line.replace(word,word.replace(channelOld,channelToReplace))
        print "WRITING LINE = ", line
        o.write(line)   
    #if channel == "Data":#Temporary inelegant solution due to the separation of mu/e: will fix it at some point
        #        line = "process.source.fileNames = cms.untracked.vstring('"+dataPath+"DataMuMerged.root','"+dataPath+"DataEleMerged.root',)"
        #        line = "process.source.fileNames = cms.untracked.vstring('"+dataPath+"DataMuMerged.root',)"
        #       line = "process.source.fileNames = cms.untracked.vstring('"+dataPath+"Mu_v1Merged.root','"+dataPath+"Mu_v2Merged.root','"+dataPath+"Ele_v1Merged.root','"+dataPath+"Ele_v2Merged.root',)"
    if "WJets" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channel+"Merged.root',"
        #        inputs = inputs.replace(channelToReplace,"WJets")
        inputs = inputs +")"
        o.write(inputs)
    if "QCDMu" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        #        inputs = inputs.replace(channelToReplace,"QCDMu")
        inputs = inputs +")"
        print "inputs = ", inputs
        o.write(inputs)        
    if "WJetsQ2up" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        inputs = inputs.replace(channelToReplace,"WJetsQ2up")
        inputs = inputs +")"
        o.write(inputs)
    if "WJetsQ2down" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        inputs = inputs.replace(channelToReplace,"WJetsQ2down")
        inputs = inputs +")"
        o.write(inputs)
    if "W1Jet" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        inputs = inputs.replace(channelToReplace,"W1Jet")
        inputs = inputs +")"
        o.write(inputs)
    if "W2Jets" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        inputs = inputs.replace(channelToReplace,"W2Jets")
        inputs = inputs +")"
        o.write(inputs)
    if "W3Jets" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        inputs = inputs.replace(channelToReplace,"W3Jets")
        inputs = inputs +")"
        o.write(inputs)
    if "W4Jets" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        inputs = inputs.replace(channelToReplace,"W4Jets")
        inputs = inputs +")"
        o.write(inputs)        
    if "ZJets" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        inputs = inputs.replace(channelToReplace,"ZJets")
        inputs = inputs +")"
        o.write(inputs)
    if (("Mu" in channelNew) or ("Ele" in channelNew)) and (not("QCD" in channelNew)) :# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
#        inputs = inputs +"'"+dataPath+"Mu_v4p1Merged.root',"
#        inputs = inputs +"'"+dataPath+"Mu_v4p2Merged.root',"
#        inputs = inputs +"'"+dataPath+"Mu_v4p3Merged.root',"
#        inputs = inputs +"'"+dataPath+"Mu_v4Merged.root',"
#        inputs = inputs +"'"+dataPath+"Mu_v2Merged.root',"
        inputs = inputs +")"
        print "inputs = ", inputs
        o.write(inputs)
    if "TTBar" in channelNew and not "Q2" in channelNew and not "Matching" in channelNew: # == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        #    inputs = inputs.replace(channelToReplace,"TTBar")
        inputs = inputs +")"
        o.write(inputs)
    if "TTBarQ2up" in channelNew : # == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        #    inputs = inputs.replace(channelToReplace,"TTBarQ2up")
        inputs = inputs +")"
        o.write(inputs)
    if "TTBarQ2down" in channelNew : # == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        #    inputs = inputs.replace(channelToReplace,"TTBarQ2down")
        inputs = inputs +")"
        o.write(inputs)
    if "TTBarMatchingup" in channelNew : # == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        #        inputs = inputs.replace(channelToReplace,"TTBar_MatchingUp")
        inputs = inputs +")"
        o.write(inputs)
    if "TTBarMatchingdown" in channelNew : # == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        #        inputs = inputs.replace(channelToReplace,"TTBar_MatchingDown")
        inputs = inputs +")"
        o.write(inputs)                        
    if "TChannel" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        #    inputs = inputs.replace(channelToReplace,"TChannel")
        inputs = inputs +")"
        o.write(inputs)
    if "TbarChannel" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        #    inputs = inputs.replace(channelToReplace,"TbarChannel")
        inputs = inputs +")"
        o.write(inputs)                
    if "WW" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        #    inputs = inputs.replace(channelToReplace,"TbarChannel")
        inputs = inputs +")"
        o.write(inputs)                
    if "WZ" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        #    inputs = inputs.replace(channelToReplace,"TbarChannel")
        inputs = inputs +")"
        o.write(inputs)                
    if "ZZ" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        #    inputs = inputs.replace(channelToReplace,"TbarChannel")
        inputs = inputs +")"
        o.write(inputs)                
#    if "Ele" in channelNew:#channelNew == "DataEle" or channelNew == "DataEleQCD":
#        inputs = "process.source.fileNames = cms.untracked.vstring("
#        inputs = inputs +"'"+dataPath+"Merged.root',"
##        inputs = inputs +"'"+dataPath+"Ele_v4.root',"
##        inputs = inputs +"'"+dataPath+"Ele_v2Merged.root',"
##        inputs = inputs +"'"+dataPath+"Ele_v1Merged.root',"
#        inputs = inputs +")"
#        o.write(inputs)
    o.close()
    return o

#Implementation of the loop part:

#Channel in the original file
startChannel = "TChannel"#channels[0]
nstart = 0;

f= open(fileName)

tmpName = "temp.py"
shutil.copy(fileName,tmpName)

for channel in channels:

    isMC = "False"
    if "Mu" in channel and not "QCD" in channel:
        channel_instruction = "mu"
    elif "Ele" in channel and not "QCD" in channel:
        channel_instruction = "ele"
    elif "Ele" in channel and not "QCD" in channel:
        channel_instruction = "ele"
    elif "Mu" in channel and ("QCD" in channel or "Had" in channel) and not "QCDMu" in channel:
        channel_instruction = "muqcd"
    elif "Ele" in channel and "QCD" in channel:
        channel_instruction = "eleqcd"
    else : 
        channel_instruction = "allmc"   
        isMC = "True"
    channelOld = startChannel
    
    cfg_file = changeChannel(tmpName,channelOld,channel,channel_instruction,isMC)
    command = 'nohup cmsRun ./' + channel+'_cfg.py > ./'+channel+'.log &'
    
    nstart = nstart +1
    if mode == "cmsRun":
        if nstart % nSimultaneous ==0 :
            command = 'nohup cmsRun ./' + channel+'_cfg.py > ./'+channel+'.log '
        else:
            command = 'nohup cmsRun ./' + channel+'_cfg.py > ./'+channel+'.log &'

        print command
        os.system(command)
        
    if mode == "qsub":
        launchCommand = 'qsub -q local jobtest_ntp.csh -v var1=' + channel + '_cfg.py -o ' + channel + '.log -j oe'  
        print launchCommand
        os.system(launchCommand)
                                               

#    if mode == "cmsRun":
#        os.system(command ) 
#    os.system("bg") 
#    os.system('rm '+channel+'_cfg.py' ) 

os.system('rm '+tmpName) 
#changeChannel(f,aChannel,startChannel)

#os.system(command)



