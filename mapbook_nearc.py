#Author:  Melissa Albino Hegeman, melissa.hegeman@gmail.com
#Date:		June 2016
#Purpose: 	The purpose of this project is to use the shapefiles resulting
#             from the Tidal Wetlands trends project to produce a series of maps
#             showing the before and after tidal wetlands on DEC properties
#             with the associated acreage.

def updateHeader(template, mapName, townName, embaymentName):
     #Update the title placement and content
    template.title = mapName
    newName = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "name")[0]
    newName.elementPositionX, newName.elementPositionY = 0.25, 10.75+3
    #make sure title fits on page
    if newName.elementWidth > 8:
        newName.elementWidth = 8
    #update the town and embayment
    town = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "town")[0]
    town.text = "Town: " + townName
    town.elementPositionX, town.elementPositionY = 0.25, 10.25+3
    if town.elementWidth > 6:
        town.elementWidth = 6
    
    embayment = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "embayment")[0]
    embayment.text = "Embayment: " + embaymentName
    embayment.elementPositionX, embayment.elementPositionY = 0.25, 10+3
    if embayment.elementWidth > 6:
        embayment.elementWidth = 6 
    else: pass
    
def summaryTable(selectedWetlands, selectedDECtidalwetlands, sumField, caseField, strYear):
    #select only tw in the designated property
    arcpy.SelectLayerByLocation_management(selectedWetlands, "INTERSECT", selectedDECtidalwetlands)
    #remove spaces from map name
    tableName = mapName.replace(" ","")
    outputTable = tableName + "summaryTable" + strYear
    arcpy.Statistics_analysis(selectedWetlands, outputTable, [[sumField,"SUM"]], caseField)
    wetlandsTable = arcpy.mapping.TableView(outputTable)
    return wetlandsTable
    
def lineUp(input1,output1):
    output1.elementPositionY = input1.elementPositionY
    
def lineUpEverything(input2,out1,out2,out3,out4):
    lineUp(input2,out1)
    lineUp(input2,out2)
    lineUp(input2,out3)
    lineUp(input2,out4)

def centerColumns():
    fm1974.elementPositionX = xPosMiddleCol
    hm1974.elementPositionX = xPosMiddleCol
    im1974.elementPositionX = xPosMiddleCol
    panne1974.elementPositionX = xPosMiddleCol
    panne1974.elementPositionX = xPosMiddleCol
    unv1974.elementPositionX = xPosMiddleCol
    up1974.elementPositionX = xPosMiddleCol
    
    fm2008.elementPositionX = xPosRightCol
    hm2008.elementPositionX = xPosRightCol
    im2008.elementPositionX = xPosRightCol
    panne2008.elementPositionX = xPosRightCol
    phrag2008.elementPositionX = xPosRightCol
    unv2008.elementPositionX = xPosRightCol
    up2008.elementPositionX = xPosRightCol
    
    fmAcres.elementPositionX = xPosDiffAcres
    hmAcres.elementPositionX = xPosDiffAcres
    imAcres.elementPositionX = xPosDiffAcres
    panneAcres.elementPositionX = xPosDiffAcres
    phragAcres.elementPositionX = xPosDiffAcres
    unvAcres.elementPositionX = xPosDiffAcres
    upAcres.elementPositionX = xPosDiffAcres
    
    fmPerc.elementPositionX = xPosDiffPerc
    hmPerc.elementPositionX = xPosDiffPerc
    imPerc.elementPositionX = xPosDiffPerc
    pannePerc.elementPositionX = xPosDiffPerc
    phragPerc.elementPositionX = xPosDiffPerc
    unvPerc.elementPositionX = xPosDiffPerc
    upPerc.elementPositionX = xPosDiffPerc
    
def setToZero():
    #set everything to 0
    fm1974.text, fm1974.elementPositionX = "0", xPosMiddleCol
    hm1974.text, hm1974.elementPositionX = "0", xPosMiddleCol
    im1974.text, im1974.elementPositionX = "0", xPosMiddleCol
    panne1974.text, panne1974.elementPositionX = "not measured", xPosMiddleCol
    phrag1974.text, phrag1974.elementPositionX = "0", xPosMiddleCol
    unv1974.text, unv1974.elementPositionX = "not measured", xPosMiddleCol
    up1974.text, up1974.elementPositionX = "not measured", xPosMiddleCol
    
    fm2008.text, fm2008.elementPositionX = "0", xPosRightCol
    hm2008.text, hm2008.elementPositionX = "0", xPosRightCol
    im2008.text, im2008.elementPositionX = "0", xPosRightCol
    panne2008.text, panne2008.elementPositionX = "0", xPosRightCol
    phrag2008.text, phrag2008.elementPositionX = "0", xPosRightCol
    unv2008.text, unv2008.elementPositionX = "0", xPosRightCol
    up2008.text, up2008.elementPositionX = "0", xPosRightCol
    
    fmAcres.text, fmAcres.elementPositionX = "0",xPosDiffAcres
    hmAcres.text,hmAcres.elementPositionX = "0",xPosDiffAcres
    imAcres.text,imAcres.elementPositionX = "0",xPosDiffAcres
    panneAcres.text,panneAcres.elementPositionX = "na",xPosDiffAcres
    phragAcres.text, phragAcres.elementPositionX = "0",xPosDiffAcres
    unvAcres.text,unvAcres.elementPositionX = "na",xPosDiffAcres
    upAcres.text,upAcres.elementPositionX = "na",xPosDiffAcres
    
    fmPerc.text,fmPerc.elementPositionX = "0",xPosDiffPerc
    hmPerc.text,hmPerc.elementPositionX = "0",xPosDiffPerc
    imPerc.text,imPerc.elementPositionX = "0",xPosDiffPerc
    pannePerc.text,pannePerc.elementPositionX = "na",xPosDiffPerc
    phragPerc.text,phragPerc.elementPositionX = "0",xPosDiffPerc
    unvPerc.text,unvPerc.elementPositionX = "na",xPosDiffPerc
    upPerc.text,upPerc.elementPositionX = "na",xPosDiffPerc
    
    lineUpEverything(freshMarsh,fm1974,fm2008,fmAcres,fmPerc)
    lineUpEverything(highMarsh,hm1974,hm2008,hmAcres,hmPerc)
    lineUpEverything(intertidalMarsh,im1974,im2008,imAcres,imPerc)
    lineUpEverything(panne,panne1974,panne2008,panneAcres,pannePerc)
    lineUpEverything(phrag,phrag1974,phrag2008,phragAcres,phragPerc)
    lineUpEverything(unveg,unv1974,unv2008,unvAcres,unvPerc)
    lineUpEverything(upland,up1974,up2008,upAcres,upPerc)
    
def calculateDifference():
    fmAcres.text = str(float(fm2008.text) - float(fm1974.text))
    hmAcres.text = str(float(hm2008.text) - float(hm1974.text))
    imAcres.text = str(float(im2008.text) - float(im1974.text))
    phragAcres.text = str(float(phrag2008.text) - float(phrag1974.text))
    
    if float(fm1974.text)>0:
        percent1 = (float(fmAcres.text)/float(fm1974.text))*100
        fmPerc.text = str("%.2f" % percent1)
    if float(hm1974.text)>0:
        percent2 = (float(hmAcres.text)/float(hm1974.text))
        hmPerc.text = str("%.2f" % percent2)
    if float(im1974.text)>0:
        percent3 = (float(imAcres.text)/float(im1974.text))*100
        imPerc.text = str("%.2f" % percent3)
    if float(phrag1974.text)>0:
        percent4 = (float(phragAcres.text)/float(phrag1974.text))*100
        phragPerc.text = str("%.2f" % percent4)
    
###

import arcpy

arcpy.env.overwriteOutput = True

#Set the workspace
arcpy.env.workspace = r"C:\Users\maalbino\Documents\GIS\mapbooks\mapbook.gdb"
arcpy.env.scratchWorkspace = r"C:\Users\maalbino\Documents\GIS\mapbooks\mapbook.gdb"
mapLocation = r"C:\Users\maalbino\Documents\GIS\mapbooks\mapstest"

#define the template .mxd
#which mxd is your template?
mapdoc = r"C:\Users\maalbino\Documents\GIS\TW_trends\example4.mxd"
template = arcpy.mapping.MapDocument(mapdoc)

#define the dataframes
dfBefore = arcpy.mapping.ListDataFrames(template, "1974")[0]
dfAfter = arcpy.mapping.ListDataFrames(template, "2008")[0]

#define category text elements
category = arcpy.mapping.ListLayoutElements(template,"TEXT_ELEMENT", "CategoryText")[0]
acreage1974 = arcpy.mapping.ListLayoutElements(template,"TEXT_ELEMENT", "1974Acreage")[0]
acreage2008 = arcpy.mapping.ListLayoutElements(template,"TEXT_ELEMENT", "2008Acreage")[0]
differenceAcres = arcpy.mapping.ListLayoutElements(template,"TEXT_ELEMENT", "DiffAcres")[0]
differencePercent = arcpy.mapping.ListLayoutElements(template,"TEXT_ELEMENT", "DiffPercent")[0]

freshMarsh = arcpy.mapping.ListLayoutElements(template,"TEXT_ELEMENT", "FreshMarshText")[0]
highMarsh = arcpy.mapping.ListLayoutElements(template,"TEXT_ELEMENT", "HighMarshText")[0]
intertidalMarsh = arcpy.mapping.ListLayoutElements(template,"TEXT_ELEMENT", "IntertidalMarshText")[0]
panne = arcpy.mapping.ListLayoutElements(template,"TEXT_ELEMENT", "PanneText")[0]
phrag = arcpy.mapping.ListLayoutElements(template,"TEXT_ELEMENT", "PhragmitesText")[0]
unveg = arcpy.mapping.ListLayoutElements(template,"TEXT_ELEMENT", "UnvegetatedText")[0]
upland = arcpy.mapping.ListLayoutElements(template,"TEXT_ELEMENT", "UplandText")[0]

xPosLeftCol = category.elementPositionX
xPosMiddleCol = acreage1974.elementPositionX
xPosRightCol = acreage2008.elementPositionX
xPosDiffAcres = differenceAcres.elementPositionX
xPosDiffPerc = differencePercent.elementPositionX

#define text elements in table
fm1974 = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "1974FM")[0]
hm1974 = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "1974HM")[0]
im1974 = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "1974IM")[0]
panne1974 = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "1974Panne")[0]
phrag1974 = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "1974Phrag")[0]
unv1974 = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "1974UnV")[0]
up1974 = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "1974Up")[0]

fm2008 = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "2008FM")[0]
hm2008 = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "2008HM")[0]
im2008 = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "2008IM")[0]
panne2008 = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "2008Panne")[0]
phrag2008 = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "2008Phrag")[0]
unv2008 = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "2008UnV")[0]
up2008 = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "2008Up")[0]

fmAcres = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "FM_Acres")[0]
hmAcres = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "HM_Acres")[0]
imAcres = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "IM_Acres")[0]
panneAcres = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "Panne_Acres")[0]
phragAcres = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "Phrag_Acres")[0]
unvAcres = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "UnV_Acres")[0]
upAcres = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "Up_Acres")[0]

fmPerc = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "FM_Per")[0]
hmPerc = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "HM_Per")[0]
imPerc = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "IM_Per")[0]
pannePerc = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "Panne_Per")[0]
phragPerc = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "Phrag_Per")[0]
unvPerc = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "UnV_Per")[0]
upPerc = arcpy.mapping.ListLayoutElements(template, "TEXT_ELEMENT", "Up_Per")[0]

setToZero()






#make tidal wetlands feature layers for 1974 and 2005/2008
try:
    arcpy.MakeFeatureLayer_management(r"data\tw20052008NAD83clip","selectedWetlands2008")
    print "feature layer a success"
except:
    print arcpy.GetMessages()
try:
    arcpy.MakeFeatureLayer_management(r"data\tw1974enhancedNAD83_clip","selectedWetlands1974")
    print "feature layer a success_2"
except:
    print arcpy.GetMessages()

#Cycle through the DEC lands, make a new map for each property
rows = arcpy.SearchCursor(r"data\DEC_tidalwetlands", "", "", "", "")
for row in rows:
    mapName = row.getValue("FACILITY")
    objectID = row.getValue("OBJECTID")
    townName = row.getValue("Town")
    embaymentName = row.getValue("Embayment")
    #make sure the name is a string, filters out the nulls
    if isinstance(mapName, unicode) == False:        
        mapName = "unnamed"+str(objectID)
    else: pass
    #print "\n" + mapName
    updateHeader(template, mapName, townName, embaymentName)
    #dec lands query statement, only show features that match the facility name
    query = " FACILITY = '" + mapName + "'" 
      
    #define layer and create definition query
    decLands74 = arcpy.mapping.ListLayers(template, "DEC_tidalwetlands", dfBefore)[0]
    decLands74.definitionQuery = query
    
    #pan to the extent of the stations layer
    dfBefore.extent = decLands74.getSelectedExtent()
    
    #match dataframes
    dfAfter.extent = dfBefore.extent
    decLands0508 = arcpy.mapping.ListLayers(template, "DEC_tidalwetlands", dfAfter)[0]
    decLands0508.definitionQuery = query
    
    #make feature layer of DEC wetlands
    arcpy.MakeFeatureLayer_management("DEC_tidalwetlands","selectedDECtidalwetlands2008", query, "", "")
    arcpy.MakeFeatureLayer_management("DEC_tidalwetlands","selectedDECtidalwetlands1974", query, "", "")
    
    #Summarize 2005/2008 wetlands
    wetlands2008Table = summaryTable("selectedWetlands2008", "selectedDECtidalwetlands2008", "Acreage", "TWL_Class", "2008")
    arcpy.mapping.AddTableView(dfAfter, wetlands2008Table)

    wetlands1974Table = summaryTable("selectedWetlands1974", "selectedDECtidalwetlands1974", "Acreage", "TWCAT74", "1974")
    arcpy.mapping.AddTableView(dfBefore, wetlands1974Table) 
        
    #print "1974 Table"
    table1974 = arcpy.da.SearchCursor(wetlands1974Table,["TWCAT74","SUM_Acreage"])
    for row in table1974:
        roundedNum1974 = "%.2f" % row[1]
        if row[0] == "FM":
            fm1974.text = str(roundedNum1974)
        elif row[0] == "HM":
            hm1974.text = str(roundedNum1974)
        elif row[0] == "IM":
            im1974.text = str(roundedNum1974)
        elif row[0] == "PH":
            phrag1974.text = str(roundedNum1974)
        #print row[0] + ", " + roundedNum1974
    
    #print "2008 Table"
    table2008 = arcpy.da.SearchCursor(wetlands2008Table,["TWL_Class","SUM_Acreage"])
    for row1 in table2008:
        roundedNum2008 = "%.2f" % row1[1]
        if row1[0] == "FreshMarsh":
            fm2008.text = str(roundedNum2008)
        elif row1[0] == "HighMarsh":
            hm2008.text = str(roundedNum2008)
        elif row1[0] == "IntertidalMarsh":
            im2008.text = str(roundedNum2008)
        elif row1[0] == "Panne/Unvegetated":
            hm2008.text = str(roundedNum2008)
        elif row1[0] == "Phragmites":
            phrag2008.text = str(roundedNum2008)
        elif row1[0] == "Unvegetated":
            unv2008.text = str(roundedNum2008)
        elif row1[0] == "Upland":
            up2008.text = str(roundedNum2008)
        #print row1[0] +", " + roundedNum2008
    
    
    calculateDifference()
    
    centerColumns()
    #make a copy of the template and name it after the facility name 
    newMap = mapLocation + "\\" + mapName + ".mxd"
    template.saveACopy(newMap)
    #remove the summary table so it doesn't appear in subsequent map documents
    arcpy.mapping.RemoveTableView(dfBefore, wetlands1974Table)
    arcpy.mapping.RemoveTableView(dfAfter, wetlands2008Table)
    setToZero()


del row, rows, template
del newMap 
del wetlands2008Table 
del wetlands1974Table


