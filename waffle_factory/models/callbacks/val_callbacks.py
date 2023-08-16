# import sys
# from collections import defaultdict
# from copy import deepcopy

# _processed_plots = {}

# def _log_plots(plots, step):
#     for name, params in plots.items():
#         timestamp = params['timestamp']
#         if _processed_plots.get(name, None) != timestamp:
#             wb.run.log({name.stem: wb.Image(str(name))}, step=step)
#             _processed_plots[name] = timestamp


# def on_val_start(validator):
#     wb.run.name = f"{sys.argv[1]}-{validator.save_dir.stem}"
#     wb.config.update(vars(validator.args))
#     wb.run.tags = ["YOLOv8"] + [validator.args.task] + [validator.args.mode] + [sys.argv[1]]
#     wb.run.save()

# def on_val_batch_start(validator):
#     """Called at the start of each validation batch."""
#     pass

# def on_val_batch_end(validator):
#     """Called at the end of each validation batch."""
#     pass



# default_callbacks = {
#     # Run in validator
#     'on_val_start': [on_val_start],
#     'on_val_batch_start': [on_val_batch_start],
#     'on_val_batch_end': [on_val_batch_end],
#     'on_val_end': [on_val_end],
#     }


# def val_callbacks():
#     return defaultdict(list, deepcopy(default_callbacks))