def listCuts( cut,sample,lepton):
    
    KinCut = "  TString KinCut = "
    
    #    KinCut = KinCut + "TString(\"*(secondJetPt > 0. && bJetDecRMS < 10.025 && bJetFinRMS < 10.025 && leptonDeltaCorrectedRelIso<0.06 && thirdJetPt>40)\")"
    #    KinCut = KinCut + "TString(\"*(secondJetPt > 0. && bJetDecRMS < 10.025 && bJetFinRMS < 10.025 && leptonDeltaCorrectedRelIso<0.06)\")"
    
    #    KinCut = KinCut + "TString(\"*(secondJetPt > 0. && bJetRMS < 10.025 && fJetRMS < 10.025 && leptonDeltaCorrectedRelIso<0.06)\")"

    #   KinCut = KinCut + "TString(\"*(secondJetPt > 0. && bJetRMS < 10.025 && fJetRMS < 10.025 && bJetPt > 60 && fJetPt > 60 && leptonDeltaCorrectedRelIso<0.06)\")"

    #    KinCut = KinCut + "TString(\"*(leptonRelIso<10.06)\")"
#    KinCut = KinCut + "TString(\"\")"

    if sample == "2J_1T":
        KinCut = KinCut+"+TString(\"*(mtwMass > 50)\")"
#    KinCut = KinCut+"+TString(\"*( (mtwMass > 50) && (nJLoose>0) )\")"
#    KinCut = KinCut+"+TString(\"*( (mtwMass > 50) && (nJLoose>0) && (looseJetPt>35) )\")"
#    KinCut = KinCut+"+TString(\"*((mtwMass > 50) && (leptonPt > 27)) \")"


    #   KinCut = KinCut + "TString(\"*(secondJetPt > 0. && bJetDecRMS < 10.025 && bJetFinRMS < 10.025 )\")"
    #   KinCut = KinCut + "TString(\"*(secondJetPt > 0. && fJetRMS < 0.025 && bJetRMS < 10.025  )\")"
#    if lepton == "Mu":
#        KinCut = KinCut + "+TString(\"*0.995*0.995\")"

#    if "2J_0T" in sample:
#        KinCut = KinCut + "+TString(\"*(bJetRMS < 10.025  && fJetRMS < 10.025)\")"
        
    if "SR" in cut:
        KinCut = KinCut + "+TString(\"*(topMassLR > 130 && topMassLR <220)\")"
    if "SB" in cut:
        KinCut = KinCut + "+TString(\"*(!(topMass > 130 && topMass <220))\")"
    if "Plus" in cut:
        KinCut = KinCut + "+TString(\"*(charge > 0)\")"
    if "Minus" in cut:
        KinCut = KinCut + "+TString(\"*(charge < 0)\")"

    if not "noQCDCut" in cut:
        if lepton == "Mu":
            KinCut = KinCut+"+TString(\"*(mtwMass > 50)\")"
            #            KinCut = KinCut+"+TString(\"*(metPt > 45)\")"
        if lepton == "Ele":
            KinCut = KinCut+"+TString(\"*(metPt > 45)\")"            
  
    if "mtwCut" in cut:
        KinCut = KinCut + "+TString(\"*(mtwMass > 10 && mtwMass < 100)\")"

    return KinCut+";\n"



def listCutsQCD( cut,sample,lepton):
    
    KinCutQCDDD = "  TString KinCutQCDDD = "
#    KinCutQCDDD = KinCutQCDDD+"+TString(\"((mtwMass > 50) && (nJLoose>0) && (looseJetPt>35))\")"
#    KinCutQCDDD = KinCutQCDDD+"+TString(\"((mtwMass > 50) && (nJLoose>0) )\")"
#    KinCutQCDDD = KinCutQCDDD+"+TString(\"(mtwMass > 50)\")"
#    KinCutQCDDD = KinCutQCDDD+"+TString(\"(mtwMass > 50) && (leptonPt > 27)\")"

#    KinCutQCDDD = KinCutQCDDD + "TString(\"(sqrt((leptonPhi-bJetFinPhi)**2+(leptonEta-bJetFinEta)**2)>0.3 && sqrt((leptonPhi-bJetDecPhi)**2+(leptonEta-bJetDecEta)**2)>0.3)\")"


#    KinCutQCDDD = KinCutQCDDD + "TString(\"(sqrt(pow(leptonPhi-fJetPhi,2)+pow(leptonEta-fJetEta,2))>0.3 && sqrt(pow(leptonPhi-bJetPhi,2)+pow(leptonEta-bJetEta,2))>0.3)\")"

    if ((sample == "2J_0T") or (sample == "2J_1T") or (sample == "2J_2T")):
        KinCutQCDDD = KinCutQCDDD + "TString(\"((DeltaR(leptonEta,leptonPhi,firstJetEta,firstJetPhi)>0.3) && (DeltaR(leptonEta,leptonPhi,secondJetEta,secondJetPhi)>0.3))\")"

    if ((sample == "3J_1T") or (sample == "3J_2T")):
        KinCutQCDDD = KinCutQCDDD + "TString(\"((DeltaR(leptonEta,leptonPhi,firstJetEta,firstJetPhi)>0.3) && (DeltaR(leptonEta,leptonPhi,secondJetEta,secondJetPhi)> 0.3) && (DeltaR(leptonEta,leptonPhi,thirdJetEta,thirdJetPhi)>0.3))\")"
   
    if sample == "4J_2T":
        KinCutQCDDD = KinCutQCDDD + "TString(\"((DeltaR(leptonEta,leptonPhi,firstJetEta,firstJetPhi)>0.3) && (DeltaR(leptonEta,leptonPhi,secondJetEta,secondJetPhi)> 0.3) && (DeltaR(leptonEta,leptonPhi,thirdJetEta,thirdJetPhi)>0.3) && (DeltaR(leptonEta,leptonPhi,fourthJetEta,fourthJetPhi)>0.3)) \")"

#    if "costhetaljCut" in cut:
#        KinCutQCDDD = "  TString KinCutQCDDD = "
#    KinCutQCDDD = KinCutQCDDD + "+TString(\"*(costhetalj_bJet<0.99 && costhetalj<0.99)\")"


    if sample == "2J_1T":
         KinCutQCDDD = KinCutQCDDD + "+TString(\"*(mtwMass > 50)\")"
    return KinCutQCDDD+";\n"

#def listCutsData( cut,sample,lepton):
#    cutData = "  TString cutData = "
#    if "costhetaljCut" in cut:
#        cutData = cutData + "TString(\"(costhetalj_new<0.99)\")"
#    return cutData+";\n"


                    
def listNormalizations( cut,sample,lepton):
# taking qcd norm from MC (QCDIntegral = 0 or no specified)
    if sample == "2J_0T":
#        return " WJetsScale = 1.2; TTBarScale =1.04; QCDIntegral = 0; \n"
        return " WJetsScale = 1.; TTBarScale =1.04; QCDIntegral = 23944; \n"
    if sample == "2J_1T":
#        return " WJetsScale = 1.;TTBarScale =1.04; QCDIntegral = 5733 ; \n"
        return " WJetsScale = 1.;TTBarScale =1.04; QCDIntegral = -1 ; \n"
    if sample == "2J_2T":
        return " WJetsScale = 1.;TTBarScale =1.04; QCDIntegral = 67; \n"
    if sample == "3J_1T":
        return " WJetsScale = 1.;TTBarScale =1.04; QCDIntegral = 1127; \n"
    if sample == "3J_2T":
        return " WJetsScale = 1.;TTBarScale =1.04; QCDIntegral = 41; \n"
    if sample == "4J_2T":
        return " WJetsScale = 1.;TTBarScale =1.04; QCDIntegral = 110 ; \n"


def listSamples( variable, sample):

    if variable == "topPt":
        return "TString observable = \"topPt\";   double observableMin = 30;   double observableMax = 180;  TString observableName = \"P_{T,lb\#nu}\"; double nBins =20; TString oTitle = \"topPt\";"

    if variable == "BDT":
        return "TString observable = \"BDT\";   double observableMin = -0.7;   double observableMax = 0.5;  TString observableName = \"BDT Discriminant\"; double nBins =20; TString oTitle = \"BDT2J2T\";"

    if variable == "BDT3J2T":
        return "TString observable = \"BDT3J2T\";   double observableMin = 0.1;   double observableMax = 0.6;  TString observableName = \"BDT Discriminant\"; double nBins =15; TString oTitle = \"BDT3J2T\";"

    if variable == "BDT2J2T":
        return "TString observable = \"BDT2J2T\";   double observableMin = -0.8;   double observableMax = 0.2;  TString observableName = \"BDT Discriminant\"; double nBins =5; TString oTitle = \"BDT2J2T\";"

    if variable == "BDT2J1T":
        return "TString observable = \"BDT2J1T\";   double observableMin = -0.55;   double observableMax = 0.05;  TString observableName = \"BDT Discriminant\"; double nBins = 15; TString oTitle = \"BDT2J1T\";"

    if variable == "BDT2J2Tqcd":
        return "TString observable = \"BDT2J2Tqcd\";   double observableMin = -0.8;   double observableMax = 0.4;  TString observableName = \"BDT Discriminant\"; double nBins =12; TString oTitle = \"BDT2J2T\";"

    if variable == "bJetPt":
        return "TString observable = \"bJetPt\";   double observableMin = 40;   double observableMax = 200;  TString observableName = \" p_{T,b}\"; double nBins = 15; TString oTitle = \"bJetPt\";"
    
    if variable == "fJetPt":
        return "TString observable = \"fJetPt\";   double observableMin = 40;   double observableMax = 200;  TString observableName = \" p_{T,f}\"; double nBins = 15; TString oTitle = \"fJetPt\";"
    
    if variable == "eta":
        return "TString observable = \"eta\";   double observableMin = 0;   double observableMax = 5;  TString observableName = \"\#eta_{lq}\"; double nBins = 30; TString oTitle = \"etalj\";"

    if variable == "topMass" : 
        if sample == "2J_0T":
            return "TString observable = \"topMass\";   double observableMin = 100;   double observableMax = 400;  TString observableName = \"m_{lb\#nu}\"; double nBins = 30; TString oTitle = \"topMass\";"
        return "TString observable = \"topMass\";   double observableMin = 100;   double observableMax = 300;  TString observableName = \"m_{lb\#nu}\"; double nBins = 20; TString oTitle = \"topMass\";"

    if variable == "topMassLR":
        if sample == "2J_0T":
            return "TString observable = \"topMassLR\";   double observableMin = 100;   double observableMax = 400;  TString observableName = \"m_{lb\#nu}\"; double nBins = 30; TString oTitle = \"topMassLR\";"
        if sample == "3J_2T":
            return "TString observable = \"topMassLR\";   double observableMin = 100;   double observableMax = 300;  TString observableName = \"m_{lb\#nu}(GeV)\"; double nBins = 25; TString oTitle = \"topMassLR\";"
        return "TString observable = \"topMassLR\";   double observableMin = 100;   double observableMax = 300;  TString observableName = \"m_{lb\#nu}(GeV)\"; double nBins = 20; TString oTitle = \"topMassLR\";"

    if variable == "topMass_best":
        return "TString observable = \"topMass_best\";   double observableMin = 100;   double observableMax = 300;  TString observableName = \"m_{lb\#nu}(GeV)\"; double nBins = 20; TString oTitle = \"topMass_best\";"
        
        
    if variable == "secondJetPt":
        return "TString observable = \"secondJetPt\";   double observableMin = 40;   double observableMax = 240;  TString observableName = \"p_{T,second jet}\"; double nBins = 20; TString oTitle = \"secondJetPt\";"

    if variable == "firstJetPt":
        return "TString observable = \"firstJetPt\";   double observableMin = 40;   double observableMax = 240;  TString observableName = \"p_{T,leading jet}\"; double nBins = 20; TString oTitle = \"firstJetPt\";"

    if variable == "bJetDecPt":
        return "TString observable = \"bJetDecPt\";   double observableMin = 40;   double observableMax = 200;  TString observableName = \"p_{T,dec}\"; double nBins = 16; TString oTitle = \"bJetDecPt\";"

    if variable == "bJetFinPt":
        return "TString observable = \"bJetFinPt\";   double observableMin = 40;   double observableMax = 240;  TString observableName = \"p_{T,recoil}\"; double nBins = 15; TString oTitle = \"bJetFinPt\";"

    if variable == "thirdJetPt":
        return "TString observable = \"thirdJetPt\";   double observableMin = 30;   double observableMax = 180;  TString observableName = \"p_{T,third}\"; double nBins = 15; TString oTitle = \"thirdJetPt\";"

    if variable == "bJetDecRMS":
        return "TString observable = \"bJetDecRMS\";   double observableMin = 0;   double observableMax = 0.1;  TString observableName = \"RMS_{b-top j}\"; double nBins = 30; TString oTitle = observable;"
        
    if variable == "bJetFinRMS":
        return "TString observable = \"bJetFinRMS\";   double observableMin = 0;   double observableMax = 0.1;  TString observableName = \"RMS_{b-recoil j}\"; double nBins = 30; TString oTitle = observable;"

    if variable == "bJetRMS":
        return "TString observable = \"bJetRMS\";   double observableMin = 0;   double observableMax = 0.1;  TString observableName = \"RMS_{bj}\"; double nBins = 30; TString oTitle = observable;"

    if variable == "fJetRMS":
        return "TString observable = \"fJetRMS\";   double observableMin = 0;   double observableMax = 0.1;  TString observableName = \"RMS_{fj}\"; double nBins = 30; TString oTitle = observable;"
    
    if variable == "metPt":
        return "TString observable = \"metPt\";   double observableMin = 0;   double observableMax = 200;  TString observableName = \"E_{T,miss}(GeV)\"; double nBins = 14;TString oTitle = observable;"

    if variable == "metPhi":
        return "TString observable = \"metPhi\";   double observableMin = -6.28;   double observableMax = 6.28;  TString observableName = \"#phi_{miss}\"; double nBins = 20;TString oTitle = observable;"

    if variable == "costhetalj":
        return "TString observable =\"costhetalj\";  double observableMin = -1;   double observableMax = 1;   TString observableName = \"cos\#theta^{*}\"; double nBins =10;TString oTitle = observable;"

    if variable == "costhetalj_new":
        return "TString observable =\"costhetalj_new\";  double observableMin = -1;   double observableMax = 1;   TString observableName = \"cos\#theta^{*}\"; double nBins =11;TString oTitle = observable;"

    if variable == "costhetalj_bJet":
        return "TString observable =\"costhetalj_bJet\";  double observableMin = -1;   double observableMax = 1;   TString observableName = \"cos\#theta^{*}\"; double nBins =11;TString oTitle = observable;"

    if variable == "costhetalbl" :
        return "TString observable =\"costhetalbl\";  double observableMin = -1;   double observableMax = 1;   TString observableName = \"cos\#theta_{l,bl}\"; double nBins =15;TString oTitle = observable;"

    if variable == "costhetalbl_best" :
        return "TString observable =\"costhetalbl_best\";  double observableMin = -1;   double observableMax = 1;   TString observableName = \"cos\#theta_{l,bl}\"; double nBins =9;TString oTitle = observable;"

    if variable == "costhetalbl_new" :
        return "TString observable =\"costhetalbl_new\";  double observableMin = -1;   double observableMax = 1;   TString observableName = \"cos\#theta_{l,bl}\"; double nBins =9;TString oTitle = observable;"

    if variable == "leptonDeltaCorrectedRelIso":
        if sample == "2J_0T":
            return "TString observable = \"leptonDeltaCorrectedRelIso\";   double observableMin = 0.0;   double observableMax = 0.12;  TString observableName = \"Iso_{rel}^{dBeta}\"; double nBins = 15;TString oTitle = observable;"
        return "TString observable = \"leptonDeltaCorrectedRelIso\";   double observableMin = 0.0;   double observableMax = 0.06;  TString observableName = \"Iso_{rel}^{dBeta}\"; double nBins = 15;TString oTitle = observable;"
        

        
    if variable == "leptonRhoCorrectedRelIso":
        return "TString observable = \"leptonRhoCorrectedRelIso\";   double observableMin = 0.0;   double observableMax = 0.1;  TString observableName = \"Iso_{rel}^{rho}\"; double nBins = 20;TString oTitle = observable;"

    if variable == "leptonRelIso":
        return "TString observable = \"leptonRelIso\";   double observableMin = 0.0;   double observableMax = 0.4;  TString observableName = \"Iso_{rel}\"; double nBins = 30; TString oTitle = observable;"

    if variable == "leptonPt":
        #        return "TString observable = \"leptonPt\";   double observableMin = 20;   double observableMax = 160;  TString observableName = \"p_{T,\#mu}(GeV)\"; double nBins = 12;TString oTitle = observable;"
        return "TString observable = \"leptonPt\";   double observableMin = 20;   double observableMax = 160;  TString observableName = \"p_{T,\#mu}(GeV)\"; double nBins = 12;TString oTitle = observable;"

    if variable == "leptonPtZoom":
        return "TString observable = \"leptonPt\";   double observableMin = 20;   double observableMax = 40;  TString observableName = \"p_{T,\#mu}(GeV)\"; double nBins = 10;TString oTitle = observable;"


    if variable == "cosLepMetPhi":
        return "TString observable = \"cos(leptonPhi-metPhi)\";   double observableMin = -1;   double observableMax = 1;  TString observableName = \"cos#Delta#phi(E_{T,miss},l)\"; double nBins = 20;TString oTitle = \"cosLepMetPhi\";"


    if variable == "charge":
        return "TString observable = \"charge\";   double observableMin = -1.5;   double observableMax = 1.5;  TString observableName = \"lepton charge\"; double nBins = 2;TString oTitle = observable;"

    if variable == "mtwMass":
        if sample == "2J_0T":
            return "TString observable = \"mtwMass\";   double observableMin = 0;   double observableMax = 200;  TString observableName = \"m_{T}(GeV)\"; double nBins = 40;TString oTitle = observable;"
        return "TString observable = \"mtwMass\";   double observableMin = 0;   double observableMax = 250;  TString observableName = \"m_{T}(GeV)\"; double nBins = 20;TString oTitle = observable;"
   
    if variable == "HT":
        return "TString observable = \"HT\";   double observableMin = 0;   double observableMax = 500;  TString observableName = \"p_{T}^{tot}(GeV)\"; double nBins = 20; TString oTitle = \"HT\";"
    
    if variable == "b1b2Mass":
        return "TString observable = \"b1b2Mass\";   double observableMin = 0;   double observableMax = 500;  TString observableName = \"m_{bb}(GeV)\"; double nBins = 20; TString oTitle = \"b1b2Mass\";"

    if variable == "b1b2Pt":
        return "TString observable = \"b1b2Pt\";   double observableMin = 0;   double observableMax = 300;  TString observableName = \"p_{T}^{bb}(GeV)\"; double nBins = 15; TString oTitle = \"b1b2Pt\";"

    if variable == "Mlb1":
        return "TString observable = \"Mlb1\";   double observableMin = 0;   double observableMax = 500;  TString observableName = \"m_{lb}(GeV)\"; double nBins = 20; TString oTitle = \"Mlb1\";"
    if variable == "Mlb2":
        return "TString observable = \"Mlb2\";   double observableMin = 0;   double observableMax = 500;  TString observableName = \"m_{lb}(GeV)\"; double nBins = 20; TString oTitle = \"Mlb2\";"
    
    if variable == "DeltaEta_b1b2":
        return "TString observable = \"abs(bJet1Eta-bJet2Eta)\";   double observableMin = 0;   double observableMax = 4;  TString observableName = \"#Delta#eta_{bb}\"; double nBins = 20; TString oTitle = \"DeltaEta_b1b2\";"

    if variable == "DeltaPhi_b1b2":
        return "TString observable = \"DeltaPhi(bJet1Phi,bJet2Phi)\";   double observableMin = -8;   double observableMax = 8;  TString observableName = \"#Delta#phi_{bb}\"; double nBins = 24; TString oTitle = \"DeltaPhi_b1b2\";"

    if variable == "DeltaPhi_topbJetFin":
        return "TString observable = \"DeltaPhi(topPhi,bJetFinPhi)\";   double observableMin = 0;   double observableMax = 3.14;  TString observableName = \"#Delta#phi_{top,bJetRecoil}\"; double nBins = 15; TString oTitle = \"DeltaPhi_topbJetFin\";"
    
    if variable == "DeltaPhi_topbJet1":
        return "TString observable = \"DeltaPhi(topPhi,bJet1Phi)\";   double observableMin = 0;   double observableMax = 3.14;  TString observableName = \"#Delta#phi_{top,bJet1}\"; double nBins = 15; TString oTitle = \"DeltaPhi_topbJet1\";"
    
    if variable == "DeltaPhi_topfJet":
        return "TString observable = \"DeltaPhi(topPhi,fJetPhi)\";   double observableMin = 0;   double observableMax = 3.14;  TString observableName = \"#Delta#phi_{top,fJet}\"; double nBins = 15; TString oTitle = \"DeltaPhi_topfJet\";"
    
    if variable == "DeltaPhi_besttopbJetRecoil":
        return "TString observable = \"DeltaPhi(topPhi_best,(bJetPhi*(!bJetIsbest)+fJetPhi*bJetIsbest))\";   double observableMin = 0;   double observableMax = 8;  TString observableName = \"#Delta#phi_{top,bJetRecoil}\"; double nBins = 12; TString oTitle = \"DeltaPhi_besttopbJetRecoil\";"
    
    if variable == "DeltaR_b1b2":
        return "TString observable = \"DeltaR(bJet1Eta,bJet1Phi,bJet2Eta,bJet2Phi)\";   double observableMin = 0;   double observableMax = 7;  TString observableName = \"#Delta R_{bb}\"; double nBins = 14; TString oTitle = \"DeltaR_b1b2\";"

    if variable == "DeltaR_lep_leadingjet":
        return "TString observable = \"DeltaR(leptonEta,leptonPhi,firstJetEta,firstJetPhi)\";   double observableMin = 0;   double observableMax = 8;  TString observableName = \"#Delta R_{lep - leading jet}\"; double nBins = 8; TString oTitle = \"DeltaR_lep_leadingjet\";"
    
    if variable == "Comb1":
        return "TString observable = \"0.83*mtwMass+0.557763*metPt\";   double observableMin = 0;   double observableMax = 300;  TString observableName = \"Mtw-met comb1\"; double nBins = 30; TString oTitle = \"Comb1\";"
    
    if variable == "Comb2":
        return "TString observable = \"0.557763*mtwMass-0.83*metPt\";   double observableMin = -100;   double observableMax = 100;  TString observableName = \"Mtw-met comb2\"; double nBins = 30; TString oTitle = \"Comb2\";"

    if variable == "nJLoose":
        return "TString observable = \"nJLoose\";   double observableMin = 0;   double observableMax = 8;  TString observableName = \"nJetsLoose\"; double nBins = 8; TString oTitle = \"nJetsLoose\";"

    if variable == "looseJetPt":
        return "TString observable = \"looseJetPt\";   double observableMin = 20;   double observableMax = 40;  TString observableName = \"looseJetPt\"; double nBins = 20; TString oTitle = \"looseJetPt\";"

    if variable == "nVertices":
        return "TString observable = \"nVertices\";   double observableMin = 0;   double observableMax = 20;  TString observableName = \"nVertices\"; double nBins = 20; TString oTitle = \"nVertices\";"

    if variable == "bJet1Pt":
        return "TString observable = \"bJet1Pt\";   double observableMin = 40;   double observableMax = 200;  TString observableName = \" p_{T,b1}\"; double nBins = 15; TString oTitle = \"bJet1Pt\";"
    
    if variable == "bJet2Pt":
        return "TString observable = \"bJet2Pt\";   double observableMin = 40;   double observableMax = 200;  TString observableName = \" p_{T,b2}\"; double nBins = 15; TString oTitle = \"bJet2Pt\";"
    
