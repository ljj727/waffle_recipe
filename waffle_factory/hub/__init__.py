import os

os.getenv("CLEARML")

def start(key=''):
    """
    Start training models with Ultralytics HUB (DEPRECATED).

    Args:
        key (str, optional): A string containing either the API key and model ID combination (apikey_modelid),
                               or the full model URL (https://hub.ultralytics.com/models/apikey_modelid).
    """
    api_key, model_id = key.split('_')
    print.warning(f"""
WARNING ⚠️ ultralytics.start() is deprecated after 8.0.60. Updated usage to train Ultralytics HUB models is:

from ultralytics import YOLO, hub

hub.login('{api_key}')
model = YOLO('{HUB_WEB_ROOT}/models/{model_id}')
model.train()""")