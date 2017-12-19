import pandas as pd
import numpy as np
import difflib as dl

x = pd.read_csv('ACE_Project.csv')

print len(x)

#print x.values[i][0], x.values[i+1][0]
# print dl.SequenceMatcher(x.values[i][0], x.values[i+1][0]).ratio()

# print x

breaks = []

for i in range(0,len(x)-1):
	#print x.values[i][0], x.values[i+1][0]
	
	if(dl.SequenceMatcher(None,x.values[i][0], x.values[i+1][0]).ratio() < .80):
		breaks.append(i)

print x.values[int(breaks[0]):int(breaks[1])]


def breaker(broken):
	broken = []
	for i in range(0,len(breaks)):
		broken = [x.values[int(breaks[i]):int(breaks[i+1])] 







# for stuff in breaks:
# 	breaker


# for i in range(0,len(x)):
# 	print x.values[i][0] 

