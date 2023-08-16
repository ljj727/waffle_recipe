from waffle_hub.dataset import Dataset

Dataset.merge(
        name= 'VihicleDataset_v1.0.0',
        root_dir = None,
        src_names = ['AihubHighway_Vihicle_v1.1.0', 'AihubCityload_Vihicle_v1.1.0'],
        src_root_dirs = [None, None],
        task = 'object_detection'
        )