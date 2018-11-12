import pandas

age_location = pandas.read_csv('Age_location.csv')

measure_comp = pandas.read_csv('measure_comp.csv')

# print(age_location.columns.values)

# print(measure_comp)


join = {} 

dfinal = age_location.merge(measure_comp, on = "ace_id", how="left")

dfinal = dfinal.fillna(0)

print(dfinal)

dfinal.to_csv("p1_status.csv")