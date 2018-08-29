import pandas as pd
import glob
import os
import pathlib
import numpy as np
import time
import datetime

#file location of all eeg and egt data:
# K:\Center for Autism and Brain Development\DukeACT\Data and Analysis\EEG and EGT\DukeACT EEG Analysis\T1 EEG Analysis\ACT T1 EEG Text Files 3-30 Hz\Bubl 

# file location of all egt data

# K:\Center for Autism and Brain Development\DukeACT\Data and Analysis\EEG and EGT\DukeACT EEG Analysis\T1 EEG Analysis\ACT T1 EEG Text Files 3-30 Hz\Socl

# file locatoin of all eeg data 

# K:\Center for Autism and Brain Development\DukeACT\Data and Analysis\EEG and EGT\DukeACT EEG Analysis\T1 EEG Analysis\ACT T1 EEG Text Files 3-30 Hz\Toys


bubl_path ='K:\Center for Autism and Brain Development\Data Center Documentation\DukeACT\EEG_EGT_upload\EEG\ACT T1 EEG Text Files 3-30 Hz\Toys' # use your path


bubl_file = []
for (dirpath, dirnames, filenames) in os.walk(bubl_path):
	bubl_file.extend(filenames)

print(bubl_file)


for i in range(len(bubl_file)):
	print(bubl_file[i])
	os.rename(bubl_path + r'\\' + bubl_file[i], bubl_path + bubl_file[i] + ".txt")



