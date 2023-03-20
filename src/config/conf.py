import sys

sys.path.append('..\src\config')

from providers.EnvProvider import EnvProvider
from providers.CSVProvider import CSVProvider

class Config:
    def __init__(self):
        self._d = {}
        # register the key what we want to use in the test
        self.register('BASE_URL')
        

    def register(self, k):
        self.providers = [
            CSVProvider(),
            EnvProvider(),
        ]
        for p in self.providers:
            v = p.getVal(k)
            if v is not None:
                self._d[k] = v
        if self._d.get(k,None) is None:
            raise Exception ('The key is not found in config files')
        print(f'{k} is successfully registered!')


    def set(self, k, v):
        self._d[k] = v

    def get(self, k):
        v =  self._d.get(k, None)
        if v is None:
            raise Exception('Varible is not registered in config')
        return v


# Config()
