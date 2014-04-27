#!/bin/csh
cd /home/fabozzi/cmsrel/stop/test/CMSSW_4_4_5/src/TopQuarkAnalysis/SingleTop/test
source /home/fabozzi/setarch_4X.csh
eval `scramv1 runtime -csh`
cmsRun $var1

