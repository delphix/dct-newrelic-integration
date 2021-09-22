# Delphix Data Control Tower MultiCloud integration with New Relic

This project will allow you to send data from [Delphix Data Control Tower Multicloud](https://docs.delphix.com/dctmc) to [New Relic](https://newrelic.com/) as events. DCT Multicloud is a tool that will allow you to connect to all your Delphix engines on premises or in the cloud (AWS, Azure, Google Cloud, OCI and IBM)

![Screenshot](images/image2.png)

## Getting Started

These instructions will provide the code you need to extract data from DCT Multicloud and send it to New Relic.

### Prerequisites

It's assumed that you have a New Relic valid account and one or many [Delphix Engines registered in DCT Multicloud](https://docs.delphix.com/dctmc/connecting-a-delphix-engine).
DCT Multicloud will extract data from the Delphix Engines and we will use [New Relic Telemetry SDK](https://docs.newrelic.com/docs/telemetry-data-platform/ingest-apis/telemetry-sdks-report-custom-telemetry-data/) to send that data to New Relic.
For this project, we will use the [Python SDK](https://github.com/newrelic/newrelic-telemetry-sdk-python), however you can use any of the available SDKs in different languages, because you will be using DCT Multicloud Restful API.



### Installing

To push the data from Delphix DCT Multicloud to New Relic, we use the script dlpx_dct_to_nr.py.
To use this script we have to do some steps first:

* Generate the [keys to connect to DCT Multicloud](https://docs.delphix.com/dctmc/authentication)
* Generate the [New Relic access key](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/#ingest-license-key)

Once we have these keys we need to replace them in the script:

* In req_headers we replace the DCT Multicloud key
* In NEW_RELIC_INSERT_KEY we replace the New Relic access key

```
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
	'Authorization': 'apk 2.bnQDDx46Z4CDlIShLw2ZHElWLyKtsmZaBjbQPjui8LcQ3nELbkdEbQJSki6vmwLf'
}

#
# Python session, also handles the cookies ...
#
session = requests.session()

#
# Login ...
#
os.environ['NEW_RELIC_INSERT_KEY'] = "87a453b2efe4nd4df78b167e7ac457e076c7NRAL"
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
```

On execution this script will extract data from all the registered Delphix Engines for the following metrics:

* Engines - Data extraction date, CPU Count, Storage, Memory, Engine Type, Version, etc.
* Environments - Data extraction date, Status, Engine ID, Name, etc.
* Sources - Data extraction date, Database Type, Database Version, Environment ID, JDBC Connection String, Database Name and Size, etc
* dSources - Data extraction date, dSource Creation Date, dSource Type, Version, Name, Status, Size, etc.
* VDBs - Data extraction date, Database Type and Version, Creation Date, Group Name, Name, Parent ID, Size, Status, etc.

This script can be added to cron or any scheduler to run in any time interval. Once the data is available in New Relic, it can be used to be queried or to create dashboards.

## Data and Dashboards

This is how the raw data looks like in the [Query your data](https://docs.newrelic.com/docs/query-your-data/explore-query-data/get-started/introduction-querying-new-relic-data/#browse-data) window for the VDB metric:

![Screenshot](images/image1.png)

With this data we can create graphs and dashboards like this:

![Screenshot](images/image3.png)

And this is the query we used to create this graph:

```
SELECT MAX(data_storage_capacity)-MIN(data_storage_used) FROM `Delphix engines` SINCE 7 DAYS AGO TIMESERIES facet name
```

## Contributing

Please read [CONTRIBUTING.md](https://github.com/delphix/.github/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Reporting Issues

Issues should be reported in the GitHub repo's issue tab. Include a link to it.

## Statement of Support

This software is provided as-is, without warranty of any kind or commercial support through Delphix. See the associated license for additional details. Questions, issues, feature requests, and contributions should be directed to the community as outlined in the Delphix Community Guidelines.

License
```
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 ```
Copyright (c) 2014, 2016 by Delphix. All rights reserved.
