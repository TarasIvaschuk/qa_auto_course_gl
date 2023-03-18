class CSVProvider:
    def __init__(self):
        self._f = 'C:/Users/taras.ivashchuk/qa_auto/config/providers/data.csv'
        self._separator = ","
        self._delim = "\""
        self._d = {}

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

    def  getData(self):
        if not len(self._d):
            self._createDict()
        return self._d