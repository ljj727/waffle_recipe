import sys

import re

from collections import defaultdict

from copy import deepcopy
from ultralytics.yolo.utils.torch_utils import model_info_for_loggers
from ultralytics.yolo.utils import LOGGER, SETTINGS, TESTS_RUNNING

import matplotlib.image as mpimg
import matplotlib.pyplot as plt


try:
    import clearml
    from clearml import Task
    from clearml.binding.frameworks.pytorch_bind import PatchPyTorchModelIO
    from clearml.binding.matplotlib_bind import PatchedMatplotlib

    # assert hasattr(clearml, '__version__')  # verify package is not directory
    # assert not TESTS_RUNNING  # do not log pytest
    # assert SETTINGS['clearml'] is True  # verify integration is enabled
except (ImportError, AssertionError):
    clearml = None

# Trainer callbacks ----------------------------------------------------------------------------------------------------

def _log_debug_samples(files, title='Debug Samples'):
    task = Task.current_task()
    if task:
        for f in files:
            if f.exists():
                it = re.search(r'_batch(\d+)', f.name)
                iteration = int(it.groups()[0]) if it else 0
                task.get_logger().report_image(title=title,
                                               series=f.name.replace(it.group(), ''),
                                               local_path=str(f),
                                               iteration=iteration)

def _log_plot(title, plot_path):
    """
    Log an image as a plot in the plot section of ClearML.

    Args:
        title (str): The title of the plot.
        plot_path (str): The path to the saved image file.
    """
    img = mpimg.imread(plot_path)
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1], frameon=False, aspect='auto', xticks=[], yticks=[])
    ax.imshow(img)
    Task.current_task().get_logger().report_matplotlib_figure(title=title,
                                                              series='',
                                                              figure=fig,
                                                              report_interactive=False)


def on_pretrain_routine_start(trainer):
    try:
        task = Task.current_task()
        if task:
            # Make sure the automatic pytorch and matplotlib bindings are disabled!
            # We are logging these plots and model files manually in the integration
            PatchPyTorchModelIO.update_current_task(None)
            PatchedMatplotlib.update_current_task(None)
        else:
            task = Task.init(project_name=trainer.args.project or 'YOLOv8',
                             task_name=trainer.args.name,
                             tags=['YOLOv8', trainer.args.task],
                             output_uri=True,
                             reuse_last_task_id=False,
                             auto_connect_frameworks={
                                 'pytorch': False,
                                 'matplotlib': False})
            LOGGER.warning('ClearML Initialized a new task. If you want to run remotely, '
                           'please add clearml-init and connect your arguments before initializing YOLO.')
        task.connect(vars(trainer.args), name='General')
    except Exception as e:
        LOGGER.warning(f'WARNING ⚠️ ClearML installed but not initialized correctly, not logging this run. {e}')


def on_fit_epoch_end(trainer):
    """Reports model information to logger at the end of an epoch."""
    task = Task.current_task()
    if task:
        # You should have access to the validation bboxes under jdict
        task.get_logger().report_scalar(title='Epoch Time',
                                        series='Epoch Time',
                                        value=trainer.epoch_time,
                                        iteration=trainer.epoch)
        if trainer.epoch == 0:
            for k, v in model_info_for_loggers(trainer).items():
                task.get_logger().report_single_value(k, v)


def on_train_epoch_end(trainer):
    """Log metrics and save images at the end of each training epoch."""
    # wb.run.log(trainer.label_loss_items(trainer.tloss, prefix='train'), step=trainer.epoch + 1)
    # wb.run.log(trainer.lr, step=trainer.epoch + 1)
    if trainer.epoch == 1:
        print("dsajkl")
        # _log_plots(trainer.plots, step=trainer.epoch + 1)
        # _log_plot(title=f.stem, plot_path=f)


def on_train_end(trainer):
    """Save the best model as an artifact at end of training."""
    task = Task.current_task()
    if task:
        # Log final results, CM matrix + PR plots
        files = [
            'results.png', 'confusion_matrix.png', 'confusion_matrix_normalized.png',
            *(f'{x}_curve.png' for x in ('F1', 'PR', 'P', 'R'))]
        files = [(trainer.save_dir / f) for f in files if (trainer.save_dir / f).exists()]  # filter
        for f in files:
            _log_plot(title=f.stem, plot_path=f)
        # Report final metrics
        for k, v in trainer.validator.metrics.results_dict.items():
            task.get_logger().report_single_value(k, v)
        # Log the final model
        task.update_output_model(model_path=str(trainer.best), model_name=trainer.args.name, auto_delete_file=False)


def on_val_end(validator):
    if Task.current_task():
        # Log val_labels and val_pred
        _log_debug_samples(sorted(validator.save_dir.glob('val*.jpg')), 'Validation')
#---
def on_pretrain_routine_end(trainer):
    """Called after the pretraining routine ends."""
    pass


def on_train_start(trainer):
    """Called when the training starts."""
    pass


def on_train_epoch_start(trainer):
    """Called at the start of each training epoch."""
    pass


def on_train_batch_start(trainer):
    """Called at the start of each training batch."""
    pass


def optimizer_step(trainer):
    """Called when the optimizer takes a step."""
    pass


def on_before_zero_grad(trainer):
    """Called before the gradients are set to zero."""
    pass


def on_train_batch_end(trainer):
    """Called at the end of each training batch."""
    pass

def on_model_save(trainer):
    """Called when the model is saved."""
    pass

def on_params_update(trainer):
    """Called when the model parameters are updated."""
    pass


def teardown(trainer):
    """Called during the teardown of the training process."""
    pass


default_callbacks = {
    # Run in trainer
    'on_pretrain_routine_start': [on_pretrain_routine_start],
    'on_pretrain_routine_end': [on_pretrain_routine_end],
    'on_train_start': [on_train_start],
    'on_train_epoch_start': [on_train_epoch_start],
    'on_train_batch_start': [on_train_batch_start],
    'optimizer_step': [optimizer_step],
    'on_before_zero_grad': [on_before_zero_grad],
    'on_train_batch_end': [on_train_batch_end],
    'on_train_epoch_end': [on_train_epoch_end],
    'on_fit_epoch_end': [on_fit_epoch_end],  # fit = train + val
    'on_model_save': [on_model_save],
    'on_train_end': [on_train_end],
    'on_params_update': [on_params_update],
    'on_val_end': [on_val_end],
    'teardown': [teardown],
}

def clearml_logs():
    """
    Return a copy of the default_callbacks dictionary with lists as default values.

    Returns:
        (defaultdict): A defaultdict with keys from default_callbacks and empty lists as default values.
    """
    return defaultdict(list, deepcopy(default_callbacks))