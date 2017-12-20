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
	# print dl.SequenceMatcher(None,x.values[i][0], x.values[i+1][0]).ratio()
	# print x.values[i][0], x.values[i+1][0]
	
	if(dl.SequenceMatcher(None,x.values[i][0], x.values[i+1][0]).ratio() < .80 ):
		
		breaks.append(i)


print len(breaks)


broken = []

for i in range(0,len(breaks)-1):
		broken.append([x.values[int(breaks[i]):int(breaks[i+1])]])

variables = []


for stuff in broken:
	for i in stuff:
		for brake in i:
			variables.append(brake[0])


print len(variables)


numbering = []

for i in range(0,len(breaks)-1):
	for j in range(len(np.asarray(broken)[i][0])):
		numbering.append(j)
# 		exec("""var{}=np.asarray(broken).item()""".format(i))


transition = []


print len(numbering)


for i in range(0, len(variables)):
	transition.append(str(variables[i]) + '_' + str(numbering[i]))

# flat_list = []

print transition

# print transition


csv_df = pd.DataFrame(transition)


csv_df.to_csv('test.csv')










# 	for j in 
# 	print "var%s" % (i)
# 	exec len("var%s" % (i) 
	# for j in range(0, len("var%s" % (i))):
	# 	print j
		# exec "var%s=np.asarray(broken)[i].item()[j][0] + '_' + str(j)" % (i)

# print [[row[i] for row in np.asarray(broken)[i].item()] for i in range(len(np.asarray(broken)[0].item()))]


# print map(np.asarray(broken)[i].item()[j][0] + '_' + str(range())



# print var50

# def transition(variable, transition)
# 	for i in range(0,len()):
# 		transition.extend ("var%s[i][0] + '_' + str(i)" % (i))



# def transition(var): 





