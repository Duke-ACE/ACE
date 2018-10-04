import pandas 

double_entry = pandas.read_csv("C:\Users\wfcla\Desktop\ARC\double_entry.csv")


datadict = pandas.read_csv("C:\Users\wfcla\Desktop\ARC\\fam_med_dd\instrument.csv")



print(double_entry)

variables_wrong = double_entry['Variables Wrong']
record_id = double_entry["Record ID"]

test = variables_wrong.values.tolist()

x =  []

for i in range(len(test)):
	x.append(test[i].split(" "))
y = []

for i in range(len(x)):
	y.append(x[i][2:])


record_id = record_id.tolist()

dict_record = {key: [] for key in record_id}

print(dict_record)

# dict_record.fromkeys([record_id], None)
# print(datadict)

test_ary = []

for i in range(len(record_id)):
	for j in range(len(y[i])):
		x = datadict[datadict['Variable / Field Name'] == str(y[i][j])]
		string = str(x['Field Label'].values[0])
		# print(string)
		test = "{} ".format(string)
		print(record_id[i])
		dict_record[record_id[i]].append(string)
# 		test_ary.append(test)

print(dict_record)


test_df = pandas.DataFrame.from_dict(dict_record, orient="index")

test_df.to_csv("test.csv")

# for i in len(double_entry):

