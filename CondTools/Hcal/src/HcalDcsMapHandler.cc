#include "CondTools/Hcal/interface/HcalDcsMapHandler.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/HcalDetId/interface/HcalGenericDetId.h"
#include <memory>

HcalDcsMapHandler::HcalDcsMapHandler(edm::ParameterSet const& ps) {
  m_name = ps.getUntrackedParameter<std::string>("name", "HcalDcsMapHandler");
  sinceTime = ps.getUntrackedParameter<unsigned>("IOVRun", 0);
}

HcalDcsMapHandler::~HcalDcsMapHandler() {}

void HcalDcsMapHandler::getNewObjects() {
  //  edm::LogInfo   ("HcalDcsMapHandler")
  std::cout << "------- " << m_name << " - > getNewObjects\n"
            <<
      //check whats already inside of database
      "got offlineInfo" << tagInfo().name << ", size " << tagInfo().size << ", last object valid since "
            << tagInfo().lastInterval.since << std::endl;

  if (!myDBObject)
    throw cms::Exception("Empty DB object")
        << m_name << " has received empty object - nothing to write to DB" << std::endl;

  //  IOV information
  cond::Time_t myTime = sinceTime;

  std::cout << "Using IOV run " << sinceTime << std::endl;

  // prepare for transfer:
  m_to_transfer.push_back(std::make_pair(myDBObject, myTime));

  edm::LogInfo("HcalDcsMapHandler") << "------- " << m_name << " - > getNewObjects" << std::endl;
}

void HcalDcsMapHandler::initObject(HcalDcsMap* fObject) { myDBObject = fObject; }
