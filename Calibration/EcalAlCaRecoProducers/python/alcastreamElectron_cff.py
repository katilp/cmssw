import FWCore.ParameterSet.Config as cms

#
#  run on collection of electrons to make a collection of AlCaReco electrons 
#  and store them in the output collection
#
# hybrid clustering in the barrel
from RecoEcal.EgammaClusterProducers.hybridClusteringSequence_cff import *
# island clustering for the endcaps
from RecoEcal.EgammaClusterProducers.islandClusteringSequence_cff import *
from Geometry.CaloEventSetup.CaloGeometry_cfi import *
# sequence to make si-strip based electrons
from Calibration.EcalAlCaRecoProducers.alCaIsolatedElectrons_cfi import *
electronFilter = cms.EDFilter("EtaPtMinGsfElectronFullCloneSelector",
    filter = cms.bool(True),
    src = cms.InputTag("gedGsfElectrons"),
    etaMin = cms.double(-2.7),
    etaMax = cms.double(2.7),
    ptMin = cms.double(5.0)
)

seqAlcastreamElectron = cms.Sequence(electronFilter*alCaIsolatedElectrons)

