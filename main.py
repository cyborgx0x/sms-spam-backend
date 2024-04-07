import json
import uuid

import pika
from fastapi import FastAPI
from pydantic import BaseModel

from config import *

app = FastAPI()


class SMS(BaseModel):
    content: str


@app.post("/spam_detection/")
async def detect_sms(sms: SMS):
    unique_id = uuid.uuid4().hex
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBITMQ_HOST, credentials=credentials, virtual_host=RABBITMQ_VHOST
        )
    )
    channel = connection.channel()

    channel.queue_declare(queue=SMS_QUEUE)
    sms = {
        "id": unique_id,
        "content": sms.content,
    }
    channel.basic_publish(exchange="", routing_key=SMS_QUEUE, body=json.dumps(sms))

    connection.close()
    return unique_id
