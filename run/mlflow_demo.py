import mlflow
import os

mlflow.set_tracking_uri("http://0.0.0.0:5000")
remote_server_uri = "http://0.0.0.0:5000" # set to your server URI
mlflow.set_tracking_uri(remote_server_uri)
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://0.0.0.0:8080"
os.environ["AWS_ACCESS_KEY_ID"] = "snuailab"
os.environ["AWS_SECRET_ACCESS_KEY"] = "init123!!"
mlflow.set_experiment("Laycom")



import yaml

# YAML 파일 읽기
config_path = '/home/ljj/waffle/ultralytics/custom_detect.yaml'
with open(config_path, 'r') as file:
    yaml_content = yaml.safe_load(file)

log_vals = [
0.1234,
0.5678,
0.2101,
0.1121,
0.3141,
]
log_keys = [
            'train/loss',
            'metrics/mAP_0.5',
            'metrics/mAP_0.5_0.95',  # metrics
            'val/loss',
            'val/mAP_0.5',
            ]  # params

x = dict(zip(log_keys, log_vals))


for k,v in yaml_content.items():
    mlflow.log_param(k,v)

for i in range(1, 5):
    for k,v in x.items():
        print(k,(v+0.08*i))
        mlflow.log_metric(k,(v+0.08*i), step=i)


mlflow.log_artifacts(
    local_dir = "/home/ljj/waffle/hubs/laycom/PeopleDet_v2.1.0",
)
