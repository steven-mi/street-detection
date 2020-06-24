# Street Situation Detection
TODO

## Getting started

```python
git clone https://github.com/steven-mi/street-situation-detection.git
pip install .
```

## Usage
```bash
is_street_situation -h
```

```python
from street_situation_detection.is_street_situation import load_image, is_street_situation
img_path = "path_to_your_image"
img = load_image(img_path)

if is_street_situation(img):
    print("True")
else:
    print("False") 
```