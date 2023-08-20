from clearml.automation.controller import PipelineDecorator
from clearml import TaskTypes

# Waffle Dataset Download
@PipelineDecorator.component(return_values=["dataset1_name"],name='Public Dataset', cache=True, task_type=TaskTypes.data_processing)
def step_one(id: str, extra: int = 43):
    print("step_one")
    from pathlib import Path
    from clearml import Dataset as cd

    clearml_dataset=cd.get(dataset_id=id)
    try: 
        dataset = clearml_dataset.get_mutable_local_copy("/home/ljj/waffle/datasets/people")
    except:
        dataset = "/home/ljj/waffle/datasets/people"
    
    dataset1_name = Path(dataset).stem

    return dataset1_name

@PipelineDecorator.component(return_values=["dataset2_name"], name='Project Dataset', cache=True, task_type=TaskTypes.data_processing)
def step_two(id: str, extra: int = 43):
    print("step_two")
    from pathlib import Path
    from clearml import Dataset as cd

    clearml_dataset=cd.get(dataset_id=id)
    try: 
        dataset = clearml_dataset.get_mutable_local_copy("/home/ljj/waffle/datasets/Iwest")
    except:
        dataset = "/home/ljj/waffle/datasets/Iwest"
    
    dataset2_name = Path(dataset).stem

    return dataset2_name

@PipelineDecorator.component(
    return_values=["dataset_name"], cache=True, name='Merge Dataset & Export', task_type=TaskTypes.data_processing
)
def step_three(data1_name, data2_name):
    print("step_three")
    # make sure we have pandas for this step, we need it to use the data_frame
    from waffle_hub.dataset import Dataset

    dataset = Dataset.merge(
            name= 'asdfzxcv',
            root_dir = None,
            src_names = [data1_name, data2_name],
            src_root_dirs = [None, None],
            task = 'object_detection'
            )
    
    dataset.split(
    train_ratio = 0.9,
    val_ratio = 0.1,
    )

    dataset.export('YOLO')


    return dataset

@PipelineDecorator.component(return_values=["model"], cache=True, name='Train', task_type=TaskTypes.training)
def step_four(dataset):
    from ultralytics import YOLO

    data = str(dataset.export_dir / 'YOLO' / 'data.yaml')

    try:
        model = YOLO("yolov8s.pt", task="detect")
        model.train(
            data=data,
            epochs=3,
            batch=64,
            imgsz=640,
            lr0=0.01,
            lrf=0.01,
            device="0",
            workers=16,
            seed=0,
            verbose=True,
            project="test",
            name="v1.0.0",
            **{}
        )
    except Exception as e:
        print(e)
        raise e

    print("step_four")
    # make sure we have pandas for this step, we need it to use the data_frame
    return model


# @PipelineDecorator.component(return_values=["accuracy"], cache=True, task_type=TaskTypes.qc)
# def step_four(model, X_data, Y_data):
#     from sklearn.linear_model import LogisticRegression  # noqa
#     from sklearn.metrics import accuracy_score

#     Y_pred = model.predict(X_data)
#     return accuracy_score(Y_data, Y_pred, normalize=True)


@PipelineDecorator.pipeline(name="custom pipeline logic", project="examples", version="0.0.5")
def executing_pipeline(pickle_url, mock_parameter="mock"):
    print("pipeline args:", pickle_url, mock_parameter)

    # Use the pipeline argument to start the pipeline and pass it ot the first step
    print("launch step one")
    data1_name = step_one('c8ac3438307a4b969a3422bc7c30f664')
    print("launch step two")
    data2_name = step_two('f4f312eae83e498bb95f5e3eccccf38b')

    print("launch step three")
    dataset = step_three(data1_name, data2_name)

    print("launch step four")
    model = step_four(dataset)

    # Notice since we are "printing" the `model` object,
    # we actually deserialize the object from the third step, and thus wait for the third step to complete.

    # print("launch step five")
    # accuracy = 100 * step_four(model, X_data=X_test, Y_data=y_test)

    # Notice since we are "printing" the `accuracy` object,
    # we actually deserialize the object from the fourth step, and thus wait for the fourth step to complete.
    # print(f"Accuracy={accuracy}%")


if __name__ == "__main__":
    PipelineDecorator.run_locally()

    # Start the pipeline execution logic.
    executing_pipeline(
        pickle_url="https://github.com/allegroai/events/raw/master/odsc20-east/generic/iris_dataset.pkl",
    )

    print("process completed")