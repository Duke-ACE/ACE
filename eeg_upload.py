import pandas as pd
import glob
import os
import pathlib
import numpy as np
import time
import datetime
import random

toys_path ='K:\Center for Autism and Brain Development\Data Center Documentation\DukeACT\EEG_EGT_upload\EEG\ACT T1 EEG Text Files 3-30 Hz\Toys' # use your path

socl_path = 'K:\Center for Autism and Brain Development\Data Center Documentation\DukeACT\EEG_EGT_upload\EEG\ACT T1 EEG Text Files 3-30 Hz\Socl'

bubl_path = 'K:\Center for Autism and Brain Development\Data Center Documentation\DukeACT\EEG_EGT_upload\EEG\ACT T1 EEG Text Files 3-30 Hz\Bubl' 

id_path = 'K:\Center for Autism and Brain Development\Data Center Documentation\DukeACT\EEG_EGT_upload\EEG\\rexid_actid.csv'

rex_codes = 'K:\Center for Autism and Brain Development\Data Center Documentation\DukeACT\EEG_EGT_upload\EEG\\rex_codes.csv'


hz = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

eeg_col = ['subject', 'date', 'assessment_id', 'study','timepoint', 'condition', 'stim', 'eeg_data']



subject_ary =[]
date_ary =[]
assessment_id_ary  = []
study_ary  = []
timepoint_ary  = []
condition_ary  = []
stim_ary  = []
eeg_data_ary  = [] 
eeg_abs_final = [] 
eeg_final = []
rex_codes = pd.read_csv(rex_codes, header=0)

def eeg_format(path, stripped, rex, stimulus):

	df_ids = pd.read_csv(id_path, header=0)
	file = []
	for (dirpath, dirnames, filenames) in os.walk(path):
		file.extend(filenames)
	files = []
	for i in range(len(file)):	
		files.append(path + r'\\' + file[i])
	for i in range(len(files)):
		mod_time = os.path.getmtime(files[i])
		mod_time = datetime.datetime.strptime(time.ctime(mod_time), "%a %b %d %H:%M:%S %Y")
		mod_time = str(mod_time).split(" ")[0]
		eeg_df = pd.read_csv(files[i], "\t", header=None)
		eeg_df['date'] = mod_time
		assessment_id = random.randint(100000000,999999999)
		eeg_df['assessment_id'] =  assessment_id
		ids = df_ids[df_ids["study_id"] == str(file[i].strip(stripped).split("_")[0])]
		rex_ids = ids["rex_id"]		
		# condition = df_ids[df_ids["study_id"] == str(file[i].strip(str(rex_ids.values[0])).split("_")[0])]
		eeg_data_df = rex_codes[rex_codes['Subject ID'] == ids['study_id'].values[0]]
		
		rex_code = eeg_data_df[rex]
		eeg_df['hertz'] = hz
		eeg_df['rex_ids'] = rex_ids.values[0]

		subject_ary.append(rex_ids.values[0])
		condition_ary.append(stripped)
		date_ary.append(mod_time)
		assessment_id_ary.append(assessment_id)
		eeg_data_ary.append(rex_code.values[0])
		timepoint_ary.append('T1')
		stim_ary.append(stimulus)
		study_ary.append('duke-act')
		eeg_abs_final.append(eeg_df)


# bubl_upload = eeg_format(bubl_path, "Bubl", 'Bubl Rex Code', "1")

# bubl_eeg_upload = pd.DataFrame({'subject' : subject_ary , 'date':  date_ary, 'assessment_id': assessment_id_ary, 'study' : study_ary, 'timepoint' : timepoint_ary, 'condition' : condition_ary,  'stim' : stim_ary, 'eeg_data' : eeg_data_ary}) 
# bubl_eeg_upload.to_csv('bubl/eeg-upload.1.csv')
# bubl_abs_df = pd.concat(eeg_abs_final)
# bubl_abs_df.to_csv('bubl/eeg-upload.1.abspower.csv')


# socl_upload = eeg_format(socl_path, "Socl", 'Socl Rex Code', "2")
# socl_eeg_upload = pd.DataFrame({'subject' : subject_ary , 'date':  date_ary, 'assessment_id': assessment_id_ary, 'study' : study_ary, 'timepoint' : timepoint_ary, 'condition' : condition_ary,  'stim' : stim_ary, 'eeg_data' : eeg_data_ary}) 

# socl_eeg_upload.to_csv('socl/eeg-upload.1.csv')
# socl_abs_df = pd.concat(eeg_abs_final)
# socl_abs_df.to_csv('socl/eeg-upload.1.abspower.csv')


# toys_upload = eeg_format(toys_path, "Toys", "Toys Rex Code", "3")
# toys_eeg_upload = pd.DataFrame({'subject' : subject_ary , 'date':  date_ary, 'assessment_id': assessment_id_ary, 'study' : study_ary, 'timepoint' : timepoint_ary, 'condition' : condition_ary,  'stim' : stim_ary, 'eeg_data' : eeg_data_ary}) 
# toys_eeg_upload.to_csv('toys/eeg-upload.1.csv')
# toys_abs_df = pd.concat(eeg_abs_final)
# toys_abs_df.to_csv('toys/eeg-upload.1.abspower.csv')



