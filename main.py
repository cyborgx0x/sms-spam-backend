from typing import Union

from fastapi import FastAPI
from detection import SpamDetection
from pydantic import BaseModel


app = FastAPI() 
from typing import Annotated

'''
Init the Spam Detection Object
'''
spam_detect = SpamDetection()


class SMS(BaseModel):
    content: str


@app.post("/spam_detection/")
async def detect_sms(sms:SMS):
    return spam_detect.detect(sms.content)
