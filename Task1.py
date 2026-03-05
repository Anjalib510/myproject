from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# load GPT-2 model and tokenizer
model_name = "gpt2"

tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# sample prompt
prompt = "Artificial Intelligence is"

# convert text into tokens
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# generate text
output = model.generate(
    input_ids,
    max_length=50,
    num_return_sequences=1,
    no_repeat_ngram_size=2
)

# convert tokens back to text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

# print result
print("Prompt:", prompt)
print("Generated Text:")
print(generated_text)