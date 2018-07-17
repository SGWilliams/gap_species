# -*- coding: utf-8 -*-
"""
Generate XML for Vert HabMap and Range datasets from template and CSVs

Created on Thu Jul 12 13:03:00 2018

@author: SGWilliams

"""

## Imports and environment settings
import sys
sys.path.append("P:/Proj3/USGap/Scripts/") ## This is the path to the config file
sys.path.append("P:/Proj3/USGap/Scripts/GAPProduction")
import datetime
import time
import csv

# Set directories
xmlPath = "P:/Proj2/2001_GAP_Vert_Products/final_xml/"

############ RANGE ##########################
rngCSV = xmlPath + 'ScienceBaseRangeMapCSV_20180713.csv'
rngXML = xmlPath + 'CONUS 2001v1 Range Map TEMPLATE 13jul2018.xml'

# Iterate through each record in table
with open(rngCSV, 'r') as csv_file:
    reader = csv.reader(csv_file)
    # Reading row by row, set variables
    for row in reader:
        if row[1] != 'strUC':
            sbItem = row[0]
            strUC = row[1]    
            comName = row[2]    
            sciName = row[3]    
            doiPath = row[4]    
            sbPath = row[5]    
            editName = row[6]    
            revName = row[7]    
            startDate = row[8]    
            endDate = row[9]    
            pubDate = row[10]    
            pubYear = pubDate[0:4]
            # Convert editName variable to list, get unique set, build replacement text
            editList0 = (editName[1:-1].replace("'", "").split(", "))    
            list_set = set(editList0)
            editList = (list(list_set))
            if len(editList) == 1:
                editTxt = editList[0]
            elif len(editList) == 2:
                editTxt = editList[0] + ' and ' + editList[1]
            elif len(editList) == 3:
                editTxt = editList[0] + ', ' + editList[1] + ' and ' + editList[2]
            elif len(editList) == 4:
                editTxt = editList[0] + ', ' + editList[1] + ', ' + editList[2] + ' and ' + editList[3]
            # Set taxa
            if strUC[0:1] == 'a':
                strTaxa1 = 'Amphbians'
                strTaxa2 = 'amphbians'
            elif strUC[0:1] =='b':
                strTaxa1 = 'Birds'
                strTaxa2 = 'birds'
            elif strUC[0:1] == 'm':
                strTaxa1 = 'Mammals'
                strTaxa2 = 'mammals'
            elif strUC[0:1] == 'r':
                strTaxa1 = 'Reptiles'
                strTaxa2 = 'reptiles'
            strDate = str(datetime.date.today().strftime("%Y-%m-%d"))
                        
            # Set variable replacements
            wordReplacements = {'sb_Item':sbItem, 
                                'str_UC':strUC, 
                                'com_Name':comName, 
                                'sci_Name':sciName, 
                                'doi_Path':doiPath, 
                                'sb_Path':sbPath, 
                                'edit_Txt':editTxt, 
                                'rev_Name':revName,  
                                'start_Date':startDate, 
                                'end_Date':endDate, 
                                'pub_Date':pubDate, 
                                'pub_Year':pubYear,
                                'str_Taxa1':strTaxa1, 
                                'str_Taxa2':strTaxa2,
                                'str_Date':strDate }
            
            # Set output file name
            outXML = xmlPath + 'rng/' + strUC + '_CONUS_Range_2001v1.xml'
            
            # Open template and replace variables line by line, save output
            with open(outXML, "w") as output_file, open(rngXML) as input_file:
                for line in input_file:
                    for src, target in wordReplacements.iteritems():
                        line = line.replace(src, target)
                    output_file.write(line)
            
############ HABITAT ##########################
habCSV = xmlPath + 'ScienceBaseHabMapCSV_20180713.csv'
habXML = xmlPath + 'CONUS 2001v1 Habitat Map TEMPLATE 13jul2018.xml'

# Iterate through each record in table
with open(habCSV, 'r') as csv_file:
    reader = csv.reader(csv_file)
    # Reading row by row, set variables
    for row in reader:
        if row[0] != 'GAP_code':
            strUC = row[0]    
            comName = row[1]    
            sciName = row[2]    
            startDate = row[3]    
            endDate = row[4]    
            pubDate = row[5]
            placeKeys = row[6]
            themeKeys = row[7]
            editName = row[8]    
            revName = row[9]    
            nsElcode = row[10]
            tsnCode = row[11]
            nsGlobal = row[12]
            inDataStr = row[13]
            ipCode = row[14]
            doiPath = row[15]
            sbPath = row[16]
            pubYear = pubDate[0:4]
            # Convert inDataStr variable to list - not used yet in metadata
            inDataList = (editName[1:-1].replace("'", "").split(", "))    
            # Set taxa
            if strUC[0:1] == 'a':
                strTaxa1 = 'Amphbians'
                strTaxa2 = 'amphbians'
            elif strUC[0:1] =='b':
                strTaxa1 = 'Birds'
                strTaxa2 = 'birds'
            elif strUC[0:1] == 'm':
                strTaxa1 = 'Mammals'
                strTaxa2 = 'mammals'
            elif strUC[0:1] == 'r':
                strTaxa1 = 'Reptiles'
                strTaxa2 = 'reptiles'
            strDate = str(datetime.date.today().strftime("%Y-%m-%d"))
                        
            # Set variable replacements
            wordReplacements = {'str_UC':strUC, 
                                'com_Name':comName, 
                                'sci_Name':sciName, 
                                'start_Date':startDate, 
                                'end_Date':endDate, 
                                'pub_Date':pubDate,  
                                'place_Keys':placeKeys, 
                                'themeKeys':themeKeys, 
                                'edit_Name':editName, 
                                'rev_Name':revName,  
                                'ns_Elcode':nsElcode, 
                                'tsn_Code':tsnCode, 
                                'ns_Global':nsGlobal, 
                                'ip_Code':ipCode, 
                                'doi_Path':doiPath, 
                                'sb_Path':sbPath, 
                                'pub_Year':pubYear,
                                'in_DataStr':inDataStr, #!!!!!!!!!!!!
                                'str_Taxa1':strTaxa1, 
                                'str_Taxa2':strTaxa2,
                                'str_Date':strDate }
            
            # Set output file name
            outXML = xmlPath + 'hab/' + strUC + '_CONUS_HabMap_2001v1.xml'
            
            # Open template and replace variables line by line, save output
            with open(outXML, "w") as output_file, open(habXML) as input_file:
                for line in input_file:
                    for src, target in wordReplacements.iteritems():
                        line = line.replace(src, target)
                    output_file.write(line)

##########################################################