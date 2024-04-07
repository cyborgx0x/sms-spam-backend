import json

import pika

from config import *
from spam_detection import SpamDetection

spam_detect = SpamDetection()


def callback(ch, method, properties, body):

    sms = json.loads(body)
    sms["classify"] = spam_detect.detect(sms["content"])
    print(sms)


credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
parameters = pika.ConnectionParameters(
    RABBITMQ_HOST,
    credentials=credentials,
    virtual_host=RABBITMQ_VHOST,
)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue=SMS_QUEUE)

# Start consuming messages
print("Waiting for messages. To exit, press CTRL+C")
channel.basic_consume(queue=SMS_QUEUE, on_message_callback=callback, auto_ack=True)

# Start consuming messages
try:
    channel.start_consuming()
except KeyboardInterrupt:
    print("Stopped consuming messages.")
    channel.stop_consuming()

# Close the connection
connection.close()
