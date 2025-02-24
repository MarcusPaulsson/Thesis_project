from datasets import load_dataset

# Download the ClassEval dataset
ds = load_dataset("FudanSELab/ClassEval")

# List available splits
print("Available splits:", list(ds.keys()))

# Choose an available split. For example, use 'test' if 'train' isn't available.
if "train" in ds:
    data_split = ds["train"]
elif "test" in ds:
    data_split = ds["test"]
else:
    # If neither 'train' nor 'test' exists, use the first available split.
    data_split = list(ds.values())[0]

# Save the selected split to a CSV file
csv_filename = "ClassEval_data.csv"
data_split.to_csv(csv_filename, index=False)

print(f"Dataset saved to {csv_filename}")
