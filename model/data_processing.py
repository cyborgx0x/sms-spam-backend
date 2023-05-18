'''
Phục vụ tiền xử lý dữ liệu
'''
from transformers import DataCollatorWithPadding, AutoTokenizer


class Data_Processing():
    kind = ["preprocessing", "tokenization", "padding"]

    def __init__(self, dataset, pretrained_model) -> None:
        self.dataset = dataset
        self.tokenizer = AutoTokenizer.from_pretrained(pretrained_model)
        def preprocess_function(examples):
            return self.tokenizer(examples["text"], truncation=True)
        
        self.tokenized_sms = self.dataset.map(preprocess_function, batched=True)
        self.data_collator = DataCollatorWithPadding(tokenizer=self.tokenizer)
    