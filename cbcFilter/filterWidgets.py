#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:44:22 2019

@author: malkusch
"""

from ipywidgets import widgets
from IPython.display import clear_output
import tkinter as tk
from tkinter.filedialog import askopenfilename

class Widgets:
    def __init__(self):
        print("Widgets initialized")
        self.style = {'description_width': 'initial'}
        self.fileName = ""
        self.loadButton = self.createButton(desc = 'load')
        self.min_x_filter_text = self.createTextInt(val=0, minVal=0, maxVal=45000, stepSize=1, desc="min x [nm]")
        self.max_x_filter_text = self.createTextInt(val=45000, minVal=0, maxVal=45000, stepSize=1, desc="max x [nm]")
        self.x_filter = widgets.HBox((self.min_x_filter_text, self.max_x_filter_text))
        self.min_y_filter_text = self.createTextInt(val=0, minVal=0, maxVal=81000, stepSize=1, desc="min y [nm]")
        self.max_y_filter_text = self.createTextInt(val=81000, minVal=0, maxVal=81000, stepSize=1, desc="max y [nm]")
        self.y_filter = widgets.HBox((self.min_y_filter_text, self.max_y_filter_text))
        self.min_t_filter_text = self.createTextInt(val=0, minVal=0, maxVal=1000000, stepSize=1, desc="min time [frame]")
        self.max_t_filter_text = self.createTextInt(val=1000000, minVal=0, maxVal=1000000, stepSize=1, desc="max time [frame]")
        self.t_filter = widgets.HBox((self.min_t_filter_text, self.max_t_filter_text))
        self.min_cbc_filter_text = self.createTextFloat(val=-1.0, minVal=-1.0, maxVal=1.0, stepSize=0.01, desc="min cbc [a.u.]")
        self.max_cbc_filter_text = self.createTextFloat(val=1.0, minVal=-1.0, maxVal=1.0, stepSize=0.01, desc="max cbc [a.u.]")
        self.cbc_filter = widgets.HBox((self.min_cbc_filter_text, self.max_cbc_filter_text))
        self.filterButton = self.createButton(desc='Filter Lama data')
        self.plotButton = self.createButton(desc = 'plot filtered Lama data')
        self.outFilePrefix = self.createTextStr(value='filtered', desc='file prefix', placeHolder = 'filtered')
        self.saveButton = self.createButton(desc = 'save filtered Lama data')
        
        
    def createTextStr(self, value='', desc='path to file', placeHolder = 'enter a string'):
        text = widgets.Text(
                value=str(value),
                placeholder=str(placeHolder),
                description=str(desc),
                disabled=False,
                style = self.style
                )
        return text
        
    def createButton(self, desc = 'browse'):
        button=widgets.Button(
                description=str(desc),
                disabled=False,
                button_style='', # 'success', 'info', 'warning', 'danger' or ''
                tooltip='Click me',
                icon='check',
                style = self.style
                )
        return button
        
    def createTextInt(self, val=0.0, minVal=0, maxVal=100, stepSize=1, desc="d"):
        text = widgets.BoundedIntText(
                value=int(val),
                min=int(minVal),
                max=int(maxVal),
                step=int(stepSize),
                description=str(desc),
                disabled=False,
                style = self.style
                )
        return text
        
    def createTextFloat(self, val=0.0, minVal=0.0, maxVal=1.0, stepSize=0.001, desc="d"):
        text = widgets.BoundedFloatText(
                value=float(val),
                min=float(minVal),
                max=float(maxVal),
                step=float(stepSize),
                description=str(desc),
                disabled=False,
                style = self.style
                )
        return text
    
    def createSliderFloat(self, val=0.0, minVal=0.0, maxVal=1.0, stepSize=0.001, ori='horizontal', desc="d"):
        slider = widgets.FloatSlider(
                value=float(val),
                min=float(minVal),
                max=float(maxVal),
                step=float(stepSize),
                description=str(desc),
                disabled=False,
                continuous_update=False,
                orientation=ori,
                readout=True,
                readout_format='.3f',
                style = self.style
                )
        return slider
    
    def createLink(self, a, b):
        link = widgets.jslink((a, 'value'), (b, 'value'))
        return link
    
    def proofValidity(self, val=False, desc="valid"):
        validity= widgets.Valid(
                value=val,
                description=str(desc),
                style = self.style
                )
        return validity
    
    def createSelector(self, opt = ['least squares', 'maximum likelihood'],val = 'least squares', rows=1, desc = 'optimizer'):
        selector = widgets.Select(
                options=opt,
                value=val,
                rows= rows,
                description=desc,
                disabled=False
                )
        return selector
    
    def createDropDown(self, opt=[0, 1, 2], val = 0, desc='Number:'):
        selector = widgets.Dropdown(
                options=opt,
                value=val,
                description=desc,
                disabled=False,
                )
        return selector


    
    def browseFile(self, b):
        root = tk.Tk()
        root.withdraw()
        root.update()
        root.name = askopenfilename(title="import blinking histogram", filetypes=(("text files", "*.txt"),
                                       ("All files", "*.*") ))
        self.fileName = root.name
        self.pathText.value = self.fileName
        root.update()
        root.destroy()
        
    def updateFileName(self, change):
        self.fileName = self.pathText.value
        
    def clearOutput(self):
        clear_output()