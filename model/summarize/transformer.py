import bentoml
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
tokenizer = AutoTokenizer.from_pretrained("t5-base")

tag = bentoml.transformers.save("summarize", model=model, tokenizer=tokenizer)