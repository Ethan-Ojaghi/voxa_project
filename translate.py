import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class Translator:
    def __init__(self, model_name):
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
        text = text.strip()[:80]

        inputs = self.tokenizer(text, return_tensors="pt")
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        with torch.inference_mode():
            outputs = self.model.generate(
                **inputs,
                num_beams=1,
                do_sample=False,
                max_new_tokens=40
            )

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
