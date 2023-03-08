import os
import configparser
import yaml


ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "settings.ini")
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")


class FileRead:
    def __int__(self):
        self.ini_path=ini_path
        self.data_path=data_path
    def read_data(self):
        f = open(data_path, encoding="utf8")
        data = yaml.safe_load(f)
        return data

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(ini_path,encoding='utf8')
        return config

base_data = FileRead()