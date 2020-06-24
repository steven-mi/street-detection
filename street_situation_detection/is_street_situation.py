"""
street_situation_detection.is_street_situation.py
~~~~~~~~~~~~~~~~~~~~~~

This module contains methods and utilities for estimating whether a image was taken from a street
or not
"""
import argparse

import numpy as np
import tensorflow as tf

from street_situation_detection import model

def load_image(img_path) -> np.array:
    """
    This method gets a path to a image as an input and returns a array back.

    Args:
        img_path: path to a image as string

    Returns:
        img: a numpy array with size (1, 299, 299, 3)
    """
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=[299, 299])
    img = np.array(img)
    img = np.expand_dims(img, axis=0)
    return img


def is_street_situation(img) -> bool:
    """
    This method gets a numpy array as an input and returns a boolean back. The boolean is True
    if the given image was taken from a street and False otherwise.

    Args:
        img: numpy array with shape (1, 299, 299, 3)

    Returns:
        True if given image is taken from a street
    """
    prediction = model.predict(img)
    prediction_cat = np.where(prediction == 1)[0][0]
    if prediction_cat == 0:
        return False
    else:
        return True


def main() -> None:
    parser = argparse.ArgumentParser(description='is given image a street situation?')
    parser.add_argument('-p', '--img_path', required=True, type=str, help='path to an image')
    args = parser.parse_args()

    img = load_image(args.img_path)
    if is_street_situation(img):
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()
