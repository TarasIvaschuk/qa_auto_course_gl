import os 

filePath = os.path.realpath(__file__)
currentDir = os.path.dirname(filePath)

class CSVProvider:
    def __init__(self):
        # todo 
        self._f = f'{currentDir}/data.csv'
        self._separator = ","
        self._delim = "\""
        self._d = {}
        self._createDict()

    def _processRow(self, r):
        k,v = [
            c.strip().strip(self._delim)
            for c in r.split(self._separator)
        ]
        
        return k,v

    def _createDict(self):
        with open(self._f) as f:
            # skip the header
            next(f)
            for row in f:
                k,v = self._processRow(row)
                self._d[k] = v

    def  getVal(self,k):
        return self._d.get(k,None)