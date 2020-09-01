"""
street_detection
~~~~~~

The street_detection - a Python package that is intended
to be used as a image analysing tool It can detect if a image was taken
from a street or not.
"""
import os
import requests
import zipfile
import io

import tensorflow as tf


def download_and_extract(zip_file_url, output_folder):
    r = requests.get(zip_file_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(output_folder)


this_dir, _ = os.path.split(__file__)
model_path = os.path.join(this_dir, "model", "street-situation-network")
model_link = "https://github.com/steven-mi/street-situation-detection/releases/download/v1/street-situation-network.zip"
if not os.path.isdir(model_path):
    os.makedirs(model_path)
    download_and_extract(model_link, model_path)

model = tf.keras.models.load_model(model_path)
