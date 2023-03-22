import sys
import os

filePath = os.path.realpath(__file__)
configDir = os.path.dirname(filePath)
srcDir = os.path.dirname(configDir)
rootDir = os.path.dirname(srcDir)
envConfigsDir = f'{configDir}/env_configs'
sys.path.append(rootDir)


from src.config.providers.CSVProvider import CSVProvider
from src.config.providers.EnvProvider import EnvProvider
from src.config.providers.JsonProvider import JsonProvider



class Config:
    # class props
    default_env = "dev"

    def __init__(self):
        self._d = {}

        target = os.environ.get('TARGET')
        if target is None:
            target = Config.default_env

        json_path = f"{envConfigsDir}/{target}.json"
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
