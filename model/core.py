import os
from .config import Config
from .trainer import compute_metrics
from transformers import Trainer
from .data_processing import Data_Processing

class Core():

    config = Config()

    def __init__(self, dataset) -> None:
        self.dataset = dataset
        self.data = Data_Processing(dataset=self.dataset, pretrained_model=self.config.pretrained_model)
        

    def _run(self):
        training_args = self.config.training_argument
        trainer = Trainer(
            model=self.config.model,
            args=training_args,
            train_dataset=self.data.tokenized_sms["train"],
            eval_dataset=self.data.tokenized_sms["test"],
            tokenizer=self.data.tokenizer,
            data_collator=self.data.data_collator,
            compute_metrics=compute_metrics,
        )

        trainer.train()

