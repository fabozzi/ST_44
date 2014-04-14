#!/bin/sh
currendir=`pwd`
sarch="slc5_ia32_gcc434"
workdir="/build1/zx/cron/CMSSW_3_11_0"
authdir="/afs/cern.ch/user/x/xiezhen"
outdir="/afs/cern.ch/cms/lumi/www/plots/operation"
logpath="/afs/cern.ch/cms/lumi/"
withcorrection="--with-correction"
dbConnectionString="oracle://cms_orcoff_prod/cms_lumi_prod"
source /afs/cern.ch/cms/cmsset_default.sh;
export SCRAM_ARCH="$sarch";
cd $workdir
eval `scramv1 runtime -sh`
touch "$logpath/lumiPlotHourly-2011-withcorrection.log"
date >> "$logpath/lumiPlotHourly-2011-withcorrection.log"
cp  "$outdir/runlist.txt" "$outdir/runlist.txt.old"
lumiPlotFiller.py -c $dbConnectionString -P $authdir create2011runlist -o $outdir >> "$logpath/lumiPlotHourly-2011-withcorrection.log" ;
sleep 1
lumiPlotFiller.py -c $dbConnectionString -P $authdir instperrun -o $outdir -i "$outdir/runlist.txt" $withcorrection>> "$logpath/lumiPlotHourly-2011-withcorrection.log"
#if `diff "$outdir/runlist.txt" "$outdir/runlist.txt.old" > /dev/null` ; then
#   echo 'no new runs, do nothing' >> "$logpath/lumiPlotHourly-withcorrection.log"
#else
#fi   
date >> "$logpath/lumiPlotHourly-2011-withcorrection.log"
cd $currentdir
