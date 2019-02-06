import os
import logging
import platform

WINDOWS = (platform.system().lower() == 'windows') or (os.name == 'nt')
APP_NAME = 'testapp'
ENVIRONMENT_CONFIG_PATH = 'TEST_APP_CONFIG_PATH'
USER_HOME_DIR = os.path.expanduser('~')
TEST_APP_ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DEFAULT_CONFIG_PATH = [
    './',
    '~/',
    '~/.{}'.format(APP_NAME),
    '/etc/{}'.format(APP_NAME),
    TEST_APP_ROOT_DIR,
] if not WINDOWS else [
    '.\\',
    os.path.realpath(os.path.join(USER_HOME_DIR, '.{}'.format(APP_NAME))),
    os.path.realpath(os.path.join(os.getenv('APPDATA'), APP_NAME)),
    TEST_APP_ROOT_DIR,
]


class Config:
    def __init__(self, config_file=None):
        self.config_file = config_file or '{}.yaml'.format(APP_NAME)
        self.config_paths = self.init_env_config_path()

    @staticmethod
    def init_env_config_path():
        _config_path_env = [
            x for x in os.getenv(ENVIRONMENT_CONFIG_PATH, '').split(';') if x
        ]
        result = list(DEFAULT_CONFIG_PATH)
        if WINDOWS:
            result.append(os.path.realpath(
                '{}\\'.format(Config.get_windows_system_disk())
            ))
        for config_path_env in _config_path_env:
            config_path_tmp = os.path.dirname(
                config_path_env) if os.path.isfile(
                config_path_env) else config_path_env
            if config_path_tmp in result:
                result.remove(config_path_tmp)
            result.insert(0, config_path_tmp)
        return result

    @staticmethod
    def get_verbosity_level(level=None, text=False):
        levels = (
            ('critical', logging.CRITICAL, False),
            ('error', logging.ERROR, False),
            ('warning', logging.WARNING, False),
            ('info', logging.INFO, True),
            ('debug', logging.DEBUG, False),
        )
        if level is None:
            return ', '.join(x[0] for x in levels)

        if level == 'console':
            level = 'debug'

        default = None
        for x in levels:
            if isinstance(level, str):
                if x[0] == level.lower():
                    return x[1]
            elif x[2]:
                default = x[0] if text else x[1]
                break

        return default

    @staticmethod
    def get_windows_system_disk():
        result = os.getenv('SystemDrive', '')
        if not result:
            try:
                _temp = __import__('win32api', globals(), locals(),
                                   ['GetSystemDirectory'], 0)
                result = _temp.GetSystemDirectory()
                if result:
                    result = os.path.splitdrive(result)[0]
            except Exception:
                pass
        if not result:
            raise EnvironmentError('Operation system is not Windows')
        return result
