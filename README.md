# Delphix Data Control Tower's Data Source with New Relic

This project will allow you to send data from [Delphix Data Control Tower (DCT)](https://delphix.document360.io/dct/docs) to [New Relic](https://newrelic.com/) through the Events API. This repository is one component of the Delphix Quickstart. More can be learned about the [soultion on the New Relic website](https://newrelic.com/instant-observability/delphix).

![Screenshot](images/image2.png)


## Getting Started

These instructions will provide the information you need to extract data from DCT and send it to New Relic. 


### Prerequisites

* New Relic Account: [Sign Up](https://newrelic.com/signup)
* Delphix Data Control Tower (DCT) with one or more engines: [Data Control Tower Docs](https://delphix.document360.io/dct/docs)
* Python 3.10: [Python Install](https://www.python.org/downloads)
* New Relic Python SDK: [Installation Directions](https://github.com/newrelic/newrelic-telemetry-sdk-python)
* This [GitHub repository](https://github.com/delphix/dct-newrelic-integration)


### Configuration

The ```dlpx_dct_to_nr.py``` script contains the logic to perform the data upload. However, you must do some configuration first. 

Retrieve the following:
* Record the DCT URL.
* Generate a [DCT APK](https://delphix.document360.io/docs).
* Generate a [New Relic User Key](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/#ingest-license-key).

Once we have these values, specify the following environment variables:
* DCT_URL
* DCT_KEY
* NEW_RELIC_USER_KEY

Note: You may modify the Python script directly, but it is best practice to specify sensitive data through environment variables.


### Execution

You may test the script by running the following command:
```python dlpx_dct_to_nr.py```

In production, it is common to use a scheduler, such as a cron, to repeat the call on a recurring basis. For example, the following command will run the script every 5 minutes:
```*/5 * * * * python dlpx_dct_to_nr.py```

On each execution, this script will extract the following metrics from all registered Delphix engines:

* Engines - Data extraction date, CPU Count, Storage, Memory, Engine Type, Version, etc.
* Environments - Data extraction date, Status, Engine ID, Name, etc.
* Sources - Data extraction date, Database Type, Database Version, Environment ID, JDBC Connection String, Database Name and Size, etc
* dSources - Data extraction date, dSource Creation Date, dSource Type, Version, Name, Status, Size, etc.
* VDBs - Data extraction date, Database Type and Version, Creation Date, Group Name, Name, Parent ID, Size, Status, etc.


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
Copyright (c) 2021, 2022 by Delphix. All rights reserved.
