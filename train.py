import os, glob
import valohai as vh
import tarfile
import shutil
import zipfile
import time
from threading import Thread

data_dir = vh.inputs("tfrecords").path()
data_dir = data_dir.split("/")
data_dir = data_dir[:-1]
data_dir = "/".join(data_dir)
data_dir = f"{data_dir}/"

use_tpu = vh.parameters("use_tpu").value
train_steps = vh.parameters("train_steps").value
# model_dir = vh.parameters('model_dir').value
num_label_classes = vh.parameters("num_label_classes").value
train_batch_size = vh.parameters("train_batch_size").value

print(data_dir)
os.system(
    f"""python /home/tensorflow/models/research/models/official/efficientnet/main.py --use_tpu=False --data_dir={data_dir} --model_dir=/home/tensorflow/models/research/new/ --train_steps=10 --skip_host_call=true --num_label_classes=5 --train_batch_size=8 """
)
shutil.make_archive(
    vh.outputs().path("efficientnet"), "zip", "/home/tensorflow/models/research/new/"
)
vh.logger.info("[info]" + vh.outputs().path("efficientnet"))
# os.system(f"mv /home/tensorflow/models/research/new/ {vh.outputs('tfrecord').path('efficientnet')}")
