def listCuts( cut,sample,lepton):

    KinCut = "  TString KinCut = \"\""
    
#    KinCut = KinCut+"+TString(\"*((mtwMass > 50) && (nJLoose>0)) \")"
    KinCut = KinCut+"+TString(\"*(mtwMass > 50)\")"

    #KinCut = KinCut + "TString(\"*(secondJetPt > 0. && fJetRMS < 0.025 && bJetRMS<10.025)\")"
   # KinCut = KinCut + "TString(\"*(secondJetPt > 0. && bJetRMS<10.025)\")"
#    if lepton == "Mu":
#        KinCut = KinCut + "+TString(\"*0.995*0.995\")"

#    if "2J_0T" in sample:
#        KinCut = KinCut #+ "+TString(\"*(bJetRMS < 0.025)\")"
        
    if "SR" in cut:
        KinCut = KinCut + "+TString(\"*(topMass > 130 && topMass <220)\")"
    if "SB" in cut:
        KinCut = KinCut + "+TString(\"*(!(topMass > 130 && topMass <220))\")"
    if "Plus" in cut:
        KinCut = KinCut + "+TString(\"*(charge > 0)\")"
    if "Minus" in cut:
        KinCut = KinCut + "+TString(\"*(charge < 0)\")"

    if not "noQCDCut" in cut:
        if lepton == "Mu":
            #KinCut = KinCut+"+TString(\"*(metPt > 45)\")"
            KinCut = KinCut+"+TString(\"*(mtwMass > 50)\")"
        if lepton == "Ele":
            KinCut = KinCut#+"+TString(\"*(metPt > 45)\")"            
    return KinCut+";\n"

def listCutsQCD( cut,sample,lepton):
    
    KinCutQCDDD = "  TString KinCutQCDDD = "

#    KinCutQCDDD = KinCutQCDDD + "TString(\"*(sqrt((leptonPhi-bJetFinPhi)**2+(leptonEta-bJetFinEta)**2)>0.3 && sqrt((leptonPhi-bJetDecPhi)**2+(leptonEta-bJetDecEta)**2)>0.3)\")"
#    KinCutQCDDD = KinCutQCDDD + "TString(\"(sqrt((leptonPhi-fJetPhi)**2+(leptonEta-fJetEta)**2)>-0.3 && sqrt((leptonPhi-bJetPhi)**2+(leptonEta-bJetEta)**2)>-0.3)\")"
#    if "costhetaljCut" in cut:
#        KinCutQCDDD = "  TString KinCutQCDDD = "
#    KinCutQCDDD = KinCutQCDDD + "+TString(\"*(costhetalj_bJet<0.99 && costhetalj<0.99)\")"
    
    return KinCutQCDDD+";\n"

def listNormalizations( cut,sample,lepton):
    if sample == "2J_0T":
# taking qcd norm from MC (QCDIntegral = 0 or no specified)
        return " WJetsScale = 1.; TTBarScale =1.04; QCDIntegral = -1; \n"
    if sample == "3J_1T":
        return " WJetsScale = 1.3;TTBarScale =1.04; QCDIntegral = -1; \n"
    if sample == "3J_2T":
        #return " WJetsScale = 1.3;TTBarScale =1.04; \n"
#        return " WJetsScale = 1.2;TTBarScale =1.04; QCDIntegral = -1; \n"
        return " WJetsScale = 1.;TTBarScale =1.04; QCDIntegral = -1; \n"
        #return " WJetsScale = 1.2;TTBarScale =1; QCDIntegral = 300; \n"
    if sample == "2J_2T":
        return " WJetsScale = 1.;TTBarScale =1.04; QCDIntegral = -1; \n"
       # return " WJetsScale = 1.2;TTBarScale =1; QCDIntegral = 712.5; \n"
    if sample == "3J_0T":
        return " WJetsScale = 1.2;TTBarScale =1.04; QCDIntegral = -1; \n"
    if sample == "2J_1T":
        return " WJetsScale = 1.2;TTBarScale =1.04; QCDIntegral = -1 ; \n"
#        return " WJetsScale = 1.;TTBarScale =1.04; QCDIntegral = -1 ; \n"
    if sample == "4J_2T":
        return " WJetsScale = 1.;TTBarScale =1.04; QCDIntegral = -1 ; \n"

    if sample == "2J_1T" and "SR" in cut:
        if lepton == "Mu":
            if "Plus" in cut or "Minus" in cut:
                return " WJetsScale = 1.2;TTBarScale =1.; QCDIntegral =565.468/2.; \n"
            #        return " WJetsScale = 1.;TTBarScale =1.; QCDIntegral =21239.4; \n"
            return " WJetsScale = 1.2;TTBarScale =1.; QCDIntegral =565.468; \n"
        if "Plus" in cut or "Minus" in cut:
            return " WJetsScale = 1.2;TTBarScale =1.0; QCDIntegral =867.919/2.; \n"
        return " WJetsScale = 1.2;TTBarScale =1.0; QCDIntegral =867.919; \n"

    if sample == "2J_1T" and cut == "SB":
        if lepton == "Mu":
            if "Plus" in cut or "Minus" in cut:
                return " WJetsScale = 1.2;TTBarScale =1.; QCDIntegral =264.199/2.; \n"
            #        return " WJetsScale = 1.;TTBarScale =1.; QCDIntegral =21239.4; \n"
            return " WJetsScale = 1.2;TTBarScale =1.; QCDIntegral =264.199; \n"
        if "Plus" in cut or "Minus" in cut:
            return " WJetsScale = 1.2;TTBarScale =1.0; QCDIntegral =1416.96/2.; \n"
        return " WJetsScale = 1.2;TTBarScale =1.0; QCDIntegral =1416.96; \n"

    return "\n"

#def stringCharge( cut):
#    if "Plus" in cut:
#        return "TString stringCharge=TString(\" +\");\n"
#    if "Minus" in cut:
#        return "TString stringCharge=TString(\" -\");\n"
#    return "TString stringCharge=TString(\"\");\n"

def listSamples( variable, sample):
    if variable == "topPt":
        return "TString observable = \"topPt\";   double observableMin = 0;   double observableMax = 210;  TString observableName = \"P_{T,lb\#nu}(GeV)\"; double nBins =21; TString oTitle = \"topPt\";"

    if variable == "topPt_best":
        return "TString observable = \"topPt_best\";   double observableMin = 0;   double observableMax = 210;  TString observableName = \"bestP_{T,lb\#nu}(GeV)\"; double nBins =21; TString oTitle = \"topPt_best\";"

    if variable == "bJetPt":
        return "TString observable = \"bJetPt\";   double observableMin = 30;   double observableMax = 190;  TString observableName = \" p_{T,b}\"; double nBins = 25; TString oTitle = \"bJetPt\";"
    
    if variable == "eta":
        return "TString observable = \"eta\";   double observableMin = 0;   double observableMax = 5;  TString observableName = \"\|#eta_{j'}|\"; double nBins = 30; TString oTitle = \"etalj\";"
    if variable == "fJetEta":
        return "TString observable = \"fJetEta\";   double observableMin = -5;   double observableMax = 5;  TString observableName = \"\#eta_{fj}\"; double nBins = 30; TString oTitle = \"etafj\";"

    if variable == "topEta_best":
        return "TString observable = \"topEta_best\";   double observableMin = -5;   double observableMax = 5;  TString observableName = \"\#eta_{bestTop}\"; double nBins = 30; TString oTitle = \"besttopEta\";"

    if variable == "topEta":
        return "TString observable = \"topEta\";   double observableMin = -5;   double observableMax = 5;  TString observableName = \"\#eta_{Top}\"; double nBins = 30; TString oTitle = \"topEta\";" 

    if variable == "Mlb2":
        return "TString observable = \"Mlb2\";   double observableMin = 0;   double observableMax = 200;  TString observableName = \"m_{lepton_secondJet}(GeV/c^{2})\"; double nBins = 20; TString oTitle = \"Mlb2\";"

    if variable == "Mlb1":
        return "TString observable = \"Mlb1\";   double observableMin = 0;   double observableMax = 220;  TString observableName = \"m_{lepton_firstJet}(GeV/c^{2})\"; double nBins = 22; TString oTitle = \"Mlb1\";"
    if variable == "b1b2Pt":
        return "TString observable = \"b1b2Pt\";   double observableMin = 0;   double observableMax = 220;  TString observableName = \"P_{T}^{bb}(GeV)\"; double nBins = 22; TString oTitle = \"b1b2Pt\";"

    if variable == "topMass_best":
        if sample == "2J_0T":
            return "TString observable = \"topMass_best\";   double observableMin = 100;   double observableMax = 300;  TString observableName = \"m_{lb\#nu}(GeV/c^{2})\"; double nBins = 20; TString oTitle = \"topMass_best\";"
        return "TString observable = \"topMass_best\";   double observableMin = 100;   double observableMax = 300;  TString observableName = \"m_{lb\#nu}(GeV/c^{2})\"; double nBins = 20; TString oTitle = \"topMass_best\";"
    
    if variable == "topMass":
        if sample == "2J_0T":
            return "TString observable = \"topMass\";   double observableMin = 100;   double observableMax = 400;  TString observableName = \"m_{lb\#nu}(GeV/c^{2})\"; double nBins = 30; TString oTitle = \"topMass\";"
        return "TString observable = \"topMass\";   double observableMin = 100;   double observableMax = 300;  TString observableName = \"m_{lb\#nu}(GeV/c^{2})\"; double nBins = 30; TString oTitle = \"topMass\";"

    if variable == "secondJetPt":
        return "TString observable = \"secondJetPt\";   double observableMin = 40;   double observableMax = 150;  TString observableName = \"p_{T,second jet}(GeV)\"; double nBins = 11; TString oTitle = \"secondJetPt\";"

    if variable == "firstJetPt":
        return "TString observable = \"firstJetPt\";   double observableMin = 0;   double observableMax = 240;  TString observableName = \"p_{T,leading jet}(GeV)\"; double nBins = 20; TString oTitle = \"firstJetPt\";"

    if variable == "fJetRMS":
        return "TString observable = \"fJetRMS\";   double observableMin = 0;   double observableMax = 0.1;  TString observableName = \"RMS_{lj}\"; double nBins = 30; TString oTitle = observable;"

    if  variable == "thirdJetPt":
        return "TString observable = \"thirdJetPt\";   double observableMin = 0;   double observableMax = 200;  TString observableName = \"Pt_{thirdJet}(GeV)\"; double nBins = 20;TString oTitle = observable;"

    if variable == "costhetalj":
        return "TString observable =\"costhetalj\";  double observableMin = -1;   double observableMax = 1;   TString observableName = \"cos\#theta^{*}\"; double nBins =10;TString oTitle = observable;"

    if variable == "costhetalj_best":
        return "TString observable =\"costhetalj_best\";  double observableMin = -1;   double observableMax = 1;   TString observableName = \"cos\#theta^{*}_{lj}\"; double nBins =10;TString oTitle = observable;"

    if variable == "leptonDeltaCorrectedRelIso":
        return "TString observable = \"leptonDeltaCorrectedRelIso\";   double observableMin = 0.0;   double observableMax = 0.12;  TString observableName = \"Iso_{rel}^{dBeta}\"; double nBins = 20;TString oTitle = observable;"

    if variable == "leptonRhoCorrectedRelIso":
        return "TString observable = \"leptonRhoCorrectedRelIso\";   double observableMin = 0.0;   double observableMax = 0.1;  TString observableName = \"Iso_{rel}^{rho}\"; double nBins = 24;TString oTitle = observable;"

    if variable == "leptonRelIso":
        return "TString observable = \"leptonRelIso\";   double observableMin = 0.0;   double observableMax = 0.4;  TString observableName = \"Iso_{rel}\"; double nBins = 30; TString oTitle = observable;"

    if variable == "leptonPt":
        return "TString observable = \"leptonPt\";   double observableMin = 20;   double observableMax = 140;  TString observableName = \"p_{T,\l}(GeV)\"; double nBins = 12;TString oTitle = observable;"


    if variable == "leptonEta":
        return "TString observable = \"leptonEta\";   double observableMin = -2.1;   double observableMax = 2.1;  TString observableName = \"#eta_{\l}\"; double nBins = 30;TString oTitle = observable;"
    
    if variable == "leptonPhi":
        return "TString observable = \"leptonPhi\";   double observableMin = -3.14;   double observableMax = 3.14;  TString observableName = \"#phi_{\l}\"; double nBins = 20;TString oTitle = observable;"


    if variable == "cosLepMetPhi":
        return "TString observable = \"cos(leptonPhi-metPhi)\";   double observableMin = -1;   double observableMax = 1;  TString observableName = \"cos(#Delta#phi_{E_{T,miss},\l})\"; double nBins = 20;TString oTitle = \"cosLepMetPhi\";"

    if variable == "metPt":
        return "TString observable = \"metPt\";   double observableMin = 0;   double observableMax = 210;  TString observableName = \"E_{T,miss}(GeV)\"; double nBins =21;TString oTitle = observable;"

    if variable == "charge":
        return "TString observable = \"charge\";   double observableMin = -1.5;   double observableMax = 1.5;  TString observableName = \"lepton charge\"; double nBins = 2;TString oTitle = observable;"

    if variable == "mtwMass":
        return "TString observable = \"mtwMass\";   double observableMin = 0;   double observableMax = 200;  TString observableName = \"m_{T}(GeV/c^{2})\"; double nBins = 20;TString oTitle = observable;"
  
    if variable == "HT":
        if sample == "2J_2T":
            return "TString observable = \"HT\";   double observableMin = 60;   double observableMax = 300;  TString observableName = \"H_{T}(GeV)\"; double nBins = 24; TString oTitle = observable;"
        return "TString observable = \"HT\";   double observableMin = 100;   double observableMax = 400;  TString observableName = \"H_{T}(GeV)\"; double nBins = 30; TString oTitle = observable;"

    if variable == "Pt_lepton_firstJet" :
        return "TString observable = \"sqrt((leptonPt*cos(leptonPhi)+firstJetPt*cos(firstJetPhi))**2+(leptonPt*sin(leptonPhi)+firstJetPt*sin(firstJetPhi))**2)\";double observableMin = 0;   double observableMax = 300;  TString observableName = \"Pt_{lepton+firstJet}(GeV)\"; double nBins = 15;TString oTitle = \"Pt_lepton_firstJet\";"
    
    if variable == "Pt_lepton_secondJet" :
        return "TString observable = \"sqrt((leptonPt*cos(leptonPhi)+secondJetPt*cos(secondJetPhi))**2+(leptonPt*sin(leptonPhi)+secondJetPt*sin(secondJetPhi))**2)\";double observableMin = 0;   double observableMax = 300;  TString observableName = \"Pt_{lepton+secondJet}(GeV)\"; double nBins = 15;TString oTitle = \"Pt_lepton_secondJet\";"
    
    if variable == "Pt_firstJet_secondJet" :
        return "TString observable = \"sqrt((firstJetPt*cos(firstJetPhi)+secondJetPt*cos(secondJetPhi))**2+(firstJetPt*sin(firstJetPhi)+secondJetPt*sin(secondJetPhi))**2)\";double observableMin = 0;   double observableMax = 300;  TString observableName = \"Pt_{leadingJet+secondJet}(GeV)\"; double nBins = 30;TString oTitle = \"Pt_firstJet_secondJet\";"
    
    if variable == "DeltaR_lepton_firstJet" :
        return "TString observable = \"sqrt((leptonPhi-firstJetPhi)**2+(leptonEta-firstJetEta)**2)\"; double observableMin = 0 ; double observableMax =8 ;  TString observableName = \"DeltaR_{lepton_firstJet}\"; double nBins =8 ;TString oTitle = \"DeltaR_lepton_firstJet\";"
    
    if variable == "DeltaR_lepton_secondJet" :
        return "TString observable = \"sqrt((leptonPhi-secondJetPhi)**2+(leptonEta-secondJetEta)**2)\"; double observableMin = 0 ; double observableMax =8 ;  TString observableName = \" DeltaR_{lepton_secondJet}\"; double nBins =8 ;TString oTitle = \"DeltaR_lepton_secondJet\";"

    if variable == "BJetsDeltaR" :
        return "TString observable = \"sqrt((mediumBJetPhi-highBJetPhi)**2+(highBJetEta-mediumBJetEta)**2)\"; double observableMin = 0 ; double observableMax =8 ;  TString observableName = \"#DeltaR_{Bjets}\"; double nBins =8 ;TString oTitle = \"BJetsDeltaR\";"
        
    if variable == "first_secondJetsDeltaR" :
        return "TString observable = \"sqrt((secondJetPhi-firstJetPhi)**2+(secondJetEta-firstJetEta)**2)\"; double observableMin = 0 ; double observableMax =8 ;  TString observableName = \"#DeltaR_{leadingJet_secondJet}\"; double nBins =8 ;TString oTitle = \"first_secondJetsDeltaR\";"

    if variable == "recoiledb_leptonDeltaR" :
        return "TString observable = \"sqrt((leptonPhi-(bJetPhi*(!bJetIsbest)+fJetPhi*bJetIsbest))**2+(leptonEta-(bJetEta*(!bJetIsbest)+fJetEta*bJetIsbest))**2)\"; double observableMin = 0 ; double observableMax =8 ;  TString observableName = \"#DeltaR_{b',\l}\"; double nBins =8 ;TString oTitle = \"recoiledb_leptonDeltaR\";"
    if variable == "top_recoiledb_deltaPhi" :
        return "TString observable = \"(topPhi_best)-(bJetPhi*(!bJetIsbest)+fJetPhi*bJetIsbest)\"; double observableMin = 0 ; double observableMax =8 ;  TString observableName = \"#Delta#phi_{top,b'}\"; double nBins =8 ;TString oTitle = \"top_recoiledb_deltaPhi\";"

    if variable == "BDT" :
        if sample == "2J_2T":
            return "TString observable = \"BDT2J2T\"; double observableMin = -1. ; double observableMax =0.4 ;  TString observableName = \"BDT Discriminant\"; double nBins =28 ;TString oTitle = \"BDT\";"
        return "TString observable = \"BDT3J2T\"; double observableMin = -0.4. ; double observableMax =1.;  TString observableName = \"BDT Discriminant\"; double nBins =28;TString oTitle = \"BDT\";"

    if variable == "nJLoose":
        return "TString observable = \"nJLoose\";   double observableMin = 0;   double observableMax = 8;  TString observableName = \"nJetsLoose\"; double nBins = 8; TString oTitle = \"nJetsLoose\";"

    if variable == "looseJetPt":
        return "TString observable = \"looseJetPt\";   double observableMin = 20;   double observableMax = 40;  TString observableName = \"looseJetPt\"; double nBins = 20; TString oTitle = \"looseJetPt\";"

    if variable == "DeltaR_lep_leadingjet":
        return "TString observable = \"sqrt((leptonEta-firstJetEta)^2 + (leptonPhi-firstJetPhi)^2)\";   double observableMin = 0;   double observableMax = 8;  TString observableName = \"#Delta R_{lep - leading jet}\"; double nBins = 8; TString oTitle = \"DeltaR_lep_leadingjet\";"
    

