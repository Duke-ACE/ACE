import os
import urllib
from requests import post
import urllib.request
import wx
import sys
import requests
import urllib
from requests import post
import pandas as pd
import json
import os.path
import csv
import numpy as np
import datetime
import pandas



print("Calling RedCAP API...")




def getData(data):
  r = post("https://redcap.duke.edu/redcap/api/", data) 
  r.content
  d = urllib.parse.urlencode(data).encode("utf-8")
  req = urllib.request.Request("https://redcap.duke.edu/redcap/api/", d)
  response = urllib.request.urlopen(req)
  file = response.read()
  result = json.loads(file)
  df = pd.DataFrame.from_records(result)
  return df

# print(str(record_id['record_id'].values[0]))

log_df = pandas.DataFrame(columns=['Record_ID', "Second Entry Exist", 'Variables Wrong', 'Entries are Equal'])

data = {
    'token': 'E643DF26872773CD6C4BE421CF36A476',
    'content': 'record',
    'format': 'json',
    'type': 'flat',
    'records[0]': "6" ,
    'forms[0]': 'pefb',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
    'returnFormat': 'json'
}
entry = getData(data)

print(entry.iloc[[0]])

entry1 = entry.iloc[[0]]
entry2 = entry.iloc[[1]]
entry1.index = ['x']
entry2.index = ['x']
ne = (entry1 != entry2).any(1)
ne_stacked = (entry1 != entry2).stack()
compare = ne_stacked[ne_stacked]
if(len(compare) == 0):
      log_df['Entries are Equal'].loc[0] = "Yes"
else:
      log_df['Entries are Equal'].loc[0] = "No"
      flagged = ""
      for flags in compare.index:
            flagged=flagged +" " + str(flags[1])
            print(flags[1])
            # flagged.append(flags[1])
            log_df['Variables Wrong'].loc[i] = flagged
log_df["Second Entry Exist"].loc[0] = "Yes" 
# except IndexError:
#       log_df["Second Entry Exist"].loc[0] = "No"




print(log_df)


# flagged = []



# print str(flagged).strip("[]")



# print("Moving data to path...")




