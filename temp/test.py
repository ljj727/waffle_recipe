from datasets import load_dataset 

# Print all the available datasets
from huggingface_hub import list_datasets
# print([dataset.id for dataset in list_datasets()])

image_dataset = load_dataset('cifar10')
print(image_dataset)
# for example in image_dataset["train"]:
#     break