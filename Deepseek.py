import os
from transformers import AutoTokenizer, pipeline, logging
from gptqmodel import GPTQModel

# Set the local model folder path (adjust the folder name if needed)
model_name_or_path = os.path.join(os.getcwd(), "DeepSeek-R1-Distill-Qwen-7B-gptqmodel-4bit-vortex-v2")

# Load the tokenizer from the local model folder
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True)

# Load the model using the from_quantized() method
model = GPTQModel.from_quantized(
    model_name_or_path,
    use_safetensors=True,
    device="cuda:0",    # Change to "cpu" if you don't have a GPU
    use_triton=False,   # Set to True if you want to use Triton
    quantize_config=None  # Quantization parameters are read automatically
)

# Suppress extra logging messages
logging.set_verbosity(logging.CRITICAL)

# Create a text-generation pipeline using the loaded model and tokenizer
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Define a prompt template and generate a prompt
prompt_template = '''Below is an instruction that describes a task. Write a response that appropriately completes the request

### Instruction: {prompt}

### Response:'''
prompt = prompt_template.format(prompt="How do I sort a list in Python?")

# Generate text using the pipeline
outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.2, top_k=50, top_p=0.95)

# Print the generated text
print(outputs[0]['generated_text'])
