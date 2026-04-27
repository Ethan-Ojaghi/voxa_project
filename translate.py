import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class Translator:
    def __init__(self, model_name="facebook/nllb-200-distilled-600M", target_lang=None):
        self.model_name = model_name
        self.target_lang = target_lang

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name,
            local_files_only=True
        )

        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            self.model_name,
            local_files_only=True
        )

        self.model.eval()
        self.model.config.use_cache = True  

        self.tokenizer.src_lang = "eng_Latn"

        self.device = torch.device("cpu")
        self.model.to(self.device)

    def translate(self, text, target_lang=None):
        if target_lang is None:
            target_lang = self.target_lang

        text = text.strip()[:150]

        inputs = self.tokenizer(text, return_tensors="pt")
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        forced_id = self.tokenizer.convert_tokens_to_ids(target_lang)

        with torch.inference_mode():
            outputs = self.model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            forced_bos_token_id=forced_id,

            num_beams=1,
            do_sample=False,
            max_new_tokens=20,

            use_cache=True,
            early_stopping=False
        )

        return self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
