# Delphix Data Control Tower MultiCloud integration with New Relic

This project will allow you to send data from [Delphix Data Control Tower Multicloud](https://docs.delphix.com/dctmc) to [New Relic](https://newrelic.com/). DCT Multicloud is a tool that will allow you to connect to all your Delphix engines on premises or in the cloud (AWS, Azure, Google Cloud, OCI and IBM)

## Getting Started

These instructions will provide the code you need to extract data from DCT Multicloud and send it to New Relic.

### Prerequisites

It's assumed that you have a New Relic valid account and one or many Delphix Engines registered in DCT Multicloud.
DCT Multicloud will extract data from the Delphix Engines and we will use [New Relic Telemetry SDK](https://docs.newrelic.com/docs/telemetry-data-platform/ingest-apis/telemetry-sdks-report-custom-telemetry-data/) to send that data to New Relic.
For this project, we will use the [Python SDK](https://github.com/newrelic/newrelic-telemetry-sdk-python), however you can use any of the available SDKs in different languages, because you will be using DCT Multicloud Restful API.

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://github.com/delphix/.github/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Joe Smith** - *Initial work* - [Company](https://github.com/Company)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the XX License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
