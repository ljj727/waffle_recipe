# create example dataset
from waffle_hub.dataset import Dataset as wd
from clearml import Dataset as cd

name="AihubHighway_Vihicle_v1.1.0"

dataset = wd.load(name)

clearml_dataset = cd.create(
    dataset_project="Public", dataset_name="Vihicle", dataset_version=dataset.name.split('_')[-1][1:], dataset_tags= [dataset.task] + dataset.name.split('_')
)

clearml_dataset.add_files(
    path=str(dataset.dataset_dir)
)

clearml_dataset.upload(show_progress=True, verbose=False, output_url="s3://192.168.0.51:9000/MLTeam/Dataset/clearml", compression=None, chunk_size=None, max_workers=None, retries=3)


clearml_dataset.finalize()