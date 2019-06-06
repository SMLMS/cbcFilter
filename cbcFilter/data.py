# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:37:29 2019

@author: malkusch
"""
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

class SMLM_dataObject:
    def __init__(self, fileName = ""):
        self._fileName = fileName
        self._baseName = ""
        self._folderName = ""
        self._dataFrame = pd.DataFrame()
        self._filteredDataFrame = pd.DataFrame()
        
        
    @property
    def fileName(self):
        print("returning fileName")
        return self._fileName
    
    @fileName.setter
    def fileName(self, value):
        print("set fileName")
        self._fileName = value
        
    @property
    def baseName(self):
        print("return baseName")
        return self._baseName
    
    @property
    def folderName(self):
        print("return folderName")
        return self._folderName
    
    @property
    def dataFrame(self):
        return self._dataFrame
    
    @property
    def filteredDataFrame(self):
        return self._filteredDataFrame
    
    
    def updateNames(self):
        if (len(self._fileName)>0):
            self._folderName = os.path.dirname(self._fileName)
            self._baseName = os.path.basename(self._fileName)[:-4]
        else:
            print("No fileName selected!")
    
    def browseFile(self):
        root = tk.Tk()
        root.withdraw()
        root.update()
        root.name = askopenfilename(title="import Lama localization file", filetypes=(("tab separated files", "*.txt"),
                                                                                              ("All files", "*.*") ))
        self._fileName = root.name
        root.update()
        root.destroy()
        
    def importData(self):
        data = np.loadtxt(self._fileName, comments='#')
        self._dataFrame = pd.DataFrame(data=data[:,:],# values
                                       index=np.arange(0, np.shape(data)[0]),
                                       columns=['x[nm]', 'y[nm]', 't[frame]', 'cbc[a.u.]'])
    
    def viewData(self):
        print(self._dataFrame.head())
        
    def viewFilteredData(self):
        print(self._filteredDataFrame.head())
        
    def filterDataFrame(self,
                        minX=0, maxX=1,
                        minY=0, maxY=1,
                        minT=0, maxT=1,
                        minCbc=-1.0, maxCbc=1.0):
        idx1 = self._dataFrame['x[nm]'] >= minX
        idx2 = self._dataFrame['x[nm]'] <= maxX
        idx3 = self._dataFrame['y[nm]'] >= minY
        idx4 = self._dataFrame['y[nm]'] <= maxY
        idx5 = self._dataFrame['t[frame]'] >= minT
        idx6 = self._dataFrame['t[frame]'] <= maxT
        idx7 = self._dataFrame['cbc[a.u.]'] >= minCbc
        idx8 = self._dataFrame['cbc[a.u.]'] <= maxCbc
        self._filteredDataFrame = self._dataFrame[idx1 &
                                                  idx2 &
                                                  idx3 &
                                                  idx4 &
                                                  idx5 &
                                                  idx6 &
                                                  idx7 &
                                                  idx8]
        
    def plotFilteredData(self):
        self._filteredDataFrame.hist(column = 'cbc[a.u.]',
                                     bins = np.arange(-1.0, 1.05, 0.05)
                                     )
        plt.show()
          
    def saveFilteredDataFrame(self, prefix='filtered'):
        outName = str('%s\%s_%s%s' %(self._folderName, self._baseName, prefix, '.txt'))
        f = open(outName, 'w')
        f.write('# localization roi file (Malk format)\n#')
        self._filteredDataFrame.to_csv(f, index=False, header=True, sep='\t',line_terminator='\n', quoting=csv.QUOTE_NONNUMERIC)
        f.close
        print("Filtered dataset written to: %s" % (outName))