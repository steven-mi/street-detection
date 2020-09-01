# Street Detection
[![Build Status](https://travis-ci.com/steven-mi/street-situation-detection.svg?token=v7d1qysqnBpw9q4zGDjA&branch=master)](https://travis-ci.com/steven-mi/street-situation-detection)

![img](https://images.unsplash.com/photo-1475998776787-d22fa84424b6?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1359&q=80)

This project deals with the problem of detecting street images (images which are taken on streets). It is a package build around the model achieved from [train-street-detection](https://github.com/steven-mi/train-street-detection). To make the model useable for other services, a package is built around. Additionally, the model is loaded to the GPU during import and not inference. Therefore the time for inference is minimized.

## Getting started
This package is not and will not be hosted on PyPI. You will have to clone this repository and install this package by hand:

```python
git clone https://github.com/steven-mi/street-detection.git
pip install .
```

## Usage
After downloading this package, you will be able to use the `is_street` command. It gets an image path and prints True if the given image is taken from a street and False otherwise.
```bash
is_street -p PATH_TO_YOUR_IMAGE
```
You can also use this package with Python. Just copy the following snippet:

```python
from street_detection.is_street import load_image, is_street # initializing our model

img_path = "path_to_your_image"
img = load_image(img_path) # Numpy Array

is_street(img) # boolean - True/False
```
