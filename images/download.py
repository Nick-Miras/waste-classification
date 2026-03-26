"""
https://huggingface.co/docs/hub/datasets-usage
"""
from datasets import load_dataset


# Login using e.g. `huggingface-cli login` to access this dataset
ds = load_dataset("NickAnthonyMiras/waste_classification")
