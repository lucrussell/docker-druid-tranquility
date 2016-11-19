import json
from pykafka import KafkaClient

TEST_KAFKA_BROKER = '0.0.0.0'
TEST_KAFKA_BROKER_PORT = '9092'
TOPIC = b'demo'
publish = False


def process_input_file(filename, producer):
    with open('sample_data/' + filename) as json_data:
        data = json.load(json_data)
        measure = filename.split('.')[0]
        for x in range(0, len(data['dataset'])):
            keys = ('date', 'measure', 'value')
            values = (data['dataset']['data'][x][0], measure, data['dataset']['data'][x][1])
            adict = dict(zip(keys, values))
            if publish:
                producer.produce(str(adict).encode('utf-8'))
            print(str(adict))


def send():
    producer = None
    if publish:
        client = KafkaClient(TEST_KAFKA_BROKER + ':' + TEST_KAFKA_BROKER_PORT)
        topic = client.topics[TOPIC]
        producer = topic.get_sync_producer(delivery_reports=True)
    process_input_file('us_gdp.json', producer)
    process_input_file('ecb_systemic_risk.json', producer)
    process_input_file('us_construction.json', producer)

if __name__ == "__main__":
    send()
