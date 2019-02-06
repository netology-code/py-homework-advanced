import logging
from helpers.config import Config, APP_NAME


class App:
    def __init__(self, level='console'):
        self._log = logging.getLogger(APP_NAME)
        level = Config.get_verbosity_level(level)
        if level:
            self._log.setLevel(level)
        self.config = Config()

    def run(self):
        print(APP_NAME)
        print(self.config.config_file)
        print(self.config.config_paths)


if __name__ == '__main__':
    App().run()
