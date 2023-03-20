import os

class EnvProvider:
  def getVal(self,k):
    return os.environ.get(k,None)