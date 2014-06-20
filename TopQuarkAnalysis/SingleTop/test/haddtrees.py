#!/usr/bin/python

import os,sys,re,shutil,commands


channelsfiles = {
"ZJets":15,
"TTBar":15,
"W1Jet":15,
"W2Jets":15,
"W3Jets":15,
"W4Jets":20,
#"WJets":20,
"Ele_2011A_08Nov":15,
"Ele_2011B_19Nov":15,
"Mu_2011A_08Nov":15,
"Mu_2011B_19Nov":20,
"ZZ":20,
"WZ":20,
}

# for command line
#channel = sys.argv[1]
#nfiles = int(sys.argv[2])

ntppath = "/data3/scratch/users/fabozzi/SingleTop/ntp14apr14_Merged_trees_v2/"

root_ext = ".root"

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

