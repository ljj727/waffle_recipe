
# create example dataset
from waffle_hub.dataset import Dataset as wd
from clearml import Dataset as cd

clearml_dataset= cd.get(
    dataset_project='Public',
    dataset_name='PeopleDataset'
)