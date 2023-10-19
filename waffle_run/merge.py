from waffle_hub.dataset import Dataset



Dataset.merge(
        name= 'PeopleDataset_valid_v3.0.0',
        root_dir = None,
        src_names = [
                'PeopleDataset_FalldownNG_v1.0.0',
                'PeopleDataset_valid_v2.0.0'
                ],
        # src_names = [
        #         'PeopleDataset_Iwest_v1.1.0',
        #         'PeopleDataset_Iwest_v2.0.0',
        #         'PeopleDataset_KISA_HARD_v1.0.0',
        #         'PeopleDataset_KISA_v2.0.0',
        #         'PeopleDataset_SNU_v1.0.0',
        #         'PeopleDataset_YNCC_v1.0.1',
        #         'PeopleDataset_else_v1.0.0',
        #         'PeopleDataset_valid_v2.0.0'
        #         ],
        src_root_dirs = [None, None],
        task = 'object_detection'
        )

# Dataset.merge(
#         name= 'FireDataset_v2.0.0',
#         root_dir = None,
#         src_names = [
#                 'FireDataset_KISA_v2.0.1',
#                 'FireDataset_Aihub_v1.1.0',
#                 'FireDataset_Iwest_v1.0.0',
#                 'FireDataset_YNCC_v1.0.0',
#                 ],
#         src_root_dirs = [None, None, None, None],
#         task = 'object_detection'
#         )

# print(2475 + 1360 + 3476 + 19334+ 4195 + 1351 + 12098 == 43907)
# print(19334+3476+1360+2093+1351+4195+12098 == 43907)