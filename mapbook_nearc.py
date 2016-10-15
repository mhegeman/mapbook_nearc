#Author:  Melissa Albino Hegeman, melissa.hegeman@gmail.com
#Date:		June 2016
#Purpose: 	The purpose of this project is to use the shapefiles resulting
#             from the Tidal Wetlands trends project to produce a series of maps
#             showing the before and after tidal wetlands on DEC properties
#             with the associated acreage.
#%%
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
    

#lines up the columns
def centerColumns():
    col1974 = {key:value for key, value in textDict.items() if '1974' in key}
    for key in col1974:
        col1974[key].elementPositionX = xPosMiddleCol
    
    col2008 = {key:value for key, value in textDict.items() if '2008' in key}
    for key in col2008:
        col2008[key].elementPositionX = xPosRightCol
               
    colDiff = {key:value for key, value in textDict.items() if 'Acres' in key}
    for key in colDiff:
        colDiff[key].elemenyPositionX = xPosDiffAcres

    colPer = {key:value for key, value in textDict.items() if '_Per' in key}
    for key in colPer:
        colPer[key].elementPositionX = xPosDiffPerc

def lineUpRows():
    for key in colsDict:
        colsDict[key].elementPositionY = yPosHeader

    fm = {key:value for key, value in textDict.items() if 'fm' in key}
    for key in fm:
        fm[key].elementPositionY = yPosFM
    hm = {key:value for key, value in textDict.items() if 'hm' in key}
    for key in hm:
        hm[key].elementPositionY = yPosHM
    im = {key:value for key, value in textDict.items() if 'im' in key}
    for key in im:
        im[key].elementPositionY = yPosIM
    panne = {key:value for key, value in textDict.items() if 'panne' in key}
    for key in panne:
        panne[key].elementPositionY = yPosPanne
    phrag = {key:value for key, value in textDict.items() if 'phrag' in key}
    for key in phrag:
        phrag[key].elementPositionY = yPosPhrag
    unv = {key:value for key, value in textDict.items() if 'unv' in key}
    for key in unv:
        unv[key].elementPositionY = yPosUnv
    up = {key:value for key, value in textDict.items() if 'up' in key}
    for key in up:
        up[key].elementPositionY = yPosUp

          
def setToZero():
    #set everything to 0
    for key in textDict:
        if key == 'tblpanne1974' or key == 'tblunv1974' or key == 'tblup1974':
            textDict[key].text = "not measured"
    
        elif key == 'tblpanne_Acres' or key == 'tblun_Acres' or key == 'tblup_Acres':
            textDict[key].text = "NA"
        elif key == 'tblpanne_Per' or key == 'tblun_Per' or key == 'tblup_Per':
            textDict[key].text = "NA"
        else:
            textDict[key].text = 0
    centerColumns()
    lineUpRows()

    

    
def calculateDifference():
    
    textDict['tblfm_Acres'].text = str(float(textDict['tblfm2008'].text) - float(textDict['tblfm1974'].text))
    textDict['tblhm_Acres'].text = str(float(textDict['tblhm2008'].text) - float(textDict['tblhm1974'].text))
    textDict['tblim_Acres'].text = str(float(textDict['tblim2008'].text) - float(textDict['tblim1974'].text))
    textDict['tblphrag_Acres'].text = str(float(textDict['tblphrag2008'].text) - float(textDict['tblphrag1974'].text))
    
    if float(textDict['tblfm1974'].text)>0:
        percent1 = (float(textDict['tblfm_Acres'].text)/float(textDict['tblfm1974'].text))*100
        textDict['tblfm_Per'].text = str("%.2f" % percent1)
    if float(textDict['tblhm1974'].text)>0:
        percent2 = (float(textDict['tblhm_Acres'].text)/float(textDict['tblhm1974'].text))
        textDict['tblhm_Per'].text = str("%.2f" % percent2)
    if float(textDict['tblim1974'].text)>0:
        percent3 = (float(textDict['tblim_Acres'].text)/float(textDict['tblim1974'].text))*100
        textDict['tblim_Per'].text = str("%.2f" % percent3)
    if float(textDict['tblphrag1974'].text)>0:
        percent4 = (float(textDict['tblphrag_Acres'].text)/float(textDict['tblphrag1974'].text))*100
        textDict['tblphrag_Per'].text = str("%.2f" % percent4)
    

#%%
import arcpy

arcpy.env.overwriteOutput = True

#Set the workspace
arcpy.env.workspace = r"\\gis-serv\workspace\private\mapbooks\mapbook.gdb"
arcpy.env.scratchWorkspace = r"\\gis-serv\workspace\private\mapbooks\mapbook.gdb"
mapLocation = r"\\gis-serv\workspace\private\mapbooks\mapstest"

#define the template .mxd
#which mxd is your template?
mapdoc = r"\\gis-serv\workspace\private\mapbooks\layout_template_test.mxd"
template = arcpy.mapping.MapDocument(mapdoc)

#define the dataframes
dfBefore = arcpy.mapping.ListDataFrames(template, "1974")[0]
dfAfter = arcpy.mapping.ListDataFrames(template, "2008")[0]


#%%
#define the columns
cols = arcpy.mapping.ListLayoutElements(template,"TEXT_ELEMENT","*Col")
colsDict = {col.name:col for col in cols}

#define the rows
records = arcpy.mapping.ListLayoutElements(template,"TEXT_ELEMENT","*Row")
recordsDict = {record.name:record for record in records}

#define all text elements in the table
textBoxes = arcpy.mapping.ListLayoutElements(template,"TEXT_ELEMENT","tbl*")
textDict ={x.name:x for x in textBoxes}

#%%
#define the center of each column
xPosLeftCol = colsDict['CategoryCol'].elementPositionX
xPosMiddleCol = colsDict['acreage1974Col'].elementPositionX
xPosRightCol = colsDict['acreage2008Col'].elementPositionX
xPosDiffAcres = colsDict['DiffAcresCol'].elementPositionX
xPosDiffPerc = colsDict['DiffPercentCol'].elementPositionX

yPosHeader = colsDict['CategoryCol'].elementPositionY
yPosFM = recordsDict['fmRow'].elementPositionY
yPosHM = recordsDict['hmRow'].elementPositionY
yPosIM = recordsDict['imRow'].elementPositionY
yPosPanne = recordsDict['panneRow'].elementPositionY
yPosPhrag = recordsDict['phragRow'].elementPositionY
yPosUnv = recordsDict['unvRow'].elementPositionY
yPosUp = recordsDict['upRow'].elementPositionY

#%%
setToZero()

#%%
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
rows = arcpy.SearchCursor(r"data\DEC_tidalwetlands_test", "", "", "", "")
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
            textDict['tblfm1974'].text = str(roundedNum1974)
        elif row[0] == "HM":
            textDict['tblhm1974'].text = str(roundedNum1974)
        elif row[0] == "IM":
            textDict['tblim1974'].text = str(roundedNum1974)
        elif row[0] == "PH":
            textDict['tblphrag1974'].text = str(roundedNum1974)
        #print row[0] + ", " + roundedNum1974
    
    #print "2008 Table"
    table2008 = arcpy.da.SearchCursor(wetlands2008Table,["TWL_Class","SUM_Acreage"])
    for row1 in table2008:
        roundedNum2008 = "%.2f" % row1[1]
        if row1[0] == "FreshMarsh":
            textDict['tblfm2008'].text = str(roundedNum2008)
        elif row1[0] == "HighMarsh":
            textDict['tblhm2008'].text = str(roundedNum2008)
        elif row1[0] == "IntertidalMarsh":
            textDict['tblim2008'].text = str(roundedNum2008)
        elif row1[0] == "Panne/Unvegetated":
            textDict['tblpanne2008'].text = str(roundedNum2008)
        elif row1[0] == "Phragmites":
            textDict['tblphrag2008'].text = str(roundedNum2008)
        elif row1[0] == "Unvegetated":
            textDict['tblunv2008'].text = str(roundedNum2008)
        elif row1[0] == "Upland":
            textDict['tblup2008'].text = str(roundedNum2008)
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


