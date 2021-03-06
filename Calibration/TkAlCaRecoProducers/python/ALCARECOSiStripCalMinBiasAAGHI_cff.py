import FWCore.ParameterSet.Config as cms

# Set the HLT paths
import HLTrigger.HLTfilters.hltHighLevel_cfi
ALCARECOSiStripCalMinBiasAAGHLT = HLTrigger.HLTfilters.hltHighLevel_cfi.hltHighLevel.clone(
    andOr = True, ## choose logical OR between Triggerbits
##     HLTPaths = [
##     #Minimum Bias
##     "HLT_MinBias*"
##     ],
    # We want to change this key to SiStripCalMinBiasAAGHI --> update triggerbits first
    eventSetupPathsKey = 'SiStripCalMinBiasAAGHI',
    throw = False # tolerate triggers stated above, but not available
    )

# Select only events where tracker had HV on (according to DCS bit information)
# AND respective partition is in the run (according to FED information)
import CalibTracker.SiStripCommon.SiStripDCSFilter_cfi
DCSStatusForSiStripCalMinBiasAAG = CalibTracker.SiStripCommon.SiStripDCSFilter_cfi.siStripDCSFilter.clone()

# Select pp-like events based on the pixel cluster multiplicity
#import HLTrigger.special.hltPixelActivityFilter_cfi
#HLTPixelActivityFilterForSiStripCalMinBias = HLTrigger.special.hltPixelActivityFilter_cfi.hltPixelActivityFilter.clone()
#HLTPixelActivityFilterForSiStripCalMinBias.maxClusters = 500
#HLTPixelActivityFilterForSiStripCalMinBias.inputTag    = 'siPixelClusters'

# Select only good tracks
import Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi
ALCARECOSiStripCalMinBiasAAG = Alignment.CommonAlignmentProducer.AlignmentTrackSelector_cfi.AlignmentTrackSelector.clone()

ALCARECOSiStripCalMinBiasAAG.filter         = True    ##do not store empty events	
ALCARECOSiStripCalMinBiasAAG.src            = 'hiGeneralTracks'
ALCARECOSiStripCalMinBiasAAG.applyBasicCuts = True
ALCARECOSiStripCalMinBiasAAG.ptMin          = 0.8     ##GeV
ALCARECOSiStripCalMinBiasAAG.nHitMin        = 6       ## at least 6 hits required
ALCARECOSiStripCalMinBiasAAG.chi2nMax       = 10.

ALCARECOSiStripCalMinBiasAAG.GlobalSelector.applyIsolationtest    = False
ALCARECOSiStripCalMinBiasAAG.GlobalSelector.applyGlobalMuonFilter = False
ALCARECOSiStripCalMinBiasAAG.GlobalSelector.applyJetCountFilter   = False

ALCARECOSiStripCalMinBiasAAG.TwoBodyDecaySelector.applyMassrangeFilter    = False
ALCARECOSiStripCalMinBiasAAG.TwoBodyDecaySelector.applyChargeFilter       = False
ALCARECOSiStripCalMinBiasAAG.TwoBodyDecaySelector.applyAcoplanarityFilter = False
ALCARECOSiStripCalMinBiasAAG.TwoBodyDecaySelector.applyMissingETFilter    = False

# Sequence with the filter for the Pixel activity #
#seqALCARECOSiStripCalMinBias = cms.Sequence(ALCARECOSiStripCalMinBiasHLT*HLTPixelActivityFilterForSiStripCalMinBias*DCSStatusForSiStripCalMinBias*ALCARECOSiStripCalMinBias)

seqALCARECOSiStripCalMinBiasAAG = cms.Sequence(ALCARECOSiStripCalMinBiasAAGHLT *
                                                         DCSStatusForSiStripCalMinBiasAAG *
                                                         ALCARECOSiStripCalMinBiasAAG)
