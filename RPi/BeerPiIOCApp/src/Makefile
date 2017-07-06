TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = BeerPiIOC
# BeerPiIOC.dbd will be created and installed
DBD += BeerPiIOC.dbd

# BeerPiIOC.dbd will be made up from these files:
BeerPiIOC_DBD += base.dbd
BeerPiIOC_DBD += asyn.dbd
BeerPiIOC_DBD += stream.dbd
BeerPiIOC_DBD += drvAsynIPPort.dbd
BeerPiIOC_DBD += drvAsynSerialPort.dbd

# Include dbd files from all support applications:
#BeerPiIOC_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#BeerPiIOC_LIBS += xxx
BeerPiIOC_LIBS += asyn
BeerPiIOC_LIBS += stream

# BeerPiIOC_registerRecordDeviceDriver.cpp derives from BeerPiIOC.dbd
BeerPiIOC_SRCS += BeerPiIOC_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
BeerPiIOC_SRCS_DEFAULT += BeerPiIOCMain.cpp
BeerPiIOC_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#BeerPiIOC_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
BeerPiIOC_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

