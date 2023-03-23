import os
import csv

filePath = os.path.realpath(__file__)
currentDir = os.path.dirname(filePath)


class CSVProvider:
    def __init__(self):
        self._f = f'{currentDir}/data.csv'
        self._d = {}
        self._createDict()

    def _createDict(self):
        with open(self._f) as f:
            csv.register_dialect(
                'custom',
                delimiter=",",
                quotechar="\"",
                skipinitialspace=True,
                escapechar="\\"
            )
            text = csv.reader(f, dialect="custom")
            # skip the headers
            next(text)
            for row in text:
                k, v = row
                self._d[k] = v

    def getVal(self, k):
        return self._d.get(k, None)
