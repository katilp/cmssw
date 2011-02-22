# /dev/CMSSW_3_11_1/GRun/V39

import FWCore.ParameterSet.Config as cms

# dump of the Stream A Datasets defined in the HLT table

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetCommissioning_selector
streamA_datasetCommissioning_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetCommissioning_selector.l1tResults = cms.InputTag('')
streamA_datasetCommissioning_selector.throw      = cms.bool(False)
streamA_datasetCommissioning_selector.triggerConditions = cms.vstring('HLT_BTagMu_DiJet20_Mu5_v1', 
    'HLT_BTagMu_DiJet60_Mu7_v1', 
    'HLT_BTagMu_DiJet80_Mu9_v1', 
    'HLT_BeamGas_BSC_v1', 
    'HLT_BeamGas_HF_v1', 
    'HLT_CentralJet80_MET100_v1', 
    'HLT_CentralJet80_MET160_v1', 
    'HLT_CentralJet80_MET65_v1', 
    'HLT_CentralJet80_MET80_v1', 
    'HLT_DiJet100_PT100_v1', 
    'HLT_DiJet130_PT130_v1', 
    'HLT_DiJet60_MET45_v1', 
    'HLT_DiJet70_PT70_v1', 
    'HLT_DiJetAve100U_v4', 
    'HLT_DiJetAve140U_v4', 
    'HLT_DiJetAve15U_v4', 
    'HLT_DiJetAve180U_v4', 
    'HLT_DiJetAve300U_v4', 
    'HLT_DiJetAve30U_v4', 
    'HLT_DiJetAve50U_v4', 
    'HLT_DiJetAve70U_v4', 
    'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v1', 
    'HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v1', 
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v1', 
    'HLT_DoubleIsoPFTau20_Trk5_v1', 
    'HLT_DoubleJet30_ForwardBackward_v1', 
    'HLT_DoubleJet60_ForwardBackward_v1', 
    'HLT_DoubleJet70_ForwardBackward_v1', 
    'HLT_DoubleJet80_ForwardBackward_v1', 
    'HLT_DoubleMu3_Bs_v1', 
    'HLT_DoubleMu3_HT160_v1', 
    'HLT_DoubleMu3_HT200_v1', 
    'HLT_DoubleMu3_Jpsi_v1', 
    'HLT_DoubleMu3_Quarkonium_v1', 
    'HLT_DoubleMu3_v3', 
    'HLT_DoubleMu4_Acoplanarity03_v1', 
    'HLT_DoubleMu5_Ele8_CaloIdL_TrkIdVL_v1', 
    'HLT_DoubleMu5_Ele8_v1', 
    'HLT_DoubleMu6_v1', 
    'HLT_DoubleMu7_v1', 
    'HLT_DoublePhoton32_CaloIdL_v1', 
    'HLT_DoublePhoton5_IsoVL_CEP_v1', 
    'HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v1', 
    'HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v1', 
    'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1', 
    'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1', 
    'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1', 
    'HLT_Ele15_CaloIdVT_TrkIdT_LooseIsoPFTau15_v1', 
    'HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v1', 
    'HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1', 
    'HLT_Ele17_CaloIdL_CaloIsoVL_v1', 
    'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v1', 
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralDiJet30_v1', 
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralJet30_v1', 
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralJet40_BTagIP_v1', 
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralTriJet30_v1', 
    'HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1', 
    'HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1', 
    'HLT_Ele45_CaloIdVT_TrkIdT_v1', 
    'HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v1', 
    'HLT_Ele8_CaloIdL_CaloIsoVL_v1', 
    'HLT_Ele8_CaloIdL_TrkIdVL_v1', 
    'HLT_Ele8_v1', 
    'HLT_Ele90_NoSpikeFilter_v1', 
    'HLT_ExclDiJet60_HFAND_v1', 
    'HLT_ExclDiJet60_HFOR_v1', 
    'HLT_HT160_v1', 
    'HLT_HT240_v1', 
    'HLT_HT260_MHT60_v1', 
    'HLT_HT300_MHT75_v1', 
    'HLT_HT300_v1', 
    'HLT_HT360_v1', 
    'HLT_HT440_v1', 
    'HLT_HT520_v1', 
    'HLT_IsoMu12_LooseIsoPFTau10_v1', 
    'HLT_IsoMu12_v1', 
    'HLT_IsoMu15_v5', 
    'HLT_IsoMu17_CentralJet40_BTagIP_v1', 
    'HLT_IsoMu17_v5', 
    'HLT_IsoMu30_v1', 
    'HLT_IsoMu5_DoubleMu5_v1', 
    'HLT_IsoPFTau35_Trk20_MET45_v1', 
    'HLT_IsoTrackHB_v2', 
    'HLT_IsoTrackHE_v3', 
    'HLT_Jet110_v1', 
    'HLT_Jet150_v1', 
    'HLT_Jet190_v1', 
    'HLT_Jet240_v1', 
    'HLT_Jet30_v1', 
    'HLT_Jet370_NoJetID_v1', 
    'HLT_Jet370_v1', 
    'HLT_Jet60_v1', 
    'HLT_Jet80_v1', 
    'HLT_L1DoubleMu0_v1', 
    'HLT_L1SingleMu10_v1', 
    'HLT_L1SingleMu20_v1', 
    'HLT_L1SingleMuOpen_v1', 
    'HLT_L1Tech_BSC_minBias_OR_v1', 
    'HLT_L1_BeamHalo_v1', 
    'HLT_L1_Interbunch_BSC_v1', 
    'HLT_L1_PreCollisions_v1', 
    'HLT_L2DoubleMu0_v2', 
    'HLT_L2DoubleMu35_NoVertex_v1', 
    'HLT_L2Mu10_v1', 
    'HLT_L2Mu20_v1', 
    'HLT_MET100_v1', 
    'HLT_MET120_v1', 
    'HLT_MET200_v1', 
    'HLT_MR100_v1', 
    'HLT_Meff440_v1', 
    'HLT_Meff520_v1', 
    'HLT_Meff640_v1', 
    'HLT_Mu10_Ele10_CaloIdL_v1', 
    'HLT_Mu12_v1', 
    'HLT_Mu15_DoublePhoton15_CaloIdL_v1', 
    'HLT_Mu15_LooseIsoPFTau20_v1', 
    'HLT_Mu15_Photon20_CaloIdL_v1', 
    'HLT_Mu15_v2', 
    'HLT_Mu17_CentralJet30_v1', 
    'HLT_Mu17_CentralJet40_BTagIP_v1', 
    'HLT_Mu17_DiCentralJet30_v1', 
    'HLT_Mu17_Ele8_CaloIdL_v1', 
    'HLT_Mu17_TriCentralJet30_v1', 
    'HLT_Mu17_v2', 
    'HLT_Mu20_v1', 
    'HLT_Mu24_v1', 
    'HLT_Mu30_v1', 
    'HLT_Mu3_Ele8_CaloIdL_TrkIdVL_HT160_v1', 
    'HLT_Mu3_Ele8_CaloIdT_TrkIdVL_HT160_v1', 
    'HLT_Mu3_Track3_Jpsi_v4', 
    'HLT_Mu3_v2', 
    'HLT_Mu5_DoubleEle8_v1', 
    'HLT_Mu5_Ele8_CaloIdL_TrkIdVL_Ele8_v1', 
    'HLT_Mu5_HT200_v1', 
    'HLT_Mu5_L2Mu2_Jpsi_v1', 
    'HLT_Mu5_L2Mu2_v1', 
    'HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1', 
    'HLT_Mu5_Track0_Jpsi_B5Q7_v1', 
    'HLT_Mu5_Track5_Jpsi_v1', 
    'HLT_Mu5_v2', 
    'HLT_Mu7_Track5_Jpsi_v1', 
    'HLT_Mu7_Track7_Jpsi_v1', 
    'HLT_Mu8_Ele17_CaloIdL_v1', 
    'HLT_Mu8_HT200_v1', 
    'HLT_Mu8_Jet40_v1', 
    'HLT_Mu8_Photon20_CaloIdVT_IsoT_v1', 
    'HLT_Mu8_v1', 
    'HLT_PFMHT150_v1', 
    'HLT_PFMHT80_v1', 
    'HLT_Photon125_NoSpikeFilter_v1', 
    'HLT_Photon20_CaloIdVT_IsoT_Ele8_CaloIdL_CaloIsoVL_v1', 
    'HLT_Photon20_R9Id_Photon18_R9Id_v1', 
    'HLT_Photon26_CaloIdL_IsoVL_Photon18_CaloIdL_IsoVL_v1', 
    'HLT_Photon26_CaloIdL_IsoVL_Photon18_v1', 
    'HLT_Photon26_IsoL_Photon18_v1', 
    'HLT_Photon26_IsoVL_Photon18_IsoVL_v1', 
    'HLT_Photon26_IsoVL_Photon18_v1', 
    'HLT_Photon26_Photon18_v1', 
    'HLT_Photon30_CaloIdVL_IsoL_v1', 
    'HLT_Photon30_CaloIdVL_v1', 
    'HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1', 
    'HLT_Photon75_CaloIdVL_IsoL_v1', 
    'HLT_Photon75_CaloIdVL_v1', 
    'HLT_Physics_v1', 
    'HLT_PixelTracks_Multiplicity110_v1', 
    'HLT_PixelTracks_Multiplicity125_v1', 
    'HLT_QuadJet20_IsoPFTau20_PFMHT30_v1', 
    'HLT_QuadJet40_IsoPFTau40_v1', 
    'HLT_QuadJet40_v1', 
    'HLT_QuadJet50_BTagIP_v1', 
    'HLT_QuadJet50_Jet40_v1', 
    'HLT_QuadJet60_v1', 
    'HLT_QuadJet65_v1', 
    'HLT_QuadJet70_v1', 
    'HLT_R032_MR100_v1', 
    'HLT_R032_v1', 
    'HLT_R035_MR100_v1', 
    'HLT_Random_v1', 
    'HLT_TripleEle10_CaloIdL_TrkIdVL_v1', 
    'HLT_TripleMu5_v1', 
    'HLT_ZeroBias_v1')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetCosmics_selector
streamA_datasetCosmics_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetCosmics_selector.l1tResults = cms.InputTag('')
streamA_datasetCosmics_selector.throw      = cms.bool(False)
streamA_datasetCosmics_selector.triggerConditions = cms.vstring('HLT_L1MuOpen_AntiBPTX_v2', 
    'HLT_L1Tech_BSC_halo_v1', 
    'HLT_L1TrackerCosmics_v2', 
    'HLT_L2MuOpen_NoVertex_v1', 
    'HLT_L3MuonsCosmicTracking_v1', 
    'HLT_RegionalCosmicTracking_v1')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetHcalHPDNoise_selector
streamA_datasetHcalHPDNoise_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetHcalHPDNoise_selector.l1tResults = cms.InputTag('')
streamA_datasetHcalHPDNoise_selector.throw      = cms.bool(False)
streamA_datasetHcalHPDNoise_selector.triggerConditions = cms.vstring('HLT_GlobalRunHPDNoise_v2', 
    'HLT_L1Tech_HBHEHO_totalOR_v1')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetHcalNZS_selector
streamA_datasetHcalNZS_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetHcalNZS_selector.l1tResults = cms.InputTag('')
streamA_datasetHcalNZS_selector.throw      = cms.bool(False)
streamA_datasetHcalNZS_selector.triggerConditions = cms.vstring('HLT_HcalNZS_v2', 
    'HLT_HcalPhiSym_v2')

