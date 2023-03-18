from providers.CSVProvider import CSVProvider


class Config:
    def __init__(self):
        self._d = {}
        # do actual register what we want to use in the test
        self.register('BASE_URL')
        pass

    def register(self, k):
        print('register')
        # if it is not in provider list throw
        #
        # an error
        keys = CSVProvider().getData()

        if k not in keys:
            raise Exception('No key provided')

        # otherwise add a key to dictionary
        self._d[k] = keys[k]

    def set(self, k, v):
        print('set')
        self._d[k] = v

    def get(self, k):
        print('get')
        return self._d.get(k, None)


Config().get('BASE_URL')
