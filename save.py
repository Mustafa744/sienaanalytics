import os, glob
import valohai as vh
import tarfile
import shutil
import zipfile
import time

inputs = {
    "model": "",
}

vh.prepare(step="save step", image="mo0haned/net", default_inputs=inputs)

try:
    print(vh.inputs("model").paths())
except Exception as e:
    print("error", e)
try:
    print(i for i in vh.inputs("model").paths())
    for image_path in vh.inputs("model").paths():
        print(image_path)

except Exception as e:
    print("error", e)

# try:
#     unzip = zipfile.ZipFile(vh.inputs("model").path(), "r")
#     unzip.extractall(vh.outputs().path("exctracted_model"))
#     print("extracted model to: " + vh.outputs().path("exctracted_model"))
# except Exception as e:
#     print("error extracting model", e)
#     print(os.listdir(vh.inputs("model").path()))
