# sms_spam_backend

## How to RUN the server

First install the pytorch with CUDA Support to ultilize the power of GPU
If anything wrong happen, try to install CUDA toolkist

add following to env:

```sh
RABBITMQ_HOST=your-host
RABBITMQ_USER=username
RABBITMQ_PASSWORD=password
RABBITMQ_VHOST=vhost
SMS_QUEUE=yoursmsqueue
```

```sh
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
uvicorn main:app --reload --port 5000
```
