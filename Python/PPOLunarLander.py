# instead of:
# apt install python-opengl
# apt install ffmpeg
# apt install xvfb

# installing on Mac:
# pip install PyOpenGL PyOpenGL_accelerate
# pip install ffmpeg                      
# brew install --cask xquartz


from pyvirtualdisplay import Display

virtual_display = Display(visible=0, size=(1400, 900))
virtual_display.start()

from huggingface_hub import HfApi, upload_folder
from huggingface_hub.repocard import metadata_eval_result, metadata_save

from pathlib import Path
import datetime
import tempfile
import json
import shutil
import imageio

from wasabi import Printer
msg = Printer()

# Adding HuggingFace argument
# parser.add_argument("--repo-id", type=str, default="ThomasSimonini/ppo-CartPole-v1", help="id of the model repository from the Hugging Face Hub {username/repo_name}")