import os
import yaml
from pathlib import Path
import random


class ReadYaml:
    def read_config_yaml(self, key):
        with open(Path(__file__).resolve().parent.parent / 'config' / 'config.yml', mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]

    def read_data_yaml(self, file_yml):
        with open(Path(__file__).resolve().parent.parent / 'data' / file_yml, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value
