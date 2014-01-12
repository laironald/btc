from collections import defaultdict
import ConfigParser
import os
import re
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from schema import *

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

config = get_config()


class DB():
    engine = None
    _session = None
    echo = None
    database = None

    def __init__(self):
        self.echo = config.get("global").get("echo")
        self.database = config.get("global").get("database")
        self.refresh_connection()
        Base.metadata.create_all(self.engine, checkfirst=True)

    def commit(self):
        """
        Convenience method to call commit
        """
        self.session().commit()

    def session(self):
        try:
            self._session.execute('select 1')
        except:
            print 'refreshing connection'
            self.refresh_connection()
        return self._session

    def refresh_connection(self):
        if self.database == "mysql":
            self.engine = create_engine('mysql://{user}:{password}@{host}:3306/{database}'.format(**config.get(self.database)), echo=self.echo, pool_recycle=3600)
        else:
            self.engine = create_engine('sqlite:///{path}/{database}'.format(**config.get(self.database)), echo=self.echo)
        Session = sessionmaker(bind=self.engine)
        self._session = Session()

