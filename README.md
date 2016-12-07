Docker Druid
================
_Note: This is a work in progress..._

This project was built while evaluating the [Druid](http://druid.io/) distributed data store and real time analytics platform. The aim is to have a full Druid cluster running in Docker, with Kafka ingestion pre-configured via a Tranquility server. 

The project based on [this project](https://github.com/znly/docker-druid) with a few modifications, including bundling Tranquility.

Quickstart
==========
Note: You may wish to replace references to 10.200.10.1 in config files, or alias lo0 to this address, e.g. `ifconfig lo0 alias 10.200.10.1/24`. This is a workaround for a Docker for Mac limitation which can be ignored if you're not using Docker for Mac.

Run:

    docker-compose up -d --build

The compose file will launch:

- Zookeeper
- Postgres
- Kafka
- Broker
- Overlord
- Middlemanager
- Historical
- Tranquility

Loading Sample Data via Tranquility
===================================
Publish sample data to the Kafka topic with `kafka_producer.py`. 
The sample data is some randomly selected economic data from [Quandl](www.quandl.com).  

Pivot
=====
Pivot is an open source data visualisation and query tool which integrates with Druid.io. 

To start, download and extract the [Imply](https://imply.io/) platform. 

Run:

    bin/generate-pivot-config --druid localhost:32768
    
(supply the correct broker port)

Copy the generated config to conf/pivot/config.yaml.

You can view the dashboard at http://localhost:9091 


It may take 10m before data shows up in Pivot the first time (this is governed by Tranquility's windowPeriod setting). 

Check lag:

    $ <your_kafka_install>/bin/kafka-consumer-offset-checker.sh --zookeeper localhost:2181 --group druid_group_id --topic demo
     

Plyql
=====
    cd imply-1.3.0/bin
    ./plyql -h 0.0.0.0:32769 -q 'SHOW TABLES'
    ./plyql -h 0.0.0.0:32769 -q 'SELECT max(__time) as maxTime from demo'

Pydruid
=======
Run `pydruid_example.py` 
