import os, glob
import valohai as vh
import re
import tarfile
import shutil
import zipfile
import time

# inputs = {
#     "model": "",
# }

# vh.prepare(step="save step", image="mo0haned/net", default_inputs=inputs)
meta_file = ""
checkpoint_dir = ""

try:
    for file in vh.inputs("trained_model").paths():
        print(file)

except Exception as e:
    print("error", e)
