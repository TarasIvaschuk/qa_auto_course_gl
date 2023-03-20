import sys
import os

sys.path.append('../src/config')

from providers.CSVProvider import CSVProvider
from providers.EnvProvider import EnvProvider
from providers.JsonProvider import JsonProvider



class Config:
    # class props
    default_env = "dev"

    def __init__(self):
        self._d = {}

        target = os.environ.get('TARGET')
        if target is None:
            target = Config.default_env

        json_path = f"../src/config/env_configs/{target}.json"
        self.providers = [
            JsonProvider(json_path),
            CSVProvider(),
            EnvProvider(),
        ]

        # register the key what we want to use in the test
        self.register('BASE_URL')
        self.register("URL_BASE_API")

    def register(self, k):

        for p in self.providers:
            v = p.getVal(k)
            if v is not None:
                self._d[k] = v
        if self._d.get(k, None) is None:
            raise Exception('The key is not found in config files')
        print(f'{k}:{self._d.get(k)} is successfully registered!')

    def set(self, k, v):
        self._d[k] = v

    def get(self, k):
        v = self._d.get(k, None)
        if v is None:
            raise Exception('Varible is not registered in config')
        return v


# Config()
