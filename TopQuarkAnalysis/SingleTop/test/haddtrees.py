#!/usr/bin/python

import os,sys,re,shutil,commands

channelsfiles = {
"W1Jet":40,
"W2Jets":40,
"W3Jets":40,
"W4Jets":40,
"ZJets":40,
"Mu_2011A_08Nov":40,
"Mu_2011B_19Nov":40,
"QCDMu":40,
"TChannel":40,
"SChannelCompHep":4,
"WZ":40,
#"ZZ":20,
#"WW":40,
#"WJets":20,
#"Ele_2011A_08Nov":40,
#"Ele_2011B_19Nov":40,
}

# for command line
#channel = sys.argv[1]
#nfiles = int(sys.argv[2])

ntppath = "/data3/scratch/users/fabozzi/SingleTop/ntp28feb15_Merged_trees/"

root_ext = ".root"
#root_ext = "_HLT_IsoMu17.root"

wh = " "

channels = channelsfiles.keys()
print channels

for channel in channels :
    nfiles = channelsfiles[channel]
    command = "hadd -f "
    command = command + ntppath + channel + root_ext + wh
    for nn in range( 1, nfiles+1 ):
        channelinput = ntppath+channel +"_part_"+str(nn)+root_ext+wh
        command = command + channelinput
    print command
    os.system(command)

