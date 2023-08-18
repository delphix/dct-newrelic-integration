# Delphix Data Control Tower's Integration with New Relic

This project will allow you to send data from [Delphix Data Control Tower (DCT)](https://dct.delphix.com/docs/latest) to [New Relic](https://newrelic.com/) through the Events API. This repository is one component of the Delphix Quickstart. You can learn more on the [Delphix Instant Observability page](https://newrelic.com/instant-observability/delphix).

![Screenshot](images/image2.png)


## Getting Started


These instructions will provide the information you need to extract data from DCT and send it to New Relic. The Python script can run from any location with access to both DCT and New Relic.


### Prerequisites

* New Relic Account: [Sign Up](https://newrelic.com/signup)
* Delphix Data Control Tower (DCT) with one or more engines: [Data Control Tower Docs](https://dct.delphix.com/docs/latest)
* Python 3.7+: [Python Install](https://www.python.org/downloads)
* This [GitHub repository](https://github.com/delphix/dct-newrelic-integration)

<hr>
<h4> Supported Python Versions and OS </h4>
<hr>

- MacOS - Python3.7 and Python3.8
- Linux - Python3.7+
- Windows - Python3.7+

<hr>

### Installing
To use this script we have to do some steps first:

* Generate the [key to connect to DCT](https://dct.delphix.com/docs/latest/api-keys)
* Generate the [New Relic access key](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/#ingest-license-key)
* Note the URL of the DCT instance VM


### Setup
The ```src/main.py``` script contains the logic to perform the data upload. However, you must do some configuration first. 

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

Note: You may modify the Python script directly, but it is best practice to specify sensitive data through environment variables.

<hr>

In production, it is common to use a scheduler, such as a systemd, nohup, or wininit.exe, to ensure the script continually runs. For example, the following nohup command will run the script every N seconds based on the Interval provided in the `dct_nr_config.ini` file:
```nohup make run &```


On each execution, this script will extract the following metrics from all registered Delphix engines:

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


## Data, Dashboards, and Alerts

Once the data is available within New Relic, you are free to leverage it as you wish through customized Dashboards and Alerts. Samples can be found as a part of the [Delphix Quickstart](https://newrelic.com/instant-observability/delphix). 

As an example, this is how the raw data looks like in the [Query your data](https://docs.newrelic.com/docs/query-your-data/explore-query-data/get-started/introduction-querying-new-relic-data/#browse-data) window for the VDB metric:

![Screenshot](images/image1.png)

With this data we can create graphs and dashboards like this:

![Screenshot](images/image3.png)

And this is the query we used to create this graph:

```
SELECT MAX(data_storage_capacity)-MIN(data_storage_used) FROM `Delphix engines` SINCE 7 DAYS AGO TIMESERIES facet name
```


## Contributing

This project is currently not accepting external contributions.


## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).


## Reporting Issues and Questions

Please report all issues and questions in the [GitHub issue tab](https://github.com/delphix/dct-newrelic-integration/issues) or [Delphix Community page](https://community.delphix.com/home). Please include a complete problem description, error logs if appropriate, and directions on how to reproduce.


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
