import os
class DatasetProcessing():
    state = ""

    @property
    def data(self):
        pass
    
    @staticmethod
    def _get_ready():
        try:
            import pandas
            from datasets import load_dataset
            from huggingface_hub import notebook_login
            from transformers import AutoTokenizer
        except:
            os.system("pip install -r requirements.txt")


