import logging
from pathlib import Path

from waffle.callbacks import LoopCallback
from waffle.util.file import io

logger = logging.getLogger(__name__)


class InferenceCallback(LoopCallback):
    def __init__(self, output_path: str = "results.json"):
        super().__init__()

        self.output_path = output_path

    def setup(self, *args, **kwargs):
        # Config settings
        # Config Save
        pass

    def before_loop(self, *args, **kwargs):
        pass

    def on_loop_start(self, total_steps: int, *args, **kwargs):
        pass

    def on_step_start(self, *args, **kwargs):
        pass

    def on_step_end(
        self,
        current_step: int = None,
        batch_images=None,
        batch_image_resize_infos=None,
        batch_image_infos=None,
        batch_annotations=None,
        batch_results=None,
        *args,
        **kwargs,
    ):
        pass

    def on_loop_end(self, *args, **kwargs):
        pass

    def after_loop(self, total_results: list[dict] = None, *args, **kwargs):
        try:
            Path(self.output_path).parent.mkdir(parents=True, exist_ok=True)
            io.save_json(total_results, self.output_path)
        except Exception as e:
            logger.error(f"Failed to save results: {e}")

    def teardown(self, *args, **kwargs):
        pass