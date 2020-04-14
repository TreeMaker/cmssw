import FWCore.ParameterSet.Config as cms

from RecoBTag.FeatureTools.pfDeepBoostedJetTagInfos_cfi import pfDeepBoostedJetTagInfos
from RecoBTag.MXNet.pfDeepBoostedJetTags_cfi import pfDeepBoostedJetTags as _pfDeepBoostedJetTags
from RecoBTag.MXNet.pfDeepBoostedDiscriminatorsJetTags_cfi import pfDeepBoostedDiscriminatorsJetTags
from RecoBTag.MXNet.pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags_cfi import pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags
from RecoBTag.MXNet.Parameters.V02.pfDeepBoostedJetPreprocessParams_cfi import pfDeepBoostedJetPreprocessParams as pfDeepBoostedJetPreprocessParamsV02
from RecoBTag.MXNet.Parameters.V02.pfMassDecorrelatedDeepBoostedJetPreprocessParams_cfi import pfMassDecorrelatedDeepBoostedJetPreprocessParams as pfMassDecorrelatedDeepBoostedJetPreprocessParamsV02

# nominal DeepAK8
pfDeepBoostedJetTags = _pfDeepBoostedJetTags.clone(
    preprocessParams = pfDeepBoostedJetPreprocessParamsV02,
    model_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/full/resnet-symbol.json',
    param_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/full/resnet-0000.params',
    debugMode  = False, # debug
)

# mass-decorrelated DeepAK8
pfMassDecorrelatedDeepBoostedJetTags = _pfDeepBoostedJetTags.clone(
    preprocessParams = pfMassDecorrelatedDeepBoostedJetPreprocessParamsV02,
    model_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/decorrelated/resnet-symbol.json',
    param_path = 'RecoBTag/Combined/data/DeepBoostedJet/V02/decorrelated/resnet-0000.params',
    debugMode = False, # debug
)

from CommonTools.PileupAlgos.Puppi_cff import puppi
from PhysicsTools.PatAlgos.slimming.primaryVertexAssociation_cfi import primaryVertexAssociation

# This task is not used, useful only if we run DeepFlavour from RECO
# jets (RECO/AOD)
pfDeepBoostedJetTask = cms.Task(puppi, primaryVertexAssociation,
                             pfDeepBoostedJetTagInfos, pfDeepBoostedJetTags, pfMassDecorrelatedDeepBoostedJetTags,
                             pfDeepBoostedDiscriminatorsJetTags, pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags)

# declare all the discriminators
# nominal: probs
_pfDeepBoostedJetTagsProbs = ['pfDeepBoostedJetTags:' + flav_name
                              for flav_name in pfDeepBoostedJetTags.flav_names]
# nominal: meta-taggers
_pfDeepBoostedJetTagsMetaDiscrs = ['pfDeepBoostedDiscriminatorsJetTags:' + disc.name.value()
                                   for disc in pfDeepBoostedDiscriminatorsJetTags.discriminators]

# mass-decorrelated: probs
_pfMassDecorrelatedDeepBoostedJetTagsProbs = ['pfMassDecorrelatedDeepBoostedJetTags:' + flav_name
                                              for flav_name in pfMassDecorrelatedDeepBoostedJetTags.flav_names]
# mass-decorrelated: meta-taggers
_pfMassDecorrelatedDeepBoostedJetTagsMetaDiscrs = ['pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:' + disc.name.value()
                                   for disc in pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags.discriminators]

_pfDeepBoostedJetTagsAll = _pfDeepBoostedJetTagsProbs + _pfDeepBoostedJetTagsMetaDiscrs + \
    _pfMassDecorrelatedDeepBoostedJetTagsProbs + _pfMassDecorrelatedDeepBoostedJetTagsMetaDiscrs
