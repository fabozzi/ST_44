import FWCore.ParameterSet.Config as cms

from TopQuarkAnalysis.SingleTop.SelectionCuts_Skim_cff import *

from PhysicsTools.HepMCCandAlgos.flavorHistoryPaths_cfi import *

from PhysicsTools.PatAlgos.patSequences_cff import *

from TopQuarkAnalysis.SingleTop.simpleEleIdSequence_cff import *




#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleTopJetsPF
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTuplePatMETsPF
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleElectrons
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleMuons
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTuplesSkim

from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleTopJetsPF
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTuplePatMETsPF
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTuplePatType1METsPF
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleElectrons
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleMuons
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTuplesSkim

from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleAllElectrons
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleAllMuons


from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleQCDElectrons
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleQCDMuons

from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleAllJets

from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleLooseElectrons
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleLooseMuons
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleVertices
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleZVetoElectrons

from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCLeptons
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCNeutrinos
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCQuarks
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCBQuarks
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCTops
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCTopsW
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCTopsBQuark
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCTopsQuark
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCTopsQuarkBar
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCTopsLepton
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCTopsNeutrino

from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTuplesSkimMCTruth



#if isdata: process.looseLeptonSequence.remove(process.muonMatchLoose)


# require scraping filter
scrapingVeto = cms.EDFilter("FilterOutScraping",
                                                                applyfilter=cms.untracked.bool(True),
                                                                debugOn=cms.untracked.bool(False),
                                                                numtrack=cms.untracked.uint32(10),
                                                                thresh=cms.untracked.double(0.2)
                                                                )
# HB + HE noise filtering
from CommonTools.RecoAlgos.HBHENoiseFilter_cfi import HBHENoiseFilter

HBHENoiseFilter.minIsolatedNoiseSumE = cms.double(999999.)
HBHENoiseFilter.minNumIsolatedNoiseChannels = cms.int32(999999)
HBHENoiseFilter.minIsolatedNoiseSumEt = cms.double(999999.)

from CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi import HBHENoiseFilterResultProducer
HBHENoiseFilterResultProducer.minRatio = cms.double(-999)
HBHENoiseFilterResultProducer.maxRatio = cms.double(999)
HBHENoiseFilterResultProducer.minHPDHits = cms.int32(17)
HBHENoiseFilterResultProducer.minRBXHits = cms.int32(999)
HBHENoiseFilterResultProducer.minHPDNoOtherHits = cms.int32(10)
HBHENoiseFilterResultProducer.minZeros = cms.int32(10)
HBHENoiseFilterResultProducer.minHighEHitTime = cms.double(-9999.0)
HBHENoiseFilterResultProducer.maxHighEHitTime = cms.double(9999.0)
HBHENoiseFilterResultProducer.maxRBXEMF = cms.double(-999.0)
HBHENoiseFilterResultProducer.minNumIsolatedNoiseChannels = cms.int32(999999)
HBHENoiseFilterResultProducer.minIsolatedNoiseSumE = cms.double(999999.)
HBHENoiseFilterResultProducer.minIsolatedNoiseSumEt = cms.double(999999.)
HBHENoiseFilterResultProducer.useTS4TS5 = cms.bool(True)



nTuplePatMETsPF.src = cms.InputTag('patMETs')

from RecoEgamma.ElectronIdentification.electronIdSequence_cff import *

patElectronIDs = cms.Sequence(simpleEleIdSequence +
                                                            eIdSequence)
electronIDSources = cms.PSet(
        simpleEleId60cIso = cms.InputTag("simpleEleId60cIso"),
            simpleEleId70cIso = cms.InputTag("simpleEleId70cIso"),
            simpleEleId95cIso = cms.InputTag("simpleEleId95cIso"),
            eidRobustLoose= cms.InputTag("eidRobustLoose"),
            eidRobustTight= cms.InputTag("eidRobustTight"),
            eidRobustHighEnergy= cms.InputTag("eidRobustHighEnergy")
            )

#cFlavorHistory

patElectrons.addElectronID = cms.bool(True)
patElectrons.electronIDSources = electronIDSources


#makeNewPatElectrons = cms.Sequence(patElectronIDs * patElectronIsolation * patElectrons)

patElectrons.usePV = cms.bool(False)
patMuons.usePV = cms.bool(False)


#In those paths the customized collections are produced

basePath = cms.Sequence(
       preselectedMETs +
          looseMuons +
          PVFilterProducer +
          looseElectrons +
       #   zVetoElectrons +
          topJetsPF +
          UnclusteredMETPF +
#          UnclusteredType1METPF +
          genJetsPF +
          NVertices +
          NGenParticles +
          tightMuonsZeroIso +
          tightElectronsZeroIso +
          tightMuons +
          tightElectrons +
       #  SingleTopMCProducer +
          PDFInfo
          )

basePathData = cms.Sequence(
       preselectedMETs +
          looseMuons +
          PVFilterProducer +
          looseElectrons +
          #   zVetoElectrons +
          topJetsPF +
          UnclusteredMETPF +
#          UnclusteredType1METPF +
          #   NVertices +
          tightMuonsZeroIso +
          tightElectronsZeroIso +
          tightMuons +
          tightElectrons
          #  SingleTopMCProducer +
          )

#Flavor history tools sequence
flavorHistorySequence = cms.Sequence(
        cFlavorHistoryProducer *
            bFlavorHistoryProducer
            )

#Selection step: require 1 high pt muon/electron
preselection = cms.Sequence(
    #    hltFilter +
        PVFilter *
        #    HBHENoiseFilter *
        #    scrapingVeto *
            countLeptons
            )

#Selection step: require 1 high pt muon/electron
preselectionData = cms.Sequence(
    #    hltFilter +
    PVFilter *
    HBHENoiseFilter *
    scrapingVeto *
    countLeptons
    )

#Selection step: require 1 high pt muon/electron
#process.preselection(
#    hltFilter +
#    PVFilter +
#    countLeptons
#    )

#Ntuple production sequences:

#!!!Work in progress!!!#
