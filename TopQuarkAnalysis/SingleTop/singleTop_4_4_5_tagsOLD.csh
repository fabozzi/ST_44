cd ../../

cvs co -r V06-04-38      DataFormats/PatCandidates
cvs co -r V08-07-49      PhysicsTools/PatAlgos
cvs co -r V03-09-18-03   PhysicsTools/PatUtils
cvs co -r V00-05-29-01   PhysicsTools/PatExamples 
cvs co -r V08-03-16      PhysicsTools/Utilities 
cvs co -r V00-03-24-01   PhysicsTools/SelectorUtils 
cvs co -r V08-02-14      PhysicsTools/UtilAlgos
cvs co -r V00-03-05-10   CommonTools/ParticleFlow
##cvs co -r V00-03-16      CommonTools/ParticleFlow

##cvs co -r V06-23-01      CondFormats/DataRecord                           
##cvs co -r V01-02-13      CondFormats/EcalObjects                          
##cvs co -r V00-04-00      CondFormats/EgammaObjects           

## IT MUST BE SO since PFBlockElement::HO is not implemented in 44X (only in 52X/53X) 
cvs co -r V14-07-13        RecoParticleFlow/PFProducer  

#cvs co -r V15-02-05-01    RecoParticleFlow/PFProducer 
cvs co -r V00-04-11        RecoBTag/PerformanceDB 
cvs co -r V00-03-33        RecoEgamma/ElectronIdentification 
cvs co -r V03-03-07        RecoLuminosity/LumiDB 
##cvs co -r V05-08-24        RecoEcal/EgammaCoreTools                         
##cvs co -r V08-11-10-01     RecoEgamma/EgammaTools                           
##cvs co -r V00-00-08        RecoMET/METAnalyzers                             
##cvs co -r lhx_14APR2012_v1 RecoMET/METFilters                               
###wreece_020512  RecoParticleFlow/PostProcessing   

cvs co -r V15-03-04      DataFormats/ParticleFlowCandidate
cvs co -r V00-00-08 -d EGamma/EGammaAnalysisTools UserCode/EGamma/EGammaAnalysisTools
cd EGamma/EGammaAnalysisTools/data
cat download.url | xargs wget

cd ../../../

cvs co -r V00-02-09 -d CMGTools/External UserCode/CMG/CMGTools/External


cp ~oiorio/public/xMario/Lumi3DReWeighting.h PhysicsTools/Utilities/interface/Lumi3DReWeighting.h
cp ~oiorio/public/xMario/Lumi3DReWeighting.cc PhysicsTools/Utilities/src/Lumi3DReWeighting.cc

cp TopQuarkAnalysis/SingleTop/test/lhapdfwrapnew.xml $CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/selected/lhapdfwrap.xml
cp TopQuarkAnalysis/SingleTop/test/lhapdfnew.xml $CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/selected/lhapdf.xml
cp TopQuarkAnalysis/SingleTop/test/lhapdffullnew.xml $CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/selected/lhapdffull.xml

cmsenv
scram setup lhapdffull
cmsenv

#cvs up -r 1.20 RecoParticleFlow/PFProducer/plugins/PFElectronTranslator.cc
#cvs up -r 1.30 RecoParticleFlow/PFProducer/interface/PFAlgo.h
#cvs up -r 1.37 RecoParticleFlow/PFProducer/plugins/PFProducer.cc

scram b -j 9 > & step1.log 


##cvs co -r lhx_12JAN2012_v1   DataFormats/METReco 
cvs co -r V03-03-07    DataFormats/METReco
cvs co -r V04-05-08    JetMETCorrections/Type1MET 
cvs co -r b4_2_X_cvMEtCorr_13Feb2012_JEC11V12 PhysicsTools/PatUtils 


cvs co -r V02-03-00    JetMETCorrections/Algorithms 
#rm -f JetMETCorrections/Algorithms/interface/L1JPTOffsetCorrector.h
#rm -f JetMETCorrections/Algorithms/src/L1JPTOffsetCorrector.cc
cvs co -r V03-01-00 JetMETCorrections/Objects 
addpkg JetMETCorrections/Modules V05-01-00
cvs up -r 1.4 JetMETCorrections/Modules/plugins/JetCorrectorOnTheFly.cc
cvs up -r 1.6 JetMETCorrections/Modules/interface/JetCorrectionProducer.h

### IT MUST BE SO SINCE pat::Electron has no member setIsPF in 44X
cvs co -r $CMSSW_VERSION  PhysicsTools/PatAlgos 

cvs up -r 1.64.2.4   PhysicsTools/PatAlgos/python/tools/jetTools.py
cvs up -r 1.53 PhysicsTools/PatAlgos/python/tools/tauTools.py

scram b -j 9 > & step2.log &

