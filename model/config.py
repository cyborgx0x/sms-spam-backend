
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
from transformers import BertConfig, BertModel


class Config(object):
    pretrained_model = "vinai/phobert-base"
    id2label = {0: "normal", 1: "spam"}
    label2id = {"normal": 0, "spam": 1}
    output_directory = "sms_spam_detection"

    @property
    def model(self):
        return AutoModelForSequenceClassification.from_pretrained(
            self.pretrained_model, num_labels=2, id2label=self.id2label, label2id=self.label2id
        )
    @property
    def training_argument(self):
        return TrainingArguments(
            output_dir=self.output_directory,
            learning_rate=2e-5,
            per_device_train_batch_size=16,
            per_device_eval_batch_size=16,
            num_train_epochs=2,
            weight_decay=0.01,
            evaluation_strategy="epoch",
            save_strategy="epoch",
            load_best_model_at_end=True,
            push_to_hub=True,
        )