# Delphix Data Control Tower MultiCloud integration with New Relic

This project will allow you to send data from [Delphix Data Control Tower Multicloud](https://docs.delphix.com/dctmc) to [New Relic](https://newrelic.com/) as events. DCT Multicloud is a tool that will allow you to connect to all your Delphix engines on premises or in the cloud (AWS, Azure, Google Cloud, OCI and IBM)

![Screenshot](images/image2.png)


## Getting Started

These instructions will provide the steps you need to extract data from DCT Multicloud and send it to New Relic.


### Prerequisites

It's assumed that you have a New Relic valid account and one or many [Delphix Engines registered in DCT Multicloud](https://docs.delphix.com/dctmc/connecting-a-delphix-engine).
DCT Multicloud will extract data from the Delphix Engines and we will use [New Relic Telemetry SDK](https://docs.newrelic.com/docs/telemetry-data-platform/ingest-apis/telemetry-sdks-report-custom-telemetry-data/) to send that data to New Relic.
For this project, we will use the [Python SDK](https://github.com/newrelic/newrelic-telemetry-sdk-python), however you can use any of the available SDKs in different languages.

We are using Python 3.7+ for this project. Hence, prerequisite is to have Python 3.7+ installed on your system.

<hr>
<h4> Supported Python Versions </h4>
<hr>

- MacOS - Python3.7 and Python3.8
- Linux - Python3.7+
- Windows - Python3.7+

<hr>

### Installing
To use this script we have to do some steps first:

* Generate the [keys to connect to DCT Multicloud](https://docs.delphix.com/dctmc/authentication)
* Generate the [New Relic access key](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/#ingest-license-key)
* Note the URL of the DCT instance VM

To push the data from Delphix DCT Multicloud to New Relic, we will have to perform the below steps:

* We need to supply the above gathered information using 3 environment variables
  * DCT_HOST_URL
  * DCT_API_KEY
  * NEW_RELIC_INSERT_KEY
* Clone this repository
* Go inside the project directory - `cd dct-newrelic-integration`

For Mac and Linux:
* Run command `make env` (This will create the virtual environment)
* Run command `make run` (This will run the script and push the data)

For Windows:
* Check that python 3 is installed
* Create a virtual environment running `python -m venv venv`
* Activate the virtual environment by running `venv\Scripts\activate`
* Install the dependencies by running `pip install -r requirements.txt`
* Set Python path by - `set PYTHONPATH=.`
* Run the script using `python src\main.py`


On execution, this script will extract data from all the registered Delphix Engines for the following metrics:

* Engines - Data extraction date, CPU Count, Storage, Memory, Engine Type, Version, etc.
* Environments - Data extraction date, Status, Engine ID, Name, etc.
* Sources - Data extraction date, Database Type, Database Version, Environment ID, JDBC Connection String, Database Name and Size, etc
* dSources - Data extraction date, dSource Creation Date, dSource Type, Version, Name, Status, Size, etc.
* VDBs - Data extraction date, Database Type and Version, Creation Date, Group Name, Name, Parent ID, Size, Status, etc.

More over we have `dct_nr_config.ini` file which can be used to configure 
- Logging Level 
- Interval (in seconds): This script keeps running and sleeps for `INTERVAL` seconds after sending the data once.
- Components we need from DCT APIs

Once the data is available in New Relic, it can be used to be queried or to create dashboards.

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
