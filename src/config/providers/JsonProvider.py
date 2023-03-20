import json

class JsonProvider:
  def __init__(self,json_path):
    self._d = {}
    with open(json_path) as json_file:
      self._d = json.load(json_file)
  
  def getVal(self,k):
    return self._d.get(k,None)