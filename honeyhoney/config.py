import yaml

import logging

class Config(object):
    @classmethod
    def from_path(cls, path):
        return cls.from_file(
            open(path)
        )
    
    @classmethod
    def from_file(cls, f):
        return cls(
            yaml.safe_load(f)
        )
        
    def __init__(self, config):
        self._config = config
        
    def __getitem__(self, key):
        return self._config[key]

def load_config(opts):
    return Config.from_path(opts.config)
