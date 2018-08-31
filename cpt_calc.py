import scipy
import pandas 
from requests import post 
import sys
import pandas as pd
import json 
import datetime 
import requests 
import shutil 
import base64
import urllib3 
import wget 
import glob
from scipy.stats import norm
from scipy.special import ndtri
from scipy.stats import norm
from math import exp,sqrt
import datetime 
import os
import wx
import os.path
import csv
import numpy as np




class RedirectText(object):
	def __init__(self,aWxTextCtrl):
		self.out=aWxTextCtrl
	def write(self,string):
		self.out.WriteText(string)



# style= wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER 


#------Intialize the creation of the frames that are used with wxPython----#

class Frame(wx.Frame):
	def __init__(self, parent, title):




#----Initialize the wxPython GUI frame and panel and add events------#
		
		wx.Frame.__init__(self, parent, title=title, style= wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)
		self.panel = wx.Panel(self)
	
#---Intialize the methods to be used within the combo selector class----#

		self.statusbar = self.CreateStatusBar()
		self.statusbar.SetStatusText('Duke ACE Scoring v0.1')
		
		self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
		
		self.btnexecute = wx.Button(self.panel, -1, "Execute", pos=[1,1])
		self.Bind(wx.EVT_BUTTON, self.run, self.btnexecute)

		self.log = wx.TextCtrl(self.panel, wx.ID_ANY, size=(380,100),
						  style = wx.TE_MULTILINE|wx.TE_READONLY)

		
#-----------Begin the creation of the sizer and layout of the GUI--------------#


		sizer = wx.BoxSizer(wx.VERTICAL)

		btm_flags = wx.SizerFlags().Expand()

		bottomsizer = wx.BoxSizer(wx.VERTICAL)
		bottomsizer.Add(self.log, wx.ALL | wx.GROW)
		bottomsizer.Add(self.btnexecute, btm_flags)

		sizer.Add(bottomsizer, btm_flags)


		self.panel.SetSizer(sizer)
		self.panel.SetInitialSize()
		sizer.SetSizeHints(self)
		self.panel.Layout()
		self.Show()
		redir=RedirectText(self.log)
		sys.stdout=redir



#------Begin the creation of the event functions that are used within the GUI-----------#


	def GetRecordID(self, e):
		dlg = wx.TextEntryDialog(self.panel, 'Please Enter the Patients Record ID:' ,"","", 
				style=wx.OK)
		var = dlg.GetValue()
		dlg.ShowModal()
		records = dlg.GetValue()
		dlg.Destroy()
		return records


	def OnCloseWindow(self, e):
		self.Destroy()


	def getData(data):
		  r = post("https://redcap.duke.edu/redcap/api/", data)
		  r.content
		  d = urlencode(data)
		  req = urllib2.Request("https://redcap.duke.edu/redcap/api/", d)
		  response = urllib2.urlopen(req)
		  file = response.read()
		  result = json.loads(file)
		  df = pandas.DataFrame.from_records(result)
		  return df


	def run(self, event):

		now = datetime.datetime.now()

		print("Executing...")
		record = self.GetRecordID(event)


		x = glob.glob("*.csv")

		cpt_df = pd.read_csv(x[0], skiprows = [0,1,2,3,4,5,6,7,8,9,10])

		cpt_df = cpt_df.drop(cpt_df.index[len(cpt_df)-1])

		counts = cpt_df.groupby("ResponseType").count()

		correctrejections = cpt_df["Response"].isnull().sum()

		comission = "comission" in counts.index

		omission = "omission" in counts.index

		hit = "hit" in counts.index

		if omission == False:
			omission = 0
		else:
			omission = counts.loc["omission"].values[0]


		if comission == False:
			comission = 0
		else:
			comission = counts.loc["comission"].values[0]

		if hit == False: 
			hit = 0
		else:
			hit = counts.loc["hit"].values[0]

		hitRate = hit / (hit + omission)

		falseRate = (comission) / (comission + correctrejections)

		numStim  = int(len(cpt_df))

		filter_series = cpt_df[cpt_df["ResponseTime"] != 0]

		MeanHitRT = filter_series["ResponseTime"].mean() 

		RTSD = filter_series["ResponseTime"].std()

		Dprime = norm.ppf(hitRate) - norm.ppf(falseRate)

		Beta = -0.5 * Dprime * (norm.ppf(hitRate) + norm.ppf(falseRate))
		 
		completed = None

		date = now.strftime("%Y-%m-%d")

		summary = {"date": [date], "numStimuli": [numStim] , "hit" : [hit], "Comissions": [comission], "Omissions" : [omission],   "MeanHitRT" : [MeanHitRT], "RTSD": [RTSD], "Dprime" : [Dprime], "Beta" : [Beta], "Completed" : [completed]}

		out_df = pd.DataFrame(data=summary)
	
		if(out_df["Dprime"].loc[0] == float('Inf')):
			out_df["Dprime"].loc[0] = 6.18046


		if(out_df["Dprime"].loc[0] == 6.18046):
			out_df["Beta"].loc[0] = 0

		if(out_df["numStimuli"].loc[0] != 200):
			out_df["Completed"].loc[0] = False

		# print(out_df["Dprime"] == "inf")

		out = out_df.to_dict(orient='records')
		out[0]['record_id'] = str(record) 
		out_json = json.dumps(out)


		data_import = {
		    'token': 'Place p2 token here.........',
		    'content': 'record',
		    'format': 'json',
		    'type': 'flat',
		    'overwriteBehavior': 'normal',
		    'forceAutoNumber': 'false',
		    'data': out_json,
		    'returnContent': 'count',
		    'returnFormat': 'json',
		}

		# r = post("https://redcap.duke.edu/redcap/api/", data_import)

		# print(r)
		
		# print(r.status_code)

		out_df.to_csv("cpt_{}_{}".format(record, date), index = False)



app = wx.App()
frame = Frame(None, 'ACE Scoring')
app.MainLoop()






# out.to_csv("{}".format(date), index = False)


