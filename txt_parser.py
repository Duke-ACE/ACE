
from rios.conversion import (
    redcap_to_rios,
    qualtrics_to_rios,
    rios_to_redcap,   
    rios_to_qualtrics,
)  

import glob
import csv
import pandas
import os
import numpy as np
import yaml
import json
from redcap import Project, RedcapError

url_p1 = 'https://redcap.duke.edu/redcap/api/'
api_p1 = ''
project = Project(url_p1, api_p1)



# files = glob.glob("*.txt")

file_name = 'ae'

new = pandas.read_table('{}.txt'.format(file_name), skiprows=0)

to_drop = ['Author', 'Page', 'Summary', 'Variableset']

dropped = new[~new['----------------------- Page 1-----------------------'].str.contains('|'.join(to_drop))]

split = pandas.DataFrame(dropped['----------------------- Page 1-----------------------'].str.split(':',1).tolist(),
                                   columns = ['Variable / Field Name','Field Type'])

extras = pandas.DataFrame([['Subject ID', 'TEXT']], columns=['Variable / Field Name', 'Field Type'])

clean = split.append(extras)

clean['Field Type'] = clean['Field Type'].str.replace(" ", "")

clean['Variable / Field Name'] = clean['Variable / Field Name'].str.replace(" ", "")

clean =  clean.drop_duplicates()

final = clean.replace([None,'DATETIME'], 'TEXT')

final['Field Type'] = final['Field Type'].str.lower()

final['Variable / Field Name'] = final['Variable / Field Name'].str.lower()

conditions = (final['Variable / Field Name'].str.contains('yesno') == True), (final['Variable / Field Name'].str.contains('yesno') == False)

choices = ['0, Yes | 1,  No', '']

final['Choices, Calculations, OR Slider Labels'] = np.select(conditions, choices, default=' ')


final['Field Type'] = final['Field Type'].str.replace(" ", "")
final['Field Type'] = final['Field Type'].str.replace("biosample", "text")
final['Form Name'] = file_name
final['Field Label'] = 'Questions'
final['Section Header'] = ''
final['Field Note']	= ''
final['Text Validation Type OR Show Slider Number']	 = ''
final['Text Validation Min'] =''
final['Text Validation Max'] =''
final['Identifier?'] =''
final['Branching Logic (Show field only if...)'] =''	
final['Required Field?'] =''
final['Custom Alignment'] =' '	
final['Question Number (surveys only)'] = ''	
final['Matrix Group Name']=''
final['Matrix Ranking?'] =''
final['Field Annotation']='' 


final['Variable / Field Name'] = final['Variable / Field Name'].str.partition('(')

final = final[['Variable / Field Name', 'Form Name', 'Section Header','Field Type' ,'Field Label', 'Choices, Calculations, OR Slider Labels', 'Field Note' ,	'Text Validation Type OR Show Slider Number',	'Text Validation Min'	,'Text Validation Max',	'Identifier?',	'Branching Logic (Show field only if...)'	,'Required Field?',	'Custom Alignment',	'Question Number (surveys only)',	'Matrix Group Name',	'Matrix Ranking?', 'Field Annotation']]

print final

to_csv = final.to_csv('{}.csv'.format(file_name), index = False)





# with open("format_1_i.yaml") as infile:
# 	instrument = yaml.load(infile)


# with open("format_1_f.yaml") as infile: 
# 	form = yaml.load(infile)
