# create example dataset
from clearml import StorageManager, Dataset


# Create a dataset with ClearML`s Dataset class
try:
    dataset = Dataset.get(
        dataset_project='Public',
        dataset_name='FireDataset'
    )
except:
    dataset = Dataset.create(
        dataset_project="Public", dataset_name="FireDataset"
    )

dataset.add_files(
  path="/Users/ijongjin/workspace/dataset/Iwest_SmokeDataset_v1.0.0/"
)

dataset.upload(show_progress=True, verbose=False, output_url="s3://192.168.0.51:9000/MLTeam/Dataset/clearml/", compression=None, chunk_size=None, max_workers=None, retries=3)
# Upload dataset to ClearML server (customizable)

# commit dataset changes
dataset.finalize()

# class Dataset