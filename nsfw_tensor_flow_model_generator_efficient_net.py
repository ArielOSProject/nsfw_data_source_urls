import numpy as np

import tensorflow as tf
assert tf.__version__.startswith('2')

from tflite_model_maker import configs
from tflite_model_maker import image_classifier
from tflite_model_maker import ImageClassifierDataLoader
from tflite_model_maker import model_spec

import matplotlib.pyplot as plt

# inception_v3_spec = model_spec.ImageModelSpec(uri='https://tfhub.dev/google/imagenet/inception_v3/feature_vector/1')
# inception_v3_spec.input_image_shape = [299, 299]

image_train_data="data/train"
image_test_data="data/test"

train_data = ImageClassifierDataLoader.from_folder(image_train_data)
test_data = ImageClassifierDataLoader.from_folder(image_test_data)

validation_data, rest_data = train_data.split(0.8)

#model = image_classifier.create(train_data)

model = image_classifier.create(train_data, validation_data=validation_data, epochs=10)

model.summary()

loss, accuracy = model.evaluate(test_data)

model.export(export_dir='./tfmodel-efficient')

model.evaluate_tflite('./tfmodel/model.tflite', test_data)