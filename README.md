# sms_spam_backend
 
## How to RUN the server

First install the pytorch with CUDA Support to ultilize the power of GPU
If anything wrong happen, try to install CUDA toolkist

``` sh
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
uvicorn main:app --reload --port 5000
```