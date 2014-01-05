#!/usr/bin/env python
import datetime
import redis
import urllib2
import sendgrid
import MySQLdb
import keen
import json
import os
import re
import ConfigParser
from collections import defaultdict

data_source = "http://api.bitcoincharts.com/v1/markets.json"

def get_config(localfile="/home/ubuntu/btc/config.cfg"):
    openfile = localfile
    config = defaultdict(dict)
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
red = redis.StrictRedis(**config["redis"])

btc_market = urllib2.urlopen(config["btc"]["market"])
btc_market = json.loads(btc_market.read())
btc_json = {}
for btc in btc_market:
  btc_json[btc["symbol"]] = btc

mtgox = btc_json["mtgoxUSD"]
client = keen.KeenClient(**config["keen"])
client.add_event("btc-market", btc_json)

if red.get("mtgoxHigh"):
    mtgoxHigh = float(red.get("mtgoxHigh"))
else:
    mtgoxHigh = 0.0
if mtgox["close"] > mtgoxHigh:
    red.set("mtgoxHigh", mtgox["close"])
    mtgoxHigh = mtgox["close"]

trailing = mtgox["close"] / mtgoxHigh - 1

print datetime.datetime.now(), mtgox["close"], mtgoxHigh, 100*trailing, -config["global"]["limit"]

if 100*trailing <= -config["global"]["limit"] and not red.get("mtgoxIGNORE"):
    red.set("mtgoxIGNORE", True)
    red.expire("mtgoxIGNORE", config["global"]["pause"])

    message_content = "BTC mtgoxUSD {close:0.1f}/{high:0.1f} - Trail {trail:0.1f}%".format(close=mtgox["close"], high=mtgoxHigh, trail=trailing*100)

    s = sendgrid.Sendgrid(config["sendgrid"]["user"], config["sendgrid"]["passwd"])
    message = sendgrid.Message(
      "btc@aler.ts",
      " ", 
      message_content)
    message.add_to("2489101406@messaging.sprintpcs.com", "Ron Lai")
    message.add_to("6175045270@messaging.sprintpcs.com", "Sonya Lai")

    s.web.send(message)

