import os
import requests
import json
import sys
import time
from newrelic_telemetry_sdk import Event, EventClient
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

DLPX_TYPES= ["engines","sources","dsources","vdbs","environments"]
#
# Request Headers ...
#
req_headers = {
	'Authorization': 'apk 2.bnQDDx46Z4CDlIShLw2ZHElWLyKtsmZaBjbQPjui8LcQ3TELbkdEbQJSki6vmwLf'
}

#
# Python session, also handles the cookies ...
#
session = requests.session()

#
# Login ...
#
os.environ['NEW_RELIC_INSERT_KEY'] = "87a453b2efe4bd4df78b167e7ac457e076c7NRAL"
print ('')
for i in DLPX_TYPES:

	response = requests.get('https://localhost:443/v1/'+i, headers=req_headers, verify=False)
	responsej = json.loads(response.text)
	print("")
	print("")
	print("**********************************************************************************************************************************")
	event_client = EventClient(os.environ["NEW_RELIC_INSERT_KEY"])
	NEWRELIC_TYPE="Delphix " + str(i)
	print (NEWRELIC_TYPE)
	for line in responsej['items']:
		event = Event(
			NEWRELIC_TYPE, line
		)
		print (event)
		response = event_client.send(event)
		response.raise_for_status()
		print("Event sent successfully!")
		print("")

print ('')
sys.exit(0)
