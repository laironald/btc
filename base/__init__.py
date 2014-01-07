from collections import defaultdict
import ConfigParser
import os
import re
import sys


# function to parse config.ini
def get_config(localfile="config.ini"):
    config = defaultdict(dict)
    openfile = "{0}/config.ini".format(os.path.dirname(os.path.realpath(__file__)))

    if os.path.isfile(openfile):
        cfg = ConfigParser.ConfigParser()
        cfg.read(openfile)
        for s in cfg.sections():
            for k, v in cfg.items(s):
                dec = re.compile(r'^\d+(\.\d+)?$')
                if v in ("True", "False") or v.isdigit() or dec.match(v):
                    v = eval(v)
                config[s][k] = v

    return config
