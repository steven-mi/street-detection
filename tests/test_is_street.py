"""
tests.test_is_street.py
~~~~~~~~~~~~~~~~~~~~

Test suite for the is_street.py module that calculates whether a image was taken from a street
or not.
"""
import os
import numpy as np

import pytest

from street_detection.is_street import is_street, load_image


def test_load_image_successful():
    this_dir, _ = os.path.split(__file__)
    img_path = os.path.join(this_dir, "test_data", "img.jpeg")
    img = load_image(img_path)
    if len(img) > 0:
        assert True
    else:
        assert False


def test_load_image_fail():
    with pytest.raises(FileNotFoundError):
        load_image("1231231312")


def test_is_street_situation_successful_rgb():
    img = np.random.randint(0, 255, [1, 299, 299, 3])
    street = is_street(img)
    assert street is not None


def test_is_street_situation_fail_grayscale():
    img = np.random.randint(0, 255, [1, 299, 299, 1])
    with pytest.raises(ValueError):
        is_street(img)


def test_is_street_situation_fail():
    img = np.random.randint(0, 255, [299, 299, 1])
    with pytest.raises(ValueError):
        is_street(img)
