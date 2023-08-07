# create example dataset
from clearml import StorageManager, Dataset


# Create a dataset with ClearML`s Dataset class
try:
    dataset = Dataset.get(
        dataset_project='Public',
        dataset_name='Smoke'
    )
except:
    dataset = Dataset.create(
        dataset_project="Public", dataset_name="Smoke"
    )
# dataset.add_external_files(source_url="s3://my_bucket/stuff/file.jpg", dataset_path="/my_dataset/new_folder/")
dataset.add_files(
  path="/home/ljj/data/Iwest_SmokeDataset_v1.0.0"
)

dataset.upload(show_progress= True, verbose= False, output_url= 's3://snuailab-asri.iptime.org:9000/clearml', compression= None)
# dataset.upload()
# Upload dataset to ClearML server (customizable)

# commit dataset changes
dataset.finalize()

# class Dataset
