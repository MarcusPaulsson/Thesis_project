import time
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

print("Started")

# Set the absolute path to the model
model_name_or_path = "/home/marpa/Projects/Models/WizardCoder-Python-7B-V1.0"

# Start timing model loading
start_load_time = time.time()

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

# Load model with PyTorch, ensure CPU execution
model = AutoModelForCausalLM.from_pretrained(model_name_or_path, torch_dtype=torch.float16).to("cpu")

# End timing model loading
end_load_time = time.time()
loading_time = end_load_time - start_load_time
print(f"\nModel loaded in {loading_time:.2f} seconds.\n")

# Define the evaluation function
def evaluate(batch_data, tokenizer, model, max_new_tokens=4):
    """ Runs inference using PyTorch tensors. """
    # Convert input to PyTorch tensor
    inputs = tokenizer(batch_data, return_tensors="pt", max_length=256, truncation=True)
    input_ids = inputs["input_ids"].to("cpu")  # Ensure tensor is on CPU

    # Generate output using PyTorch
    with torch.no_grad():  # Disable gradients for efficiency
        generation_output = model.generate(
    input_ids,
    max_new_tokens=max_new_tokens,
    temperature=0.7,
    top_p=1,
    top_k=40,
)


    # Decode the generated tokens into human-readable text
    output_text = tokenizer.decode(generation_output[0], skip_special_tokens=True)
    return output_text

# Start timing inference
start_inference_time = time.time()

# Run inference
prompt = "Hello, tell me a story about the sun."
output = evaluate(prompt, tokenizer, model)

# End timing inference
end_inference_time = time.time()
inference_time = end_inference_time - start_inference_time

# Print results
print(output.strip())
print(f"\n\nGeneration complete! Inference took {inference_time:.2f} seconds.\n")