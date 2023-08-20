
# create example dataset
from waffle_hub.dataset import Dataset as wd
from clearml import Dataset as cd

def dataset_download(dataset_id='9da482e6528141f2986a1323e44225d6'):
    clearml_dataset=cd.get(dataset_id=dataset_id)
    dataset1 = clearml_dataset.get_mutable_local_copy("/home/ljj/waffle/datasets/HelemetDataset_v1.0.0")


def dataset_upload(project='Public', name="AihubHighway_Vehicle", version='1.1.0'):
    dataset = wd.load(name)

    clearml_dataset = cd.create(
        dataset_project=project, dataset_name=name, dataset_version=version, dataset_tags= [dataset.task] + dataset.name.split('_')
    )

    clearml_dataset.add_files(
        path=str(dataset.dataset_dir)
    )

    clearml_dataset.upload(show_progress=True, verbose=False, output_url="s3://192.168.0.51:9000/MLTeam/Dataset/clearml", compression=None, chunk_size=None, max_workers=None, retries=3)

    clearml_dataset.finalize()