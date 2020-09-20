"""
street_detection.is_street.py
~~~~~~~~~~~~~~~~~~~~~~

This module contains methods and utilities for estimating whether a image was taken from a street
or not
"""
import argparse

import numpy as np
import tensorflow as tf

from street_detection import model

from PIL import Image


def reorient_image(im):
    try:
        image_exif = im._getexif()
        image_orientation = image_exif[274]
        if image_orientation in (2, '2'):
            return im.transpose(Image.FLIP_LEFT_RIGHT)
        elif image_orientation in (3, '3'):
            return im.transpose(Image.ROTATE_180)
        elif image_orientation in (4, '4'):
            return im.transpose(Image.FLIP_TOP_BOTTOM)
        elif image_orientation in (5, '5'):
            return im.transpose(Image.ROTATE_90).transpose(Image.FLIP_TOP_BOTTOM)
        elif image_orientation in (6, '6'):
            return im.transpose(Image.ROTATE_270)
        elif image_orientation in (7, '7'):
            return im.transpose(Image.ROTATE_270).transpose(Image.FLIP_TOP_BOTTOM)
        elif image_orientation in (8, '8'):
            return im.transpose(Image.ROTATE_90)
        else:
            return im
    except (KeyError, AttributeError, TypeError, IndexError):
        return im


def load_image(img_path) -> np.array:
    """
    This method gets a path to a image as an input and returns a array back.

    Args:
        img_path: path to a image as string

    Returns:
        img: a numpy array with size (1, 299, 299, 3)
    """
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=[299, 299])
    img_reoriented = reorient_image(img)

    img_array = np.array(img_reoriented)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def is_street(img) -> bool:
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
    if is_street(img):
        print("True")
    else:
        print("False")
    exit(0)

if __name__ == "__main__":
    main()
