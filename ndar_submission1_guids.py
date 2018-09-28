#ndar submission 1
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
    'report_id': '13179',
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

ids = df['ace_id'].tolist()

ids = list(set(ids))

df_guids = pandas.read_csv("GUID_all.csv")

print(df_guids)

mask = df_guids['ACE_ID'].isin(ids)

df_arc_guids = df_guids.loc[mask]

df_arc_guids.to_csv("arc_guids.csv")