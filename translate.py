from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Translator:
    def __init__(self, model_name="facebook/nllb-200-distilled-600M", target_lang=None):
        self.model_name = model_name
        self.target_lang = target_lang
        
        # Load model + tokenizer once (important for performance)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

    def translate(self, text, target_lang=None):
        if target_lang is None:
            target_lang = self.target_lang
        
        # Tokenize input
        inputs = self.tokenizer(text, return_tensors="pt")

        # Generate translation
        translated_tokens = self.model.generate(
            **inputs,
            forced_bos_token_id=self.tokenizer.convert_tokens_to_ids(target_lang)
        )

        # Decode and RETURN result (not print)
        translated_text = self.tokenizer.batch_decode(
            translated_tokens, skip_special_tokens=True
        )[0]

        return translated_text

