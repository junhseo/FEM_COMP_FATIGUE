# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2022.HF2 replay file
# Internal Version: 2022_03_21-08.37.34 176360
# Run by jhseo on Thu Sep 29 15:52:28 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=164.57292175293, 
    height=211.140014648438)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('GOODMAN_TESTING.cae')
#: The model database "D:\00_FATIGUE\01_EXAMPLE_1\GOODMAN_TESTING.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['SPECIMEN']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
del mdb.jobs['Job-1']
del mdb.jobs['Job-2']
del mdb.jobs['Job-3']
mdb.Job(name='GOODMAN_MODEL', model='Model-1_NLGEOM', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=4, numDomains=4, numGPUs=0)
mdb.jobs['GOODMAN_MODEL'].submit(consistencyChecking=OFF)
#: The job input file "GOODMAN_MODEL.inp" has been submitted for analysis.
#: Job GOODMAN_MODEL: Analysis Input File Processor completed successfully.
#: Job GOODMAN_MODEL: Abaqus/Standard completed successfully.
#: Job GOODMAN_MODEL completed successfully. 
o3 = session.openOdb(name='D:/00_FATIGUE/01_EXAMPLE_1/GOODMAN_MODEL.odb')
#: Model: D:/00_FATIGUE/01_EXAMPLE_1/GOODMAN_MODEL.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          6
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=364.819, 
    farPlane=593.213, width=385.518, height=182.385, viewOffsetX=12.0555, 
    viewOffsetY=-1.04177)
session.Viewport(name='Viewport: 2', origin=(6.47499990463257, 
    7.5600004196167), width=379.596862792969, height=197.100006103516)
session.viewports['Viewport: 2'].makeCurrent()
session.viewports['Viewport: 2'].maximize()
session.viewports['Viewport: 1'].restore()
session.viewports['Viewport: 2'].restore()
session.viewports['Viewport: 1'].setValues(origin=(0.0, 7.56001281738281), 
    width=215.023956298828, height=203.580001831055)
session.viewports['Viewport: 2'].setValues(origin=(215.023956298828, 
    7.56001281738281), width=215.023956298828, height=203.580001831055)
o1 = session.openOdb(
    name='D:/00_FATIGUE/01_EXAMPLE_1/GOODMAN_MODE_FATIGUE.odb')
session.viewports['Viewport: 2'].setValues(displayedObject=o1)
#: Model: D:/00_FATIGUE/01_EXAMPLE_1/GOODMAN_MODE_FATIGUE.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       5
#: Number of Node Sets:          6
#: Number of Steps:              2
session.viewports['Viewport: 2'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session. linkedViewportCommands.setValues(linkViewports=True)
session.viewports['Viewport: 2'].view.setValues(session.views['Iso'])
session. linkedViewportCommands.setValues(linkViewports=False)
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')
cliCommand("""10**4.052""")
#: 11271.9745617551
session.Viewport(name='Viewport: 3', origin=(12.9499998092651, 
    7.5600004196167), width=402.529174804688, height=190.620010375977)
session.viewports['Viewport: 3'].makeCurrent()
session.viewports['Viewport: 1'].setValues(origin=(0.0, 7.56001281738281), 
    width=151.08332824707)
session.viewports['Viewport: 2'].setValues(origin=(151.08332824707, 
    7.56001281738281), width=151.08332824707)
session.viewports['Viewport: 3'].setValues(origin=(302.166656494141, 
    7.56001281738281), width=151.08332824707, height=203.580001831055)
session.viewports['Viewport: 2'].makeCurrent()
odb = session.odbs['D:/00_FATIGUE/01_EXAMPLE_1/GOODMAN_MODEL.odb']
session.viewports['Viewport: 2'].setValues(displayedObject=odb)
session.viewports['Viewport: 2'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 2'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='STATIC')
