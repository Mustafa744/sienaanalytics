import os,glob
import valohai as vh
import tarfile
import shutil
import zipfile
import time


print(vh.inputs('model'))
print(vh.inputs('model').path())

unzip = zipfile.ZipFile(vh.inputs('model').path(), 'r')
unzip.extractall(vh.outputs().path("exctracted_model"))
print("extracted model to: " + vh.outputs().path("exctracted_model")) 