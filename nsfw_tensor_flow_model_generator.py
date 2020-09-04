import numpy as np

import tensorflow as tf
assert tf.__version__.startswith('2')

from tflite_model_maker import configs
from tflite_model_maker import image_classifier
from tflite_model_maker import ImageClassifierDataLoader
from tflite_model_maker import model_spec

import matplotlib.pyplot as plt

image_train_data="data/train"
image_test_data="data/test"

train_data = ImageClassifierDataLoader.from_folder(image_train_data)
test_data = ImageClassifierDataLoader.from_folder(image_test_data)

model = image_classifier.create(train_data)

loss, accuracy = model.evaluate(test_data)

model.export(export_dir='./tfmodel')