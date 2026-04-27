import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class Translator:
    def __init__(self, model_name="facebook/nllb-200-distilled-600M", target_lang=None):
        self.model_name = model_name
        self.target_lang = target_lang

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

        self.model.eval()

        self.tokenizer.src_lang = "eng_Latn"

        self.device = torch.device("cpu")
        self.model.to(self.device)

    def translate(self, text, target_lang=None):
        if target_lang is None:
            target_lang = self.target_lang

        inputs = self.tokenizer(text, return_tensors="pt")
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        forced_id = self.tokenizer.lang_code_to_id[target_lang]

        with torch.no_grad():
            outputs = self.model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                forced_bos_token_id=forced_id
            )

        return self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
