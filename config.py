class Config:
    def __init__(self, path="config.cfg"):
        self._path = path
        if not self.check_existence():
            self.config_creator()
        else:
            self.config_import()
        # TODO save
        # TODO config fill default

    def check_existence(self):
        try:
            file = open(self._path, 'r')
            file.readline()
            file.close()
            return True
        except FileNotFoundError:
            return False

    def config_creator(self):  # TODO
        pass

    def config_import(self):  # TODO
        pass

    def config_save(self):  # TODO
        pass
