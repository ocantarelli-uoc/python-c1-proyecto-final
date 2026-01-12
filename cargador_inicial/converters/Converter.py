#It imports for abstract and abstract methods
from abc import ABC, abstractmethod
#It import pandas library
import pandas as pd
#Class that it represents a converter
class Converter(ABC):
  #method that its responsibility it's to convert a dataframe to list of objects
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass
  #method that its responsibility it's to print every list's object
  def print(self, objects):
    for item in objects:
      print(item.describe())