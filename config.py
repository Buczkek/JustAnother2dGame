import sys, time

OPTIONS = {
    "": "",
}


class Config:  # TODO check for bugs
    def __init__(self, path="config.cfg"):
        self._path = path
        self._settings = {}
        if not self.check_existence():
            self.config_creator()
            self.load_default()
        elif not self.config_import():
            self.load_default()
        self.config_import()
        if len(self._settings) < len(OPTIONS):
            self.fill_settings()

    def check_existence(self):
        try:
            file = open(self._path, 'r')
            file.readline()
            file.close()
            return True
        except FileNotFoundError:
            return False

    def config_creator(self):
        try:
            with open(self._path, 'w') as file:
                for (option, setting) in OPTIONS:
                    file.write(f"{option}={setting}\n")
        except:
            pass

    def load_default(self):
        for (option, setting) in OPTIONS:
            self._settings[option] = setting

    def config_import(self):
        try:
            with open(self._path, 'r') as config_file:
                for line in config_file.readline(len(OPTIONS)):
                    option, setting = line.strip().split('=')
                    if option in OPTIONS:
                        self._settings[option] = setting
            return True
        except:
            return False

    def config_save(self, path=""):
        if not path:
            path = self._path
        try:
            with open(path, 'w') as config_file:
                for (option, setting) in self._settings:
                    config_file.write(f"{option}={setting}\n")
        except:
            pass

    def get_setting(self, setting):
        return self._settings[setting]

    def fill_settings(self):
        for (option, setting) in OPTIONS:
            if option not in self._settings:
                self._settings[option] = setting
