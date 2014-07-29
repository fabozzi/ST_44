#include <memory>
#include <vector>
#include <map>
#include <set>

// user include files
#include "TopQuarkAnalysis/SingleTop/interface/SingleTopPassTriggerInfoProducer.h"

#include "FWCore/Utilities/interface/InputTag.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "DataFormats/PatCandidates/interface/TriggerPath.h"

#include "FWCore/Framework/interface/MakerMacros.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Framework/interface/TriggerNamesService.h"
#include "FWCore/Common/interface/TriggerNames.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

using namespace edm;
using namespace std;

SingleTopPassTriggerInfoProducer::SingleTopPassTriggerInfoProducer(const edm::ParameterSet& iConfig)
{
  hlTriggerResults_ = iConfig.getParameter<edm::InputTag> ("HLTriggerResults");
  init_ = false;
  
  verbose = iConfig.getUntrackedParameter<bool>("verbose",false);

  hltNameIsoMu17_ = "HLT_IsoMu17_v";  
  hltNameIsoMu24_ = "HLT_IsoMu24_v";  
  hltNameIsoMu24Eta2p1_ = "HLT_IsoMu24_eta2p1_v";  

  produces<bool>( "passIsoMu17" ).setBranchAlias( "passIsoMu17" );
  produces<bool>( "passIsoMu24" ).setBranchAlias( "passIsoMu24" );
  produces<bool>( "passIsoMu24Eta2p1" ).setBranchAlias( "passIsoMu24Eta2p1" );
 
}

SingleTopPassTriggerInfoProducer::~SingleTopPassTriggerInfoProducer()
{
}

void SingleTopPassTriggerInfoProducer::produce( edm::Event& iEvent,const  edm::EventSetup& c)
{
  
  auto_ptr<bool> trigOKIsoMu17_( new bool );
  auto_ptr<bool> trigOKIsoMu24_( new bool );
  auto_ptr<bool> trigOKIsoMu24Eta2p1_( new bool );

  *trigOKIsoMu17_ = false;
  *trigOKIsoMu24_ = false;
  *trigOKIsoMu24Eta2p1_ = false;

  int ievt = iEvent.id().event();
  int irun = iEvent.id().run();
  int ils = iEvent.luminosityBlock();
  int bx = iEvent.bunchCrossing();
  
  //
  // trigger type
  //
  int trigger_type=-1;
  if (iEvent.isRealData())  trigger_type = iEvent.experimentType();
  
  
  //hlt info
  edm::Handle<TriggerResults> HLTR;

  //  if(isMC)hlTriggerResults_ = edm::InputTag("TriggerResults","","REDIGI311X");

  iEvent.getByLabel(hlTriggerResults_,HLTR);

  //  std::cout << " TriggerFilter module running" <<std::endl;


  if(HLTR.isValid() == false) {
    std::cout<< " HLTInspect Error - Could not access Results with name "<<hlTriggerResults_<<std::endl;
  }
  if(HLTR.isValid()) {
    if (!init_) {
      //    init_=true;
      const edm::TriggerNames & triggerNames = iEvent.triggerNames(*HLTR);
      hlNames_=triggerNames.triggerNames();
    }
    
    string tmptrig="";      
    string tmptrig2="";      
    TriggerResults tr;
    tr = *HLTR;
    bool passesTrigger = false;
    bool tmppass=false;
    //      std::cout << "List of triggers: \n";
    for (unsigned int i=0;i<HLTR->size();++i){
		
	tmptrig = hlNames_[i];
	tmppass = tr.accept(i);
	tmptrig.erase(tmptrig.end()-1);
	tmptrig2 = tmptrig;
	tmptrig2.erase(tmptrig2.end()-1);
	
	//	std::cout.width(3); std::cout << i;
	//	std::cout << " - 2" <<  tmptrig << "   " << tmppass << std::endl;
	
	if(( tmptrig == hltNameIsoMu17_ ) && (tmppass)) { 
	  if (verbose) cout << " run " << irun << " passes trigger IsoMu17" << endl; 
	  *trigOKIsoMu17_ = true;
	} else {
	  if(( tmptrig2 == hltNameIsoMu17_ ) && (tmppass)) { 
	    if (verbose) cout << " run " << irun << " passes trigger IsoMu17" << endl; 
	    *trigOKIsoMu17_ = true;
	  }
	}
	
	if(( tmptrig == hltNameIsoMu24_ ) && (tmppass)) { 
	  if (verbose)cout << " run " << irun << " passes trigger IsoMu24" << endl; 
	  *trigOKIsoMu24_ = true;
	} else {
	  if(( tmptrig2 == hltNameIsoMu24_ ) && (tmppass)) { 
	    if (verbose) cout << " run " << irun << " passes trigger IsoMu24" << endl; 
	    *trigOKIsoMu24_ = true;
	  }
	}
	
	if(( tmptrig == hltNameIsoMu24Eta2p1_ ) && (tmppass)) { 
	  if (verbose)cout << " run " << irun << " passes trigger IsoMu24Eta2p1" << endl; 
	  *trigOKIsoMu24Eta2p1_ = true;
	} else {
	  if(( tmptrig2 == hltNameIsoMu24Eta2p1_ ) && (tmppass)) { 
	    if (verbose) cout << " run " << irun << " passes trigger IsoMu24Eta2p1" << endl; 
	    *trigOKIsoMu24Eta2p1_ = true;
	  }
	}


    }
    
  }

  iEvent.put( trigOKIsoMu17_, "passIsoMu17" );
  iEvent.put( trigOKIsoMu24_, "passIsoMu24" );
  iEvent.put( trigOKIsoMu24Eta2p1_, "passIsoMu24Eta2p1" );

}

//define this as a plug-in
DEFINE_FWK_MODULE(SingleTopPassTriggerInfoProducer);
