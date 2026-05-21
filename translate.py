import torch
import re


def split_sentences(text):
    # splits on ., !, ? while keeping it natural
    return re.split(r'(?<=[.!?])\s+', text.strip())


class Translator:
    def __init__(self, model_name):
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

        self.model_name = model_name

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name,
            local_files_only=True
        )

        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            self.model_name,
            local_files_only=True
        )

        self.model.eval()

        self.device = torch.device("cpu")
        self.model.to(self.device)

    def translate(self, text):

        sentences = split_sentences(text)

        outputs = []

        for s in sentences:
            s = s.strip()
            if not s:
                continue

            inputs = self.tokenizer(s, return_tensors="pt")
            inputs = {k: v.to(self.device) for k, v in inputs.items()}

            with torch.inference_mode():
                result = self.model.generate(
                    **inputs,
                    num_beams=1,
                    do_sample=False,
                    max_new_tokens=100
                )

            translated = self.tokenizer.decode(
                result[0],
                skip_special_tokens=True
            )

            outputs.append(translated)

        return " ".join(outputs)
