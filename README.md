# BoilerJuice Oil Price Tracker

This project queries the BoilerJuice API to retrieve recent oil prices and
pushes the data into an InfluxDB database. The application is written in Python
and is distributed under the Apache 2.0 license. Additionally, it is available
as a Docker container for ease of deployment.

## Features

- Retrieve recent oil prices from the BoilerJuice API
- Store data in an InfluxDB database
- Easy deployment with Docker
- Open-source under the Apache 2.0 license

## Getting Started

### Prerequisites

- Docker installed on your machine
- An InfluxDB instance running and accessible

### Installation via Git

1. **Clone the repository:**

   ```sh
   git clone https://github.com/cimeson/boilerjuice-oilprice-influxdb.git
   ```

2. Install Python dependencies.

   ```sh
   cd boilerjuice-oilprice-influxdb
   pip install -r requirements.txt
   ```

3. Execute the application.

   ```sh
   INFLUXDB_URL=<your_influxdb_url> \
   INFLUXDB_TOKEN=<your_influxdb_token> \
   INFLUXDB_ORG=<your_influxdb_org> \
   INFLUXDB_BUCKET=<your_influxdb_bucket> \
   python main.py
   ```

### Installation via Docker

1. Run the Docker container:

   ```sh
   docker run -it --name oil-price-tracker \
       -e INFLUXDB_URL=<your_influxdb_url> \
       -e INFLUXDB_TOKEN=<your_influxdb_token> \
       -e INFLUXDB_ORG=<your_influxdb_org> \
       -e INFLUXDB_BUCKET=<your_influxdb_bucket> \
       cimeson/boilerjuice-oilprice-influxdb
   ```

   Replace `<your_influxdb_url>`, `<your_influxdb_token>`,
   `<your_influxdb_org>` and `<your_influxdb_bucket>` with your actual InfluxDB
   URL and token.

## Configuration

The application can be configured using environment variables:

- `INFLUXDB_URL`: The URL of your InfluxDB instance.
- `INFLUXDB_TOKEN`: The token for authenticating with your InfluxDB instance.
- `INFLUXDB_ORG`: The organization in your InfluxDB instance.
- `INFLUXDB_BUCKET`: The bucket in your InfluxDB instance.

Environment variables may be passed through a `.env` file or directly on the
command line.

## Usage

Once the container is running, it will poll the BoilerJuice API for recent oil
prices and store the data in your InfluxDB database. The container will run once
and then exit. It is designed to be run periodically using a scheduler like
Kubernetes CronJobs or a similar tool.

## License

This project is licensed under the Apache 2.0 License - see the
[LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions!

## Support

This software comes with no warranty of any kind. However, if you encounter any
issues or have questions, please open an issue on the [GitHub
repository](https://github.com/cimeson/boilerjuice-oilprice-influxdb/issues).

## Acknowledgements

- Thanks to BoilerJuice team for providing the API.
