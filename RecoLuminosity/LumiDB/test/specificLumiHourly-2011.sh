#!/bin/sh
currendir=`pwd`
sarch="slc5_ia32_gcc434"
workdir="/afs/cern.ch/user/l/lumipro/scratch0/CMSSW_3_11_0"
authdir="/afs/cern.ch/user/l/lumipro"
indir="/afs/cern.ch/cms/lumi/ppfills2011"
outdir="/afs/cern.ch/cms/CAF/CMSCOMM/COMM_GLOBAL/LHCFILES"
logpath="/afs/cern.ch/cms/lumi/"
dbConnectionString="oracle://cms_orcoff_prod/cms_lumi_prod"
source /afs/cern.ch/cms/cmsset_default.sh;
export SCRAM_ARCH="$sarch";
cd $workdir
eval `scramv1 runtime -sh`
touch "$logpath/specificLumiHourly-2011-withcorrection.log"
date >> "$logpath/specificLumiHourly-2011-withcorrection.log"
specificLumi-2011.py -c $dbConnectionString -P $authdir -i $indir -o $outdir --with-correction>> "$logpath/specificLumiHourly-2011-withcorrection.log" ;
date >> "$logpath/specificLumiHourly-2011-withcorrection.log"
touch "$logpath/checklumi.log"
python $workdir/src/RecoLuminosity/LumiDB/test/checklumi.py >> "$logpath/checklumi.log"
cd $currentdir