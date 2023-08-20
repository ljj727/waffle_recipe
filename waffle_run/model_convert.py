from ultralytics import YOLO
import torch

model = YOLO(model='/home/ljj/waffle/hubs/VihicleDet_v1.0.0/weights/best_ckpt.pt')
 

"""Save model checkpoints based on various conditions."""
a = model.ckpt
from copy import deepcopy
import datetime
ckpt = {
    'epoch': -1,
    'best_fitness': None,
    'model': deepcopy(a['ema']),
    'ema': None,
    'updates': None,
    'optimizer': None,
    'train_args': a['train_args'],  # save as dict
    'date': datetime.datetime.now().isoformat(),
    'version': a['version']}

 

# Use dill (if exists) to serialize the lambda functions where pickle does not do this
try:
    import dill as pickle
except ImportError:
    import pickle

 

# Save last, best and delete
torch.save(ckpt, './best_ckpt.pt', pickle_module=pickle)
del ckpt