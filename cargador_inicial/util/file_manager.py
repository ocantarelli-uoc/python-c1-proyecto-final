"""It imports os library for tasks in relation to os routines such as for checking if path exists,
subprocesses with fork (not used in this application), file descriptors for managing files,sockets... functions for execute commands...
"""
import os
#It import pandas library
import pandas as pd
#Class that represents a csv file manager
class CSVFileManager:
  def __init__(self,path: str):
    self.path = path
  #method that its responsibility it's to read from a csv file to Pandas DataFrame
  def read(self) -> pd.DataFrame:
    return pd.read_csv(self.path)  
  #method that its responsibility it's to write a Pandas DataFrame to a csv file
  def write(self,dataFrame:pd.DataFrame,mode:str):
    #It checks if mode it's 'a' referring to append mode
    if mode == 'a':
      #It checks if file doesn't exists, it adds header
      if not os.path.exists(self.path):
        dataFrame.to_csv(self.path, mode=mode, header=True,index=False,sep=";")
      else:
        #Otherwise, if file it already exists, it doesn't add header again
        dataFrame.to_csv(self.path, mode=mode, header=False,index=False,sep=";")
    else:
      #If mode it's not 'a', it adds header
      dataFrame.to_csv(self.path, mode=mode, header=True,index=False,sep=";")