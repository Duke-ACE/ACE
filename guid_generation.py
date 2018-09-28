#Guid Generation 

import os.path
import os
import urllib2
import urllib
from urllib2 import Request
from urllib import urlencode 
from requests import post
import sys
import pandas
import json
import numpy as np


data = {
    'token': '',
    'content': 'report',
    'format': 'json',
    'report_id': '13192',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'returnFormat': 'json'
}

r = post("https://redcap.duke.edu/redcap/api/", data)
r.content
d = urlencode(data)
req = urllib2.Request("https://redcap.duke.edu/redcap/api/", d)
response = urllib2.urlopen(req)
file = response.read()
result = json.loads(file)
df = pandas.DataFrame.from_records(result)

print(df.columns.values)



columns = {"ACE_ID", "ID" , "FIRSTNAME",	"MIDDLENAME",	"LASTNAME",	"MOB",	"DOB",	"YOB", "COB", "SEX", "SUBJECTHASMIDDLENAME",	"USEEXISTINGGUID"}

guid_df = pandas.DataFrame([], columns=columns)

ID = []
ACE_ID = df["ace_id"].tolist()
FIRSTNAME = df['child_fname'].tolist()
MIDDLENAME = df['child_mname'].tolist()
LASTNAME = df['child_lname'].tolist()
DOB_hold = df['child_dob'].tolist()
MOB = []
DOB = []
YOB = []
COB = df['child_city'].tolist()
SEX = df['child_gender'].tolist()

for i in range(len(DOB_hold)):
    ID.append(i)
    x = DOB_hold[i].split("-")
    mob = x[1]
    dob = x[2]
    
    mob = '{}'.format(mob[1:] if mob.startswith('0') else mob)
    dob = '{}'.format(dob[1:] if dob.startswith('0') else dob)
    
    YOB.append(x[0])
    MOB.append(mob)    
    DOB.append(dob)

guid_df["ID"] = ID
guid_df["FIRSTNAME"] = FIRSTNAME
guid_df["MIDDLENAME"] = MIDDLENAME
guid_df["LASTNAME"] = LASTNAME
guid_df["MOB"] = MOB
guid_df["DOB"] = DOB
guid_df["YOB"] = YOB
guid_df["COB"] = COB
guid_df["SEX"] = SEX
guid_df["SEX"] = np.where(guid_df['SEX'] == '0', "FEMALE", "MALE") 
guid_df["SUBJECTHASMIDDLENAME"] = np.where(guid_df['MIDDLENAME'] == '', "NO", "YES") 
guid_df["USEEXISTINGGUID"] = "NO"
guid_df["ACE_ID"] = ACE_ID


guid_df = guid_df[["ACE_ID", "FIRSTNAME", "MIDDLENAME",   "LASTNAME", "MOB",  "DOB",  "YOB", "COB", "SEX", "SUBJECTHASMIDDLENAME",    "USEEXISTINGGUID"]]

guid_df.to_csv("GUID_all.csv", index=False)




