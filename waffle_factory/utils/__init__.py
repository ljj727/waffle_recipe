import os
from pathlib import Path
import platform
import uuid
from typing import Union
import yaml
import re


# PyTorch Multi-GPU DDP Constants
RANK = int(os.getenv('RANK', -1))
LOCAL_RANK = int(os.getenv('LOCAL_RANK', -1))  # https://pytorch.org/docs/stable/elastic/run.html

# Other Constants
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # YOLO
ASSETS = ROOT / 'assets'  # default images
DEFAULT_CFG_PATH = ROOT / 'cfg/default.yaml'
NUM_THREADS = min(8, max(1, os.cpu_count() - 1))  # number of YOLOv5 multiprocessing threads
AUTOINSTALL = str(os.getenv('YOLO_AUTOINSTALL', True)).lower() == 'true'  # global auto-install mode
VERBOSE = str(os.getenv('YOLO_VERBOSE', True)).lower() == 'true'  # global verbose mode
TQDM_BAR_FORMAT = '{l_bar}{bar:10}{r_bar}'  # tqdm bar format
LOGGING_NAME = 'ultralytics'
MACOS, LINUX, WINDOWS = (platform.system() == x for x in ['Darwin', 'Linux', 'Windows'])  # environment booleans
ARM64 = platform.machine() in ('arm64', 'aarch64')  # ARM64 booleans



def is_dir_writeable(dir_path: Union[str, Path]) -> bool:
    """
    Check if a directory is writeable.

    Args:
        dir_path (str | Path): The path to the directory.

    Returns:
        (bool): True if the directory is writeable, False otherwise.
    """
    return os.access(str(dir_path), os.W_OK)

def parse_root_dir(path):
    if path:
        return Path(path)
    elif os.getenv("WAFFLE_HUB_ROOT_DIR", None):
        return Path(os.getenv("WAFFLE_HUB_ROOT_DIR"))

def get_user_config_dir(sub_dir='waffle'):
    """
    Get the user config directory.

    Args:
        sub_dir (str): The name of the subdirectory to create.

    Returns:
        (Path): The path to the user config directory.
    """
    # Return the appropriate config directory for each operating system
    # if os.getenv("WAFFLE_HUB_ROOT_DIR", None):
    #     path = Path(os.getenv("WAFFLE_HUB_ROOT_DIR"))
    
    # else:
    if WINDOWS:
        path = Path.home() / 'AppData' / 'Roaming' / sub_dir
    elif MACOS:  # macOS
        path = Path.home() / 'Library' / 'Application Support' / sub_dir
    elif LINUX:
        path = Path.home() / '.config' / sub_dir
    else:
        raise ValueError(f'Unsupported operating system: {platform.system()}')

    # GCP and AWS lambda fix, only /tmp is writeable
    if not is_dir_writeable(path.parent):
        print.warning(f"WARNING ⚠️ user config directory '{path}' is not writeable, defaulting to '/tmp' or CWD."
                       'Alternatively you can define a YOLO_CONFIG_DIR environment variable for this path.')
        path = Path('/tmp') / sub_dir if is_dir_writeable('/tmp') else Path().cwd() / sub_dir

    # Create the subdirectory if it does not exist
    path.mkdir(parents=True, exist_ok=True)

    return path


USER_CONFIG_DIR = Path(os.getenv('YOLO_CONFIG_DIR') or get_user_config_dir())  # Ultralytics settings dir
SETTINGS_YAML = USER_CONFIG_DIR / 'settings.yaml'

def get_git_dir():
    """
    Determines whether the current file is part of a git repository and if so, returns the repository root directory.
    If the current file is not part of a git repository, returns None.

    Returns:
        (Path | None): Git root directory if found or None if not found.
    """
    for d in Path(__file__).parents:
        if (d / '.git').is_dir():
            return d


def yaml_load(file='data.yaml', append_filename=False):
    """
    Load YAML data from a file.

    Args:
        file (str, optional): File name. Default is 'data.yaml'.
        append_filename (bool): Add the YAML filename to the YAML dictionary. Default is False.

    Returns:
        (dict): YAML data and file name.
    """
    with open(file, errors='ignore', encoding='utf-8') as f:
        s = f.read()  # string

        # Remove special characters
        if not s.isprintable():
            s = re.sub(r'[^\x09\x0A\x0D\x20-\x7E\x85\xA0-\uD7FF\uE000-\uFFFD\U00010000-\U0010ffff]+', '', s)

        # Add YAML filename to dict and return
        data = yaml.safe_load(s) or {}  # always return a dict (yaml.safe_load() may return None for empty files)
        if append_filename:
            data['yaml_file'] = str(file)
        return data


def yaml_save(file='data.yaml', data=None):
    """
    Save YAML data to a file.

    Args:
        file (str, optional): File name. Default is 'data.yaml'.
        data (dict): Data to save in YAML format.

    Returns:
        (None): Data is saved to the specified file.
    """
    if data is None:
        data = {}
    file = Path(file)
    if not file.parent.exists():
        # Create parent directories if they don't exist
        file.parent.mkdir(parents=True, exist_ok=True)

    # Convert Path objects to strings
    for k, v in data.items():
        if isinstance(v, Path):
            data[k] = str(v)

    # Dump data to file in YAML format
    with open(file, 'w') as f:
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)

class SettingsManager(dict):
    """
    Manages Waffle settings stored in a YAML file.

    Args:
        file (str | Path): Path to the Ultralytics settings YAML file. Default is USER_CONFIG_DIR / 'settings.yaml'.
        version (str): Settings version. In case of local version mismatch, new default settings will be saved.
    """

    def __init__(self, file=SETTINGS_YAML, version='0.0.1'):
        import copy
        import hashlib

        git_dir = get_git_dir()
        root = git_dir or Path()
        if os.getenv("WAFFLE_ROOT_DIR", None):
            waffle_root = Path(os.getenv("WAFFLE_ROOT_DIR"))
            datasets_root = waffle_root / 'datasets'
            hub_root = waffle_root / 'hubs'
        else:
            datasets_root = (root.parent if git_dir and is_dir_writeable(root.parent) else root).resolve() / 'datasets' 
            hub_root = (root.parent if git_dir and is_dir_writeable(root.parent) else root).resolve() / 'hubs'

        self.file = Path(file)
        self.version = version
        self.defaults = {
            'settings_version': version,
            'datasets_dir': datasets_root,
            'hub_dir': hub_root,
            'uuid': hashlib.sha256(str(uuid.getnode()).encode()).hexdigest(),
            'sync': True,
            'clearml': True,
            "s3_url": "s3://192.168.0.51:9000/MLTeam/Dataset/clearml"}

        super().__init__(copy.deepcopy(self.defaults))

        if not self.file.exists():
            self.save()

        self.load()

    def load(self):
        """Loads settings from the YAML file."""
        super().update(yaml_load(self.file))

    def save(self):
        """Saves the current settings to the YAML file."""
        yaml_save(self.file, dict(self))

    def update(self, *args, **kwargs):
        """Updates a setting value in the current settings."""
        super().update(*args, **kwargs)
        self.save()

    def reset(self):
        """Resets the settings to default and saves them."""
        self.clear()
        self.update(self.defaults)
        self.save()

SETTINGS = SettingsManager()  # initialize settings