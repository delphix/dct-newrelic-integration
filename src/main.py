#
# Copyright (c) 2022 by Delphix. All rights reserved.
#

"""
This python script takes care of sending the data
from DCT APIs for a set of components to New relic.
It can be run using Python 3.8
"""
import datetime
import os.path
import sys
import time

import newrelic_telemetry_sdk.client
import requests
import logging
import urllib3
import configparser
import tenacity

from newrelic_telemetry_sdk import Event, EventClient
from urllib3.exceptions import InsecureRequestWarning
from src import VERSION

urllib3.disable_warnings(InsecureRequestWarning)

config_file = "dct_nr_config.ini"
config = configparser.ConfigParser()

if not os.path.exists(config_file):
    raise Exception("Config file is required. "
                    "Please add dct_nr_config.ini in the current directory")

config.read_file(open("dct_nr_config.ini"))
keys = config['API_KEYS']
dct = config['DCT']
config_log_level = config['LOGGING']['LEVEL']
INTERVAL = int(config['INTERVAL']['seconds'])

formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging_levels = {
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
    'WARN': logging.WARNING,
    'ERROR': logging.ERROR
}
logging.basicConfig(level=logging_levels[config_log_level], format=formatter)


DCT_URL = dct['DCT_HOST_URL']
DCT_API_URL = f'https://{DCT_URL}/v2/'
DLPX_TYPES = [i.strip() for i in config['COMPONENTS']['monitor'].split(',')]

# Request Headers ...
req_headers = {
    'Authorization': keys['DCT_API_KEY']  # noqa
}

# Python session, also handles the cookies ...
session = requests.session()


@tenacity.retry(
    retry=tenacity.retry_if_exception_type(
        newrelic_telemetry_sdk.client.HTTPError
    ),
    stop=tenacity.stop_after_attempt(5),
    wait=tenacity.wait_fixed(5),
    before_sleep=tenacity.before_sleep_log(logging, logging.INFO),
)
def send_event(event):
    logging.debug(event)
    event_client = EventClient(keys['NEW_RELIC_INSERT_KEY'])
    response = event_client.send(event)
    response.raise_for_status()
    logging.debug("Event sent successfully!\n")


@tenacity.retry(
    retry=tenacity.retry_if_exception_type(
        AssertionError
    ),
    stop=tenacity.stop_after_attempt(5),
    wait=tenacity.wait_fixed(5),
    before_sleep=tenacity.before_sleep_log(logging, logging.DEBUG),
)
def get_data_from_dct(component):
    response = requests.get(DCT_API_URL + component,
                            headers=req_headers, verify=False)
    assert response.status_code == 200
    response_json = response.json()
    return response_json


def push_data():
    while True:
        logging.info('*' * 70)
        logging.info("Pushing Data to New Relic at %s",
                     datetime.datetime.now())
        logging.info('*' * 70)
        for i in DLPX_TYPES:
            response_json = get_data_from_dct(i)

            NEWRELIC_TYPE = "Delphix " + str(i).split('/')[-1]
            logging.info("Sending Data for %s \n", NEWRELIC_TYPE)
            for line in response_json['items']:
                event = Event(
                    NEWRELIC_TYPE, line
                )
                send_event(event)

        logging.info(f"Sleeping for %s seconds before pushing again", INTERVAL)
        logging.info('-' * 70)
        time.sleep(INTERVAL)


def run():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--version":
            print(VERSION)
    else:
        logging.info('#' * 70)
        logging.info("Staring to Push Data to New Relic")
        logging.info('#' * 70)
        logging.debug(f"{DCT_URL=}")
        logging.debug(f"{DLPX_TYPES=}")
        logging.debug(f"{req_headers=}")
        logging.debug(f"NEW_RELIC_INSERT_KEY = {keys['NEW_RELIC_INSERT_KEY']}")
        push_data()


if __name__ == '__main__':
    run()
