import FWCore.ParameterSet.Config as cms
from CondCore.DBCommon.CondDBSetup_cfi import *

#### Please fill with comments
# 
# combination of PhiSym + PiZero + Ele 2012 with also 2010-2011 using
# the weighted average of the errors estimated with the differential smearing
# on top of RUN2012C prompt GT
#

RerecoGlobalTag = cms.ESSource("PoolDBESSource",
                               CondDBSetup,
                               connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG'),
                               globaltag = cms.string('GR_P_V42B::All'),
                               toGet = cms.VPSet(
    cms.PSet(record = cms.string("EcalIntercalibConstantsRcd"),
             tag = cms.string('EcalIntercalibConstants_V20121025_2011_2012CombWithDSMethodErrors'),
             connect = cms.untracked.string("frontier://FrontierInt/CMS_COND_ECAL")
              )
    ),
                               BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService')
                               )

