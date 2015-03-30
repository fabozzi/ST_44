#!/usr/bin/env cmsRun
import FWCore.ParameterSet.Config as cms
import os,sys,re,shutil


#Original config file
fileName = "SingleTopSystematicsWithTrigger_cfg.py"
#fileName = "SingleTopPDFWithTrigger_cfg.py"
#fileName = "SingleTopSystematics_cfg.py"
#fileName = "SingleTopSystematics_split_cfg.py"
#fileName = "SingleTopNEvents_cfg.py"

nSimultaneous = 4


#Channels to include
channels = [
#"TChannel",

#"Ele_2011A_08Nov_part_1",
#"Ele_2011A_08Nov_part_2",
#"Ele_2011A_08Nov_part_3",
#"Ele_2011A_08Nov_part_4",
#"Ele_2011A_08Nov_part_5",
#"Ele_2011A_08Nov_part_6",
#"Ele_2011A_08Nov_part_7",
#"Ele_2011A_08Nov_part_8",
#"Ele_2011A_08Nov_part_9",
#"Ele_2011A_08Nov_part_10",
#"Ele_2011A_08Nov_part_11",
#"Ele_2011A_08Nov_part_12",
#"Ele_2011A_08Nov_part_13",
#"Ele_2011A_08Nov_part_14",
#"Ele_2011A_08Nov_part_15",
#"Ele_2011A_08Nov_part_16",
#"Ele_2011A_08Nov_part_17",
#"Ele_2011A_08Nov_part_18",
#"Ele_2011A_08Nov_part_19",
#"Ele_2011A_08Nov_part_20",
#"Ele_2011A_08Nov_part_21",
#"Ele_2011A_08Nov_part_22",
#"Ele_2011A_08Nov_part_23",
#"Ele_2011A_08Nov_part_24",
#"Ele_2011A_08Nov_part_25",
#"Ele_2011A_08Nov_part_26",
#"Ele_2011A_08Nov_part_27",
#"Ele_2011A_08Nov_part_28",
#"Ele_2011A_08Nov_part_29",
#"Ele_2011A_08Nov_part_30",
#"Ele_2011A_08Nov_part_31",
#"Ele_2011A_08Nov_part_32",
#"Ele_2011A_08Nov_part_33",
#"Ele_2011A_08Nov_part_34",
#"Ele_2011A_08Nov_part_35",
#"Ele_2011A_08Nov_part_36",
#"Ele_2011A_08Nov_part_37",
#"Ele_2011A_08Nov_part_38",
#"Ele_2011A_08Nov_part_39",
#"Ele_2011A_08Nov_part_40",

#"Ele_2011B_19Nov_part_1",
#"Ele_2011B_19Nov_part_2",
#"Ele_2011B_19Nov_part_3",
#"Ele_2011B_19Nov_part_4",
#"Ele_2011B_19Nov_part_5",
#"Ele_2011B_19Nov_part_6",
#"Ele_2011B_19Nov_part_7",
#"Ele_2011B_19Nov_part_8",
#"Ele_2011B_19Nov_part_9",
#"Ele_2011B_19Nov_part_10",
#"Ele_2011B_19Nov_part_11",
#"Ele_2011B_19Nov_part_12",
#"Ele_2011B_19Nov_part_13",
#"Ele_2011B_19Nov_part_14",
#"Ele_2011B_19Nov_part_15",
#"Ele_2011B_19Nov_part_16",
#"Ele_2011B_19Nov_part_17",
#"Ele_2011B_19Nov_part_18",
#"Ele_2011B_19Nov_part_19",
#"Ele_2011B_19Nov_part_20",
#"Ele_2011B_19Nov_part_21",
#"Ele_2011B_19Nov_part_22",
#"Ele_2011B_19Nov_part_23",
#"Ele_2011B_19Nov_part_24",
#"Ele_2011B_19Nov_part_25",
#"Ele_2011B_19Nov_part_26",
#"Ele_2011B_19Nov_part_27",
#"Ele_2011B_19Nov_part_28",
#"Ele_2011B_19Nov_part_29",
#"Ele_2011B_19Nov_part_30",
#"Ele_2011B_19Nov_part_31",
#"Ele_2011B_19Nov_part_32",
#"Ele_2011B_19Nov_part_33",
#"Ele_2011B_19Nov_part_34",
#"Ele_2011B_19Nov_part_35",
#"Ele_2011B_19Nov_part_36",
#"Ele_2011B_19Nov_part_37",
#"Ele_2011B_19Nov_part_38",
#"Ele_2011B_19Nov_part_39",
#"Ele_2011B_19Nov_part_40",

#############################################
## NOTA BENE: WRONG ELE ISOLATION
## FOR SINGLE TOP TREES
## TREES TO BE REDONE FOR ELECTRON CHANNEL STUDIES
#############################################

#"SChannel",
#"SChannelMassup_part_4",
#"SChannelMassdown_part_4",
#"SChannelQ2up_part_4",
#"SChannelQ2down_part_4",

#"SbarChannel",
#"SbarChannelMassup_part_4",
#"SbarChannelMassdown_part_4",
#"SbarChannelQ2up_part_4",
#"SbarChannelQ2down_part_4",

#"TChannel_part_1",
#"TChannel_part_2",
#"TChannel_part_3",
#"TChannel_part_4",
#"TChannel_part_5",
#"TChannel_part_6",
#"TChannel_part_7",
#"TChannel_part_8",
#"TChannel_part_9",
#"TChannel_part_10",
#"TChannel_part_11",
#"TChannel_part_12",
#"TChannel_part_13",
#"TChannel_part_14",
#"TChannel_part_15",
#"TChannel_part_16",
#"TChannel_part_17",
#"TChannel_part_18",
#"TChannel_part_19",
#"TChannel_part_20",
#"TChannel_part_21",
#"TChannel_part_22",
#"TChannel_part_23",
#"TChannel_part_24",
#"TChannel_part_25",
#"TChannel_part_26",
#"TChannel_part_27",
#"TChannel_part_28",
#"TChannel_part_29",
#"TChannel_part_30",
#"TChannel_part_31",
#"TChannel_part_32",
#"TChannel_part_33",
#"TChannel_part_34",
#"TChannel_part_35",
#"TChannel_part_36",
#"TChannel_part_37",
#"TChannel_part_38",
#"TChannel_part_39",
#"TChannel_part_40",

#"TChannelQ2up_part_1",
#"TChannelQ2up_part_2",
#"TChannelQ2up_part_3",
#"TChannelQ2up_part_4",
#"TChannelQ2down_part_1",
#"TChannelQ2down_part_2",
#"TChannelQ2down_part_3",
#"TChannelQ2down_part_4",
#"TChannelMassup_part_1",
#"TChannelMassup_part_2",
#"TChannelMassup_part_3",
#"TChannelMassup_part_4",
#"TChannelMassdown_part_1",
#"TChannelMassdown_part_2",
#"TChannelMassdown_part_3",
#"TChannelMassdown_part_4",

#"TbarChannel_part_40",

#"TbarChannelMassup_part_1",
#"TbarChannelMassup_part_2",
#"TbarChannelMassup_part_3",
#"TbarChannelMassup_part_4",
#"TbarChannelMassdown_part_1",
#"TbarChannelMassdown_part_2",
#"TbarChannelMassdown_part_3",
#"TbarChannelMassdown_part_4",
#"TbarChannelQ2up_part_1",
#"TbarChannelQ2up_part_2",
#"TbarChannelQ2up_part_3",
#"TbarChannelQ2up_part_4",
#"TbarChannelQ2down_part_1",
#"TbarChannelQ2down_part_2",
#"TbarChannelQ2down_part_3",
#"TbarChannelQ2down_part_4",

#"TWChannel_part_40",
#"TbarWChannel_part_40",

#"SChannelCompHep_part_1",
#"SChannelCompHep_part_2",
#"SChannelCompHep_part_3",
#"SChannelCompHep_part_4",

#"TTBarQ2up_part_1",
#"TTBarQ2up_part_2",
#"TTBarQ2up_part_3",
#"TTBarQ2up_part_4",
#"TTBarQ2down_part_1",
#"TTBarQ2down_part_2",
#"TTBarQ2down_part_3",
#"TTBarQ2down_part_4",
#"TTBarMassup_part_1",
#"TTBarMassup_part_2",
#"TTBarMassup_part_3",
#"TTBarMassup_part_4",
#"TTBarMassdown_part_1",
#"TTBarMassdown_part_2",
#"TTBarMassdown_part_3",
#"TTBarMassdown_part_4",
#"TTBarMatchingup_part_1",
#"TTBarMatchingup_part_2",
#"TTBarMatchingup_part_3",
#"TTBarMatchingup_part_4",
"TTBarMatchingdown_part_1",
"TTBarMatchingdown_part_2",
"TTBarMatchingdown_part_3",
"TTBarMatchingdown_part_4",

#"WW_part_40",
#"ZZ_part_40",

#"WZ_part_1",
#"WZ_part_2",
#"WZ_part_3",
#"WZ_part_4",
#"WZ_part_5",
#"WZ_part_6",
#"WZ_part_7",
#"WZ_part_8",
#"WZ_part_9",
#"WZ_part_10",
#"WZ_part_11",
#"WZ_part_12",
#"WZ_part_13",
#"WZ_part_14",
#"WZ_part_15",
#"WZ_part_16",
#"WZ_part_17",
#"WZ_part_18",
#"WZ_part_19",
#"WZ_part_20",
#"WZ_part_21",
#"WZ_part_22",
#"WZ_part_23",
#"WZ_part_24",
#"WZ_part_25",
#"WZ_part_26",
#"WZ_part_27",
#"WZ_part_28",
#"WZ_part_29",
#"WZ_part_30",
#"WZ_part_31",
#"WZ_part_32",
#"WZ_part_33",
#"WZ_part_34",
#"WZ_part_35",
#"WZ_part_36",
#"WZ_part_37",
#"WZ_part_38",
#"WZ_part_39",
#"WZ_part_40",

#"QCDMu_part_1",
#"QCDMu_part_2",
#"QCDMu_part_3",
#"QCDMu_part_4",
#"QCDMu_part_5",
#"QCDMu_part_6",
#"QCDMu_part_7",
#"QCDMu_part_8",
#"QCDMu_part_9",
#"QCDMu_part_10",
#"QCDMu_part_11",
#"QCDMu_part_12",
#"QCDMu_part_13",
#"QCDMu_part_14",
#"QCDMu_part_15",
#"QCDMu_part_16",
#"QCDMu_part_17",
#"QCDMu_part_18",
#"QCDMu_part_19",
#"QCDMu_part_20",
#"QCDMu_part_21",
#"QCDMu_part_22",
#"QCDMu_part_23",
#"QCDMu_part_24",
#"QCDMu_part_25",
#"QCDMu_part_26",
#"QCDMu_part_27",
#"QCDMu_part_28",
#"QCDMu_part_29",
#"QCDMu_part_30",
#"QCDMu_part_31",
#"QCDMu_part_32",
#"QCDMu_part_33",
#"QCDMu_part_34",
#"QCDMu_part_35",
#"QCDMu_part_36",
#"QCDMu_part_37",
#"QCDMu_part_38",
#"QCDMu_part_39",
#"QCDMu_part_40",


#"ZJets_part_1",
#"ZJets_part_2",
#"ZJets_part_3",
#"ZJets_part_4",
#"ZJets_part_5",
#"ZJets_part_6",
#"ZJets_part_7",
#"ZJets_part_8",
#"ZJets_part_9",
#"ZJets_part_10",
#"ZJets_part_11",
#"ZJets_part_12",
#"ZJets_part_13",
#"ZJets_part_14",
#"ZJets_part_15",
#"ZJets_part_16",
#"ZJets_part_17",
#"ZJets_part_18",
#"ZJets_part_19",
#"ZJets_part_20",
#"ZJets_part_21",
#"ZJets_part_22",
#"ZJets_part_23",
#"ZJets_part_24",
#"ZJets_part_25",
#"ZJets_part_26",
#"ZJets_part_27",
#"ZJets_part_28",
#"ZJets_part_29",
#"ZJets_part_30",
#"ZJets_part_31",
#"ZJets_part_32",
#"ZJets_part_33",
#"ZJets_part_34",
#"ZJets_part_35",
#"ZJets_part_36",
#"ZJets_part_37",
#"ZJets_part_38",
#"ZJets_part_39",
#"ZJets_part_40",

#"WJetsQ2up_part_1",
#"WJetsQ2up_part_2",
#"WJetsQ2up_part_3",
#"WJetsQ2up_part_4",

#"WJetsQ2down_part_1",
#"WJetsQ2down_part_2",
#"WJetsQ2down_part_3",
#"WJetsQ2down_part_4",

#"WJetsMatchingup_part_1",
#"WJetsMatchingup_part_2",
#"WJetsMatchingup_part_3",
#"WJetsMatchingup_part_4",

#"WJetsMatchingdown_part_1",
#"WJetsMatchingdown_part_2",
#"WJetsMatchingdown_part_3",
#"WJetsMatchingdown_part_4",


#"TTBar_part_1",
#"TTBar_part_2",
#"TTBar_part_3",
#"TTBar_part_4",
#"TTBar_part_5",
#"TTBar_part_6",
#"TTBar_part_7",
#"TTBar_part_8",
#"TTBar_part_9",
#"TTBar_part_10",
#"TTBar_part_11",
#"TTBar_part_12",
#"TTBar_part_13",
#"TTBar_part_14",
#"TTBar_part_15",
#"TTBar_part_16",
#"TTBar_part_17",
#"TTBar_part_18",
#"TTBar_part_19",
#"TTBar_part_20",
#"TTBar_part_21",
#"TTBar_part_22",
#"TTBar_part_23",
#"TTBar_part_24",
#"TTBar_part_25",
#"TTBar_part_26",
#"TTBar_part_27",
#"TTBar_part_28",
#"TTBar_part_29",
#"TTBar_part_30",
#"TTBar_part_31",
#"TTBar_part_32",
#"TTBar_part_33",
#"TTBar_part_34",
#"TTBar_part_35",
#"TTBar_part_36",
#"TTBar_part_37",
#"TTBar_part_38",
#"TTBar_part_39",
#"TTBar_part_40",

#"W1Jet_part_1",
#"W1Jet_part_2",
#"W1Jet_part_3",
#"W1Jet_part_4",
#"W1Jet_part_5",
#"W1Jet_part_6",
#"W1Jet_part_7",
#"W1Jet_part_8",
#"W1Jet_part_9",
#"W1Jet_part_10",
#"W1Jet_part_11",
#"W1Jet_part_12",
#"W1Jet_part_13",
#"W1Jet_part_14",
#"W1Jet_part_15",
#"W1Jet_part_16",
#"W1Jet_part_17",
#"W1Jet_part_18",
#"W1Jet_part_19",
#"W1Jet_part_20",
#"W1Jet_part_21",
#"W1Jet_part_22",
#"W1Jet_part_23",
#"W1Jet_part_24",
#"W1Jet_part_25",
#"W1Jet_part_26",
#"W1Jet_part_27",
#"W1Jet_part_28",
#"W1Jet_part_29",
#"W1Jet_part_30",
#"W1Jet_part_31",
#"W1Jet_part_32",
#"W1Jet_part_33",
#"W1Jet_part_34",
#"W1Jet_part_35",
#"W1Jet_part_36",
#"W1Jet_part_37",
#"W1Jet_part_38",
#"W1Jet_part_39",
#"W1Jet_part_40",

#"W2Jets_part_1",
#"W2Jets_part_2",
#"W2Jets_part_3",
#"W2Jets_part_4",
#"W2Jets_part_5",
#"W2Jets_part_6",
#"W2Jets_part_7",
#"W2Jets_part_8",
#"W2Jets_part_9",
#"W2Jets_part_10",
#"W2Jets_part_11",
#"W2Jets_part_12",
#"W2Jets_part_13",
#"W2Jets_part_14",
#"W2Jets_part_15",
#"W2Jets_part_16",
#"W2Jets_part_17",
#"W2Jets_part_18",
#"W2Jets_part_19",
#"W2Jets_part_20",
#"W2Jets_part_21",
#"W2Jets_part_22",
#"W2Jets_part_23",
#"W2Jets_part_24",
#"W2Jets_part_25",
#"W2Jets_part_26",
#"W2Jets_part_27",
#"W2Jets_part_28",
#"W2Jets_part_29",
#"W2Jets_part_30",
#"W2Jets_part_31",
#"W2Jets_part_32",
#"W2Jets_part_33",
#"W2Jets_part_34",
#"W2Jets_part_35",
#"W2Jets_part_36",
#"W2Jets_part_37",
#"W2Jets_part_38",
#"W2Jets_part_39",
#"W2Jets_part_40",

#"W3Jets_part_1",
#"W3Jets_part_2",
#"W3Jets_part_3",
#"W3Jets_part_4",
#"W3Jets_part_5",
#"W3Jets_part_6",
#"W3Jets_part_7",
#"W3Jets_part_8",
#"W3Jets_part_9",
#"W3Jets_part_10",
#"W3Jets_part_11",
#"W3Jets_part_12",
#"W3Jets_part_13",
#"W3Jets_part_14",
#"W3Jets_part_15",
#"W3Jets_part_16",
#"W3Jets_part_17",
#"W3Jets_part_18",
#"W3Jets_part_19",
#"W3Jets_part_20",
#"W3Jets_part_21",
#"W3Jets_part_22",
#"W3Jets_part_23",
#"W3Jets_part_24",
#"W3Jets_part_25",
#"W3Jets_part_26",
#"W3Jets_part_27",
#"W3Jets_part_28",
#"W3Jets_part_29",
#"W3Jets_part_30",
#"W3Jets_part_31",
#"W3Jets_part_32",
#"W3Jets_part_33",
#"W3Jets_part_34",
#"W3Jets_part_35",
#"W3Jets_part_36",
#"W3Jets_part_37",
#"W3Jets_part_38",
#"W3Jets_part_39",
#"W3Jets_part_40",

#"W4Jets_part_1",
#"W4Jets_part_2",
#"W4Jets_part_3",
#"W4Jets_part_4",
#"W4Jets_part_5",
#"W4Jets_part_6",
#"W4Jets_part_7",
#"W4Jets_part_8",
#"W4Jets_part_9",
#"W4Jets_part_10",
#"W4Jets_part_11",
#"W4Jets_part_12",
#"W4Jets_part_13",
#"W4Jets_part_14",
#"W4Jets_part_15",
#"W4Jets_part_16",
#"W4Jets_part_17",
#"W4Jets_part_18",
#"W4Jets_part_19",
#"W4Jets_part_20",
#"W4Jets_part_21",
#"W4Jets_part_22",
#"W4Jets_part_23",
#"W4Jets_part_24",
#"W4Jets_part_25",
#"W4Jets_part_26",
#"W4Jets_part_27",
#"W4Jets_part_28",
#"W4Jets_part_29",
#"W4Jets_part_30",
#"W4Jets_part_31",
#"W4Jets_part_32",
#"W4Jets_part_33",
#"W4Jets_part_34",
#"W4Jets_part_35",
#"W4Jets_part_36",
#"W4Jets_part_37",
#"W4Jets_part_38",
#"W4Jets_part_39",
#"W4Jets_part_40",


#"Mu_2011A_08Nov_part_1",
#"Mu_2011A_08Nov_part_2",
#"Mu_2011A_08Nov_part_3",
#"Mu_2011A_08Nov_part_4",
#"Mu_2011A_08Nov_part_5",
#"Mu_2011A_08Nov_part_6",
#"Mu_2011A_08Nov_part_7",
#"Mu_2011A_08Nov_part_8",
#"Mu_2011A_08Nov_part_9",
#"Mu_2011A_08Nov_part_10",
#"Mu_2011A_08Nov_part_11",
#"Mu_2011A_08Nov_part_12",
#"Mu_2011A_08Nov_part_13",
#"Mu_2011A_08Nov_part_14",
#"Mu_2011A_08Nov_part_15",
#"Mu_2011A_08Nov_part_16",
#"Mu_2011A_08Nov_part_17",
#"Mu_2011A_08Nov_part_18",
#"Mu_2011A_08Nov_part_19",
#"Mu_2011A_08Nov_part_20",
#"Mu_2011A_08Nov_part_21",
#"Mu_2011A_08Nov_part_22",
#"Mu_2011A_08Nov_part_23",
#"Mu_2011A_08Nov_part_24",
#"Mu_2011A_08Nov_part_25",
#"Mu_2011A_08Nov_part_26",
#"Mu_2011A_08Nov_part_27",
#"Mu_2011A_08Nov_part_28",
#"Mu_2011A_08Nov_part_29",
#"Mu_2011A_08Nov_part_30",
#"Mu_2011A_08Nov_part_31",
#"Mu_2011A_08Nov_part_32",
#"Mu_2011A_08Nov_part_33",
#"Mu_2011A_08Nov_part_34",
#"Mu_2011A_08Nov_part_35",
#"Mu_2011A_08Nov_part_36",
#"Mu_2011A_08Nov_part_37",
#"Mu_2011A_08Nov_part_38",
#"Mu_2011A_08Nov_part_39",
#"Mu_2011A_08Nov_part_40",

#"Mu_2011B_19Nov_part_1",
#"Mu_2011B_19Nov_part_2",
#"Mu_2011B_19Nov_part_3",
#"Mu_2011B_19Nov_part_4",
#"Mu_2011B_19Nov_part_5",
#"Mu_2011B_19Nov_part_6",
#"Mu_2011B_19Nov_part_7",
#"Mu_2011B_19Nov_part_8",
#"Mu_2011B_19Nov_part_9",
#"Mu_2011B_19Nov_part_10",
#"Mu_2011B_19Nov_part_11",
#"Mu_2011B_19Nov_part_12",
#"Mu_2011B_19Nov_part_13",
#"Mu_2011B_19Nov_part_14",
#"Mu_2011B_19Nov_part_15",
#"Mu_2011B_19Nov_part_16",
#"Mu_2011B_19Nov_part_17",
#"Mu_2011B_19Nov_part_18",
#"Mu_2011B_19Nov_part_19",
#"Mu_2011B_19Nov_part_20",
#"Mu_2011B_19Nov_part_21",
#"Mu_2011B_19Nov_part_22",
#"Mu_2011B_19Nov_part_23",
#"Mu_2011B_19Nov_part_24",
#"Mu_2011B_19Nov_part_25",
#"Mu_2011B_19Nov_part_26",
#"Mu_2011B_19Nov_part_27",
#"Mu_2011B_19Nov_part_28",
#"Mu_2011B_19Nov_part_29",
#"Mu_2011B_19Nov_part_30",
#"Mu_2011B_19Nov_part_31",
#"Mu_2011B_19Nov_part_32",
#"Mu_2011B_19Nov_part_33",
#"Mu_2011B_19Nov_part_34",
#"Mu_2011B_19Nov_part_35",
#"Mu_2011B_19Nov_part_36",
#"Mu_2011B_19Nov_part_37",
#"Mu_2011B_19Nov_part_38",
#"Mu_2011B_19Nov_part_39",
#"Mu_2011B_19Nov_part_40",




#
#


#"QCD_Pt_20to30_BCtoE",
#"QCD_Pt_30to80_BCtoE",
#"QCD_Pt_80to170_BCtoE",
#"QCD_Pt_20to30_EMEnriched",
#"QCD_Pt_30to80_EMEnriched",
#"QCD_Pt_80to170_EMEnriched",


#"QCD_HT_40_100_GJets",
#"QCD_HT_100_200_GJets",
#"QCD_HT_200_inf_GJets",

    





 





#### NOT USED
#"ZZ_part_1",
#"ZZ_part_2",
#"ZZ_part_3",
#"ZZ_part_4",
#"ZZ_part_5",
#"ZZ_part_6",
#"ZZ_part_7",
#"ZZ_part_8",
#"ZZ_part_9",
#"ZZ_part_10",
#"ZZ_part_11",
#"ZZ_part_12",
#"ZZ_part_13",
#"ZZ_part_14",
#"ZZ_part_15",
#"ZZ_part_16",
#"ZZ_part_17",
#"ZZ_part_18",
#"ZZ_part_19",
#"ZZ_part_20",

#"WJets_part_1",
#"WJets_part_2",
#"WJets_part_3",
#"WJets_part_4",
#"WJets_part_5",
#"WJets_part_6",
#"WJets_part_7",
#"WJets_part_8",
#"WJets_part_9",
#"WJets_part_10",
#"WJets_part_11",
#"WJets_part_12",
#"WJets_part_13",
#"WJets_part_14",
#"WJets_part_15",
#"WJets_part_16",
#"WJets_part_17",
#"WJets_part_18",
#"WJets_part_19",
#"WJets_part_20",


  ### 
 ]

#Path to take data merged files
#dataPath = "rfio:/castor/cern.ch/user//m/mmerola/SingleTop_2012/MergedJune/"
dataPath = "file:/data3/scratch/users/fabozzi/SingleTop/ntp11sep14_Merged/"

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
    if "WJets" in channelNew and not "Q2" in channelNew and not "Matching" in channelNew:
        channelToReplace = "WJets"
    if "WJetsQ2up" in channelNew:
        channelToReplace = "WJetsQ2up"
    if "WJetsQ2down" in channelNew:
        channelToReplace = "WJetsQ2down"
    if "WJetsMatchingup" in channelNew:
        channelToReplace = "WJetsMatchingup"
    if "WJetsMatchingdown" in channelNew:
        channelToReplace = "WJetsMatchingdown"
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
    if "TTBar" in channelNew and not "Q2" in channelNew and not "Matching" in channelNew and not "Mass" in channelNew:
        channelToReplace = "TTBar"
    if "TTBarQ2up" in channelNew : 
        channelToReplace = "TTBarQ2up"
    if "TTBarQ2down" in channelNew : 
        channelToReplace = "TTBarQ2down"
    if "TTBarMatchingup" in channelNew : 
        channelToReplace = "TTBarMatchingup"
    if "TTBarMatchingdown" in channelNew : 
        channelToReplace = "TTBarMatchingdown"                
    if "TTBarMassup" in channelNew : 
        channelToReplace = "TTBarMassup"
    if "TTBarMassdown" in channelNew : 
        channelToReplace = "TTBarMassdown"                

    if "TChannel" in channelNew and not "Q2" in channelNew and not "Mass" in channelNew:
        channelToReplace = "TChannel"        
    if "TChannelQ2up" in channelNew:
        channelToReplace = "TChannelQ2up"        
    if "TChannelQ2down" in channelNew:
        channelToReplace = "TChannelQ2down"        
    if "TChannelMassup" in channelNew:
        channelToReplace = "TChannelMassup"        
    if "TChannelMassdown" in channelNew:
        channelToReplace = "TChannelMassdown"        

    if "TbarChannel" in channelNew and not "Q2" in channelNew and not "Mass" in channelNew:
        channelToReplace = "TbarChannel"        
    if "TbarChannelQ2up" in channelNew:
        channelToReplace = "TbarChannelQ2up"        
    if "TbarChannelQ2down" in channelNew:
        channelToReplace = "TbarChannelQ2down"        
    if "TbarChannelMassup" in channelNew:
        channelToReplace = "TbarChannelMassup"        
    if "TbarChannelMassdown" in channelNew:
        channelToReplace = "TbarChannelMassdown"        

    if "TWChannel" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "TWChannel"        
    if "TbarWChannel" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "TbarWChannel"        
    if "QCDMu" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "QCDMu"
    if "WW" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "WW"        
    if "WZ" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "WZ"        
    if "ZZ" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "ZZ"
        
    if "SChannel" in channelNew and not "Q2" in channelNew and not "Mass" in channelNew and not "CompHep" in channelNew:  #=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "SChannel"
    if "SChannelCompHep" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "SChannelCompHep"        
    if "SChannelQ2up" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "SChannelQ2up"        
    if "SChannelQ2down" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "SChannelQ2down"        
    if "SChannelMassup" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "SChannelMassup"        
    if "SChannelMassdown" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "SChannelMassdown"        

    if "SbarChannel" in channelNew and not "Q2" in channelNew and not "Mass" in channelNew:  #=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "SbarChannel"
    if "SbarChannelQ2up" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "SbarChannelQ2up"        
    if "SbarChannelQ2down" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "SbarChannelQ2down"        
    if "SbarChannelMassup" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "SbarChannelMassup"        
    if "SbarChannelMassdown" in channelNew:#=="DataMu" or channelNew == "DataEle" or channelNew == "DataMuQCD" or channelNew =="DataEleQCD":
        channelToReplace = "SbarChannelMassdown"        


    file = open(fileName)
    lines = file.readlines()
    o = open(channelNew+"_cfg.py","w") 
    for line in lines:
#        print "THIS IS THE LINE: ", line
        if '"channel_instruction"' in line:
#            print "BEFORE ", line
            line = line.replace('"channel_instruction"','"'+switch+'"')
#            print "AFTER REPLACE ", line
        if "MC_instruction" in line and "False" in line:
       #     if "False" in line:
#            print line
            line = line.replace("False",isMC)
#            print "AFTER REPLACE: ", line
        words = line.split()
        for word in words:
            if channelOld in word:  
                #                print " line old " + line
                if (not switch == "all") and ("process.TFileService" in line):
#                    line = line.replace(word,word.replace(channelOld,channelNew+"_HLT_IsoMu17"))
                    line = line.replace(word,word.replace(channelOld,channelNew))
#                    print "process.TFileService in line,switch " + switch +" line: \n" +line
                else:
                    line = line.replace(word,word.replace(channelOld,channelToReplace))
#        print "WRITING LINE = ", line
        o.write(line)   
    #if channel == "Data":#Temporary inelegant solution due to the separation of mu/e: will fix it at some point
        #        line = "process.source.fileNames = cms.untracked.vstring('"+dataPath+"DataMuMerged.root','"+dataPath+"DataEleMerged.root',)"
        #        line = "process.source.fileNames = cms.untracked.vstring('"+dataPath+"DataMuMerged.root',)"
        #       line = "process.source.fileNames = cms.untracked.vstring('"+dataPath+"Mu_v1Merged.root','"+dataPath+"Mu_v2Merged.root','"+dataPath+"Ele_v1Merged.root','"+dataPath+"Ele_v2Merged.root',)"
    if "WJets" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channel+"Merged.root',"
        inputs = inputs +")"
        o.write(inputs)
    if "QCDMu" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        #        inputs = inputs.replace(channelToReplace,"QCDMu")
        inputs = inputs +")"
        print "inputs = ", inputs
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
#        print "inputs = ", inputs
        o.write(inputs)
    if "TTBar" in channelNew: 
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        inputs = inputs +")"
        o.write(inputs)
    if "SChannel" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        #    inputs = inputs.replace(channelToReplace,"TChannel")
        inputs = inputs +")"
        o.write(inputs)
    if "SbarChannel" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        #    inputs = inputs.replace(channelToReplace,"TChannel")
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
    if "TWChannel" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
        #    inputs = inputs.replace(channelToReplace,"TChannel")
        inputs = inputs +")"
        o.write(inputs)
    if "TbarWChannel" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
        inputs = "process.source.fileNames = cms.untracked.vstring("
        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
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
#    if "SChannelCompHep" in channelNew:# == "DataMu" or channelNew == "DataMuQCD":
#        inputs = "process.source.fileNames = cms.untracked.vstring("
#        inputs = inputs +"'"+dataPath+channelNew+"Merged.root',"
#        #    inputs = inputs.replace(channelToReplace,"TChannel")
#        inputs = inputs +")"
#        o.write(inputs)
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



