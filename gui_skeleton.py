import os
import urllib
from requests import post
import urllib.request
import wx
import sys
import requests
import urllib
from requests import post
import pandas as pd
import json
import os.path
import csv
import numpy as np
import datetime




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

        # project_name = [Project(0, "Personal Sandbox", ""), Project(1, "ACE Sandbox", "")]
        
        
        # sas_scoring = [Scoring(0, "CBCL", "cbcl_ages_155", "CBCLScoring.sas")]


        # visit_type = [Visit(0, "Visit 1" , "visit_1_arm_1"), Visit(1, "Visit 2", "visit_1_arm_2")]

#Begin the creation of widgets
        # self.cb_project = wx.ComboBox(self.panel, -1, value="Select Project", style=wx.CB_DROPDOWN) 
        # self.widgetProject(self.cb_project, project_name)
        
        # self.cb_scoring = wx.ComboBox(self.panel, -1, value="Select Scoring", size=[125,20])
        # self.widgetScoring(self.cb_scoring, sas_scoring)
        

        # self.cb_visit = wx.ComboBox(self.panel, -1, value="Select Visit", size=[125,20])
        # self.widgetVisit(self.cb_visit, visit_type)
        

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Duke ACE Scoring v0.1')
        

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        

        # self.btn = wx.Button(self.panel, -1, "Record ID", pos=[1,1])
        # self.Bind(wx.EVT_BUTTON, self.GetRecordID, self.btn)
        


        self.btnexecute = wx.Button(self.panel, -1, "Execute", pos=[1,1])
        self.Bind(wx.EVT_BUTTON, self.run, self.btnexecute)

        # self.reponse = wx.TextCtrl(self.panel, -1, pos=[1,40], size=[342,130], style=
        #     wx.TE_MULTILINE)

        self.log = wx.TextCtrl(self.panel, wx.ID_ANY, size=(380,100),
                          style = wx.TE_MULTILINE|wx.TE_READONLY)

        
#-----------Begin the creation of the sizer and layout of the GUI--------------#


        sizer = wx.BoxSizer(wx.VERTICAL)

        # top_flags = wx.SizerFlags().Expand().Border(wx.ALL, 1).Proportion(0)


        # topsizer = wx.BoxSizer(wx.HORIZONTAL)
        # # topsizer.Add(self.cb_project, top_flags)
        # # topsizer.Add(self.cb_scoring, top_flags)
        # # topsizer.Add(self.cb_visit, top_flags)

        
        # sizer.Add(topsizer)

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


    # def widgetProject(self, widget, objects):
    #     """"""
    #     for obj in objects:
    #         widget.Append(obj.project, obj)
    #     widget.Bind(wx.EVT_COMBOBOX, self.onProjectSelect)
    
    # def widgetScoring(self, widget, objects):
    #     """"""
    #     for obj in objects:
    #         widget.Append(obj.scoring_package, obj)
    #     widget.Bind(wx.EVT_COMBOBOX, self.onScoringSelect)

    # def widgetVisit(self, widget, objects):
    #     """"""
    #     for obj in objects:
    #         widget.Append(obj.visit, obj)
    #     widget.Bind(wx.EVT_COMBOBOX, self.onVisitSelect)


    # def onScoringSelect(self, event):
    #     obj = self.cb_scoring.GetClientData(self.cb_scoring.GetSelection())
    #     return obj.scoring_package, obj.intrument, obj.scoring_path


    # def onProjectSelect(self, event):
    #     	obj = self.cb_project.GetClientData(self.cb_project.GetSelection())
    #     	return obj.token, obj.project



    # def onVisitSelect(self, event):
    #     obj = self.cb_visit.GetClientData(self.cb_visit.GetSelection())
    #     return obj.visit, obj.visit_name




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


#-----Initialize the pull from RedCAP using the user selected attributes------#


    def run(self, event):
        print("Executing...")
        record = self.GetRecordID(event)
        # token, project_name = self.onProjectSelect(event)
        # scoring_package, instrument, scoring_path = self.onScoringSelect(event)
        # visit, visit_name = self.onVisitSelect(event)
        

app = wx.App()
frame = Frame(None, 'ACE Scoring')
app.MainLoop()






        data = {
            'token': str(token),
            'content': 'record',
            'format': 'csv',
            'type': 'flat',
            'records[0]': str(record),
            'forms[0]': str(instrument),
            'events[0]': str(visit_name),
            'rawOrLabel': 'raw',
            'rawOrLabelHeaders': 'raw',
            'exportCheckboxLabel': 'false',
            'exportSurveyFields': 'false',
            'exportDataAccessGroups': 'false',
            'returnFormat': 'json'
        }


        record_id = getData(records)

        log_df = pandas.DataFrame(columns=['Record_ID', "Second Entry Exist", 'Variables Wrong', 'Entries are Equal'], index=range(len(record_id['record_id'])))

        for i in range(0,len(record_id['record_id'])):
              ids = str(record_id['record_id'].values[i])
              log_df['Record_ID'].loc[i] = ids
              data = {
                  'token': '',
                  'content': 'record',
                  'format': 'json',
                  'type': 'flat',
                  'records[0]': ids ,
                  'forms[0]': 'cbcl_ages_155',
                  'rawOrLabel': 'raw',
                  'rawOrLabelHeaders': 'raw',
                  'exportCheckboxLabel': 'false',
                  'exportSurveyFields': 'false',
                  'exportDataAccessGroups': 'false',
                  'returnFormat': 'json'
              }
              entry = getData(data)
              try:
                    entry1 = entry.iloc[[0]]
                    entry2 = entry.iloc[[1]]
                    entry1.index = ['x']
                    entry2.index = ['x']
                    ne = (entry1 != entry2).any(1)
                    ne_stacked = (entry1 != entry2).stack()
                    compare = ne_stacked[ne_stacked]
                    if(len(compare) == 0):
                          log_df['Entries are Equal'].loc[i] = "Yes"
                    else:
                          log_df['Entries are Equal'].loc[i] = "No"
                          flagged = ""
                          for flags in compare.index:
                                flagged=flagged +" " + str(flags[1])
                                print(flags[1])
                                # flagged.append(flags[1])
                                log_df['Variables Wrong'].loc[i] = flagged
                    log_df["Second Entry Exist"].loc[i] = "Yes" 
              except IndexError:
                    log_df["Second Entry Exist"].loc[i] = "No"



app = wx.App()
frame = Frame(None, 'ACE Scoring')
app.MainLoop()

