import sys
# import wandb as wb
from collections import defaultdict
from copy import deepcopy

# Predictor callbacks --------------------------------------------------------------------------------------------------
def on_predict_start(predictor):
    wb.config.update(vars(predictor.args))
    wb.run.tags = ["YOLOv8"] + [predictor.args.task] + [predictor.args.mode] + [sys.argv[1]]

def on_predict_batch_start(predictor):
    """Called at the start of each prediction batch."""
    pass

def on_predict_batch_end(predictor):
    """Called at the end of each prediction batch."""
    pass

def on_predict_postprocess_end(predictor):
    """Called after the post-processing of the prediction ends."""
    pass

def on_predict_end(predictor):
    """Called when the prediction ends."""
    wb.run.summary['imgsz'] = predictor.imgsz
    predictor.plotted_img
    wb.run.log({name.stem})
    pass


default_callbacks = {
    # Run in predictor
    'on_predict_start': [on_predict_start],
    'on_predict_batch_start': [on_predict_batch_start],
    'on_predict_postprocess_end': [on_predict_postprocess_end],
    'on_predict_batch_end': [on_predict_batch_end],
    'on_predict_end': [on_predict_end],
}

def pred_callbacks():
    """
    Return a copy of the default_callbacks dictionary with lists as default values.

    Returns:
        (defaultdict): A defaultdict with keys from default_callbacks and empty lists as default values.
    """
    return defaultdict(list, deepcopy(default_callbacks))