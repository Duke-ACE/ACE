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

x = pandas.read_csv("sub_med.csv")


ndar_compare = x.columns.values.tolist()

token = ""

data = {
    'token': '',
    'content': 'record',
    'format': 'json',
    'type': 'flat',
    'forms[0]': 'ace_subject_medical_history',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'exportSurveyFields': 'false',
    'exportDataAccessGroups': 'false',
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

redcap_compare = df.columns.values


test = []
test2 = []

for i in range(len(redcap_compare)):
	test.append(str(redcap_compare[i].split("___")[0]))

[x for x in test if "___" in x]

redcap_compare = list(set(test))

for i in range(len(redcap_compare)):
	test2.append(str(redcap_compare[i].strip().lower().replace(' ', '_').replace('(', '').replace(')', '')))

print(len(ndar_compare), len(redcap_compare))

redcap_dev = list(set(ndar_compare) & set(test))

ndar_dev = list(set(ndar_compare) - set(test))

print(len(set(redcap_dev)))

print(ndar_dev)


test_df1 = pandas.DataFrame([], columns = [list(ndar_compare)])


test = []

for i in range(len(list(test_df1.columns))):
	test.append(str(test_df1.columns[i][-1]).strip("(").strip(")").strip("'").strip("'").strip(","))


# print(test)

# print(type(test[0]))

test_df2 = pandas.DataFrame(columns = test, index=range(0))




test_df2.columns = test_df2.columns.str.strip("'")

test_df3 = pandas.concat([df,test_df2])

# print(test_df3)

# for i in range(len(test)):
# 	try:
# 		test_df3 = test_df3[[test[i]]]
# 	except:
# 		pass

# print(test_df2.columns)
df = test_df3[test_df3.columns & test_df2.columns]
print(df)


# x = pandas.concat([df, test_df1], ignore_index=True, axis=0)

# print(x)
