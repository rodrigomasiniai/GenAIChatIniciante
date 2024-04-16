import os
import json
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from mylib.file_path_handler import FilePathHandler

class ModelLoader:
    def __init__(self):
        self.file_path_handler = FilePathHandler()
        self.tokenizer, self.model, self.summary_model, self.app_name, self.config = self.load_model()

    def load_model(self):
        config_file_path = self.file_path_handler.config_file_path
        if os.path.isfile(config_file_path):
            with open(config_file_path, "r") as config_file:
                config = json.load(config_file)
                qa_model_name = config.get("qa_model_name")
                summary_model_name = config.get("summary_model_name")
                app_name = config.get("app_name")
        else:
            qa_model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"  # Backup model
            app_name = None
            config = None

        # Load the question-answering model and tokenizer
        tokenizer = AutoTokenizer.from_pretrained(qa_model_name)
        model = AutoModelForQuestionAnswering.from_pretrained(qa_model_name)
        summary_model = summary_model_name

        return tokenizer, model, summary_model, app_name, config
