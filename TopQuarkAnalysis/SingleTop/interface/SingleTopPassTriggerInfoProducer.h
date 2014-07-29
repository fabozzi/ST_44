#ifndef __SINGLETOPPASSTRIGGERINFOPRODUCER_H__
#define __SINGLETOPPASSTRIGGERINFOPRODUCER_H__

/* \Class SingleTopAnalyzer
 *
 * \Authors M.Merola, A. Orso M. Iorio
 * 
 * \ version $Id: SingleTopTriggers.h,v 1.2.2.2 2011/09/20 13:36:20 oiorio Exp $
 */


//----------------- system include files
#include <memory>
#include <iostream>
#include <list>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>

//----------------- cmssw includes

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/TriggerEvent.h"
#include "DataFormats/PatCandidates/interface/TriggerPath.h"

#include <FWCore/Framework/interface/Run.h>

#include "FWCore/Framework/interface/MakerMacros.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Framework/interface/TriggerNamesService.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

using namespace std;
using namespace edm;
using namespace reco;

class SingleTopPassTriggerInfoProducer : public edm::EDProducer {
 public:
  SingleTopPassTriggerInfoProducer(const edm::ParameterSet & iConfig);
  ~SingleTopPassTriggerInfoProducer();

 private:
  void produce(edm::Event & iEvent, const edm::EventSetup & iSetup);
  
  // names of HLT algorithms
  string hltNameIsoMu17_ ;
  string hltNameIsoMu24_ ;
  string hltNameIsoMu24Eta2p1_ ;

  std::vector<std::string>  hlNames_;  // name of each HLT algorithm
  edm::InputTag hlTriggerResults_;
  bool init_;
  
  bool verbose;
    
 };

#endif
