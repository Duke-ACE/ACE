import pandas as pd
import glob
import os
import pathlib
import numpy as np
import time
import datetime
import random 


egt_path  = 'K:\Center for Autism and Brain Development\Data Center Documentation\DukeACT\EEG_EGT_upload\EGT\DukeACT_T1_EGT\DukeACT_T1_EGT Text Files'

rex_codes = 'K:\Center for Autism and Brain Development\Data Center Documentation\DukeACT\EEG_EGT_upload\egt\\rex_codes.csv'

id_path = 'K:\Center for Autism and Brain Development\Data Center Documentation\DukeACT\EEG_EGT_upload\egt\\rexid_actid.csv'

subject_ary =[]
date_ary =[]
assessment_id_ary  = []
study_ary  = []
timepoint_ary  = []
stim_ary  = []
egt_data_ary  = [] 
egt_ptoma_ary = [] 
egt_ptomd_ary = []
egt_pted_ary = []
egt_ptmd_ary = []
egt_ptafd_ary = []
egt_ptoaa_ary = []
egt_ptoad_ary = []
egt_entire_length_ary = []
egt_dbseg_length_ary = []
egt_number_samples_ary = []



rex_codes = pd.read_csv(rex_codes, header=0)



def egt_format(path):
	df_ids = pd.read_csv(id_path, header=0)
	file = []
	files = []
	



	for (dirpath, dirnames, filenames) in os.walk(egt_path):
		file.extend(filenames)
	
	for i in range(len(file)):	
		files.append(egt_path + r'\\' + file[i])
		print(files)

	for i in range(len(files)):
		mod_time = os.path.getmtime(files[i])
		mod_time = datetime.datetime.strptime(time.ctime(mod_time), "%a %b %d %H:%M:%S %Y")
		mod_time = str(mod_time).split(" ")[0]
		egt_df = pd.read_csv(files[i], sep='\t', header=None)
		egt_df.columns = ['egt_ptoma',	'egt_ptomd',	'egt_pted',	'egt_ptmd',	'egt_ptafd',	'egt_ptoaa',	'egt_ptoad',	'egt_entire_length',	'egt_dbseg_length',	'egt_number_samples', 'egt_ttdb', 'egt_tta']
		egt_df['date'] = mod_time
		assessment_id = random.randint(100000000,999999999)
		egt_df['assessment_id'] =  assessment_id
		ids = df_ids[df_ids["study_id"] == str(file[i].strip('EGT').split("_")[0])]
		rex_ids = ids["rex_id"]		
		# condition = df_ids[df_ids["study_id"] == str(file[i].strip(str(rex_ids.values[0])).split("_")[0])]
		egt_data_df = rex_codes[rex_codes['Subject ID'] == ids['study_id'].values[0]]
		rex_code = egt_data_df['Rex Code']
		egt_ptoma_ary.append(egt_df['egt_ptoma'].values[0])
		egt_ptomd_ary.append(egt_df['egt_ptomd'].values[0])
		egt_pted_ary.append(egt_df['egt_pted'].values[0])
		egt_ptmd_ary.append(egt_df['egt_ptmd'].values[0])
		egt_ptafd_ary.append(egt_df['egt_ptafd'].values[0])
		egt_ptoaa_ary.append(egt_df['egt_ptoaa'].values[0])
		egt_ptoad_ary.append(egt_df['egt_ptoad'].values[0])
		egt_entire_length_ary.append(egt_df['egt_entire_length'].values[0])
		egt_dbseg_length_ary.append(egt_df['egt_dbseg_length'].values[0])
		egt_number_samples_ary.append(egt_df['egt_number_samples'].values[0])
		subject_ary.append(rex_ids.values[0])
		date_ary.append(mod_time)
		assessment_id_ary.append(assessment_id)
		egt_data_ary.append(rex_code.values[0])
		timepoint_ary.append('T1')
		study_ary.append('duke-act')




egt_format(egt_path)

egt_upload = pd.DataFrame({'subject' : subject_ary , 'date':  date_ary, 'assessment_id': assessment_id_ary, 'study' : study_ary, 'timepoint' : timepoint_ary, 'egt_data' : egt_data_ary, 'egt_ptoma' : egt_ptoma_ary, 'egt_ptomd' : egt_ptomd_ary, 'egt_pted'  : egt_pted_ary , 'egt_ptmd' : egt_ptmd_ary, 'egt_ptafd' :  egt_ptafd_ary, 'egt_ptoaa' : egt_ptoaa_ary, 'egt_ptoad' : egt_ptoad_ary , 'egt_entire_length' : egt_entire_length_ary , 'egt_dbseg_length' : egt_dbseg_length_ary , 'egt_number_samples' :  egt_number_samples_ary})

egt_upload.to_csv('act-egt.3.csv')

print(egt_upload)
