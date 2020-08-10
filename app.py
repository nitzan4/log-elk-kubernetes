#!/usr/bin/env python3

import datetime
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
import atexit
from flask import Flask

app = Flask(__name__)

@app.route('/')
def app_main():
    return 'works'

def writeTimeToLogFile():
    logging.basicConfig(filename='test_logs.log', level=logging.DEBUG)
    logging.info(datetime.datetime.now())

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(id ='Test', func = writeTimeToLogFile, trigger = IntervalTrigger(seconds = 5))
    atexit.register(lambda: scheduler.shutdown())
    app.run(host='0.0.0.0', port='5000')
