import numpy as np

import tensorflow as tf
assert tf.__version__.startswith('2')

from tflite_model_maker import configs
from tflite_model_maker import image_classifier
from tflite_model_maker import ImageClassifierDataLoader
from tflite_model_maker import model_spec

import matplotlib.pyplot as plt

inception_v3_spec = model_spec.ImageModelSpec(uri='https://tfhub.dev/google/inaturalist/inception_v3/feature_vector/4')

inception_v3_spec.input_image_shape = [299, 299]

image_train_data="data/train"
#image_test_data="data/test"

image_data_set = ImageClassifierDataLoader.from_folder(image_train_data)
train_data, rest_data = image_data_set.split(0.8)
validation_data, test_data = rest_data.split(0.5)

# test_data = ImageClassifierDataLoader.from_folder(image_test_data)
# train_data, validation_data = train_data.split(0.9)


#model = image_classifier.create(train_data)

model = image_classifier.create(train_data, model_spec=inception_v3_spec, validation_data=validation_data, epochs=5, shuffle=True)

model.summary()

loss, accuracy = model.evaluate(test_data)

model.export(export_dir='./tfmodel/', label_filename='nsfw_labels.txt')

model.evaluate_tflite('./tfmodel/model.tflite', test_data)