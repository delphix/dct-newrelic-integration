import os
import requests
import json
import sys
import time
from newrelic_telemetry_sdk import Event, EventClient

##
# Uncomment the following lines to ignore SSL Warnings
##
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

DLPX_TYPES= ["management/engines","sources","dsources","vdbs","environments"]

#
# Required Input Parameters
#
try:
	DCT_URL = os.environ["DCT_URL"] # Example: https://localhost:443
	DCT_KEY = os.environ['DCT_KEY'] # Example: 'apk 2.bnQDDx46Z4CDlIShLw2ZHElWLyKtsmZaBjbQPjui8LcQ3TELbkdEbQJSki6vmwLf'
	NEW_RELIC_KEY = os.environ['NEW_RELIC_KEY'] # Generated "INGEST - LICENSE" Key from https://one.newrelic.com/admin-portal/api-keys/home
except:
	print ("[Error] One or more of the DCT_URL, DCT_KEY, OR NEW_RELIC_KEY environment variables are empty. Ensure all values are specified.")
	exit()

#
# Python session, also handles the cookies ...
#
session = requests.session()

#
# Request Headers ...
#
req_headers = {
	'Authorization': DCT_KEY
}

for i in DLPX_TYPES:
	NEWRELIC_TYPE = "Delphix " + str(i)	
	print ("Uploading events: " + NEWRELIC_TYPE)
	response = requests.get(DCT_URL + '/v2/' + i, headers=req_headers, verify=False)
	responsej = json.loads(response.text)
	# print("")
	# print("")
	# print("**********************************************************************************************************************************")
	event_client = EventClient(NEW_RELIC_KEY)
	for line in responsej['items']:
		event = Event(
			NEWRELIC_TYPE, line
		)
		# print (event)
		response = event_client.send(event)
		response.raise_for_status()
	print ("Upload successful: " + NEWRELIC_TYPE)

sys.exit(0)

