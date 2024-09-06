from confluent_kafka import Consumer, KafkaError, KafkaException
import sys, os

def consume_messages():
    # kafka configuration
    conf = {
        "bootstrap.servers": os.getenv("BROKER_SERVER"),
        "group.id": os.getenv("GROUP_ID"),
        "auto.offset.reset" : "earliest"
    }

    # create consumer instance
    consumer = Consumer(conf)

    # subscribe to topic
    consumer.subscribe([os.getenv("CONSUMER_KAFKA_TOPIC")])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                    (msg.topic(), msg.partition(), msg.offset()))
                    
                elif msg.error():
                    raise KafkaException(msg.error())
                
            else:
                # consumer.commit(asynchronous=False)
                message = msg.value().decode('utf-8')
                print('Received message: %s' % (msg.value().decode('utf-8')))
                return message

                
    except KeyboardInterrupt:
        pass

    finally:
        consumer.close()