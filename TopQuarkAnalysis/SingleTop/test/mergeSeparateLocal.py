#!/usr/bin/env cmsRun
import FWCore.ParameterSet.Config as cms
import os,sys,re,shutil,commands


inputDir = "/data3/scratch/users/fabozzi/SingleTop/ntp14apr14/"
outputDir = "/data3/scratch/users/fabozzi/SingleTop/ntp14apr14_Merged/"

#Original config file
template = "copyFlavorSeparationTemplateSummer"
#fName = "copyFlavorSeparationTemplate.py"
#f = open(fName)


option = "None"
#option = "cmsRun"
option = "qsub"

nparts = 1
channels = [
#"Mu_2011A_08Nov",
#"Mu_2011B_19Nov",
#"TTBar",
#"TTBarQ2up",
#"TTBarQ2down",
#"WJetsQ2up",
#"WJetsQ2down",

#"TTBarMatchingup",
#"TTBarMatchingdown",
    
#"TChannel_Q2Up",
#"TbarChannel_Q2Up",
#"TChannel_Q2Down",
#"TbarChannel_Q2Down",
#"WJets",
#"W1Jet",
#"W2Jets"
#"W3Jets"
#"W4Jets"
#"ZJets",
#"TWChannel",
#"TbarWChannel",
#"TChannel",
#"TbarChannel",
#"SChannel",
#"SbarChannel",
#"TChannel",
#"Ele_v1_A",
#"Mu_v1_A",
#"Mu_v1_B2",
#"Mu_v1_B1",
#"WW",
#"WZ",
#"ZZ",
#---------------------------------------------
"QCDMu",
"QCD_Pt_20to30_EMEnriched",
"QCD_Pt_20to30_BCtoE",
"QCD_Pt_30to80_EMEnriched",
"QCD_Pt_30to80_BCtoE",
"QCD_Pt_80to170_EMEnriched",
"QCD_Pt_80to170_BCtoE",
"QCD_HT_100_200_GJets",
"QCD_HT_200_inf_GJets",
"QCD_HT_40_100_GJets",
"SChannel",
"SbarChannel",
"TChannel",
"TWChannel",
"TbarChannel",
"TbarWChannel",
"WW",
#"ZJets",
#"TTBar",
#"W1Jet",
#"W2Jets",
#"W3Jets",
#"Ele_2011A_08Nov",
#"Ele_2011B_19Nov",
#"Mu_2011A_08Nov",
]

for channel in channels: 
#    command_ls = "ls " + inputDir + " | grep _"+channel+"_"
    command_ls = "ls -1 " + inputDir + "/"+ channel+ " | grep edmntuple"
    print command_ls
    files = commands.getoutput(command_ls).split('\n')
    print "channel "+ channel +" n files " + str(len(files))

    print files

    templateFile= __import__(template)     

#    for file in files:
#        print file
    print "Removing doubles from list"
# looping over copies of list, otherwise unexpected results!
    files1 = list(files)
    files2 = list(files)
    nn1 = len(files1)
    nn2 = len(files2)
    nremoved = 0
    for ii in range(0, nn1) :
        for jj in range(ii+1, nn2) :
            file1 = files1[ii]
            file2 = files2[jj]
            fileNameParts = file1.split("_")
            jobNumber = fileNameParts[len(fileNameParts)-3] 
            checkFileNameParts = file2.split("_")
            checkJobNumber = checkFileNameParts[len(checkFileNameParts)-3] 
            if jobNumber == checkJobNumber:
                print " double: " + file1 +" vs " + file2 
                print "REMOVING " + file2 
                files.remove(file2)
                nremoved = nremoved + 1
#            Break 
    nfiles = len(files)    
    nraws = nfiles/(nparts)
    
    part = 0
    print "files removed = ", nremoved
    print channel + " after removal: n files " + str(len(files))
    for file in files:
        print file
    
    while int(part) < int(nparts):
        templateFileCopy = templateFile 
        templateFileCopy.process.source.fileNames = cms.untracked.vstring([]) 

               
        part = part +1
        if int(nparts) ==1:
            templateFileCopy.process.skimwall.fileName = cms.untracked.string(outputDir+channel+'Merged.root')
            configFile = open(channel + "_part_" +str(part)+"_cfg.py","w")
        else:
            templateFileCopy.process.skimwall.fileName = cms.untracked.string(outputDir+channel+'_part_'+str(part)+'Merged.root')
            configFile = open(channel + "_part_" +str(part)+"_cfg.py","w")

        
        nr =0
        for file in files:
            nr = nr +1
            if part == nparts:
                if nr > nraws * (part -1):
                    templateFileCopy.process.source.fileNames.append("file:"+inputDir+"/"+channel+"/"+str(file))
            elif  nr > nraws * (part -1) and  nr <= nraws *part:
    #            print "nr "+str( nr )+" part "+str( part) + " nraws "+str( nraws ) + " filename " + str(file)
                templateFileCopy.process.source.fileNames.append("file:"+inputDir+"/"+channel+"/"+str(file))
               
        configFile.write(templateFileCopy.process.dumpPython())
        configFile.close()
        if option == "cmsRun":
            launchCommand = 'nohup cmsRun ./' + channel + "_part_" +str(part)+"_cfg.py" +' >  '+outputDir+channel+"_part_"+str(part)+'_merge.log &'
            print launchCommand
            os.system(launchCommand)
        if option == "qsub":
            launchCommand = 'qsub -q local jobtest_ntp.csh -v var1=' + channel + "_part_" +str(part)+"_cfg.py -o "+channel + "_part_" +str(part)+".log -j oe"  
            print launchCommand
            os.system(launchCommand)
                                        
        
