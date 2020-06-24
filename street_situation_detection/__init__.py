"""
street_situation_detection
~~~~~~

The street_situation_detection - a Python package that is intended
to be used as a image analysing tool It can detect if a image was taken
from a street or not.
"""
import os

import tensorflow as tf

this_dir, _ = os.path.split(__file__)
model_path = os.path.join(this_dir, "model", "street-situation-network")
model = tf.keras.models.load_model(model_path)