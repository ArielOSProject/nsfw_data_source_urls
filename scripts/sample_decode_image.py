# Typical setup to include TensorFlow.
import tensorflow as tf
from os import listdir
import os

# test script to try and decode images to be used for
# tensorflow training

train_dir = '/media/mikalackis/3719d14c-5eaf-4c7a-8230-25219a0b08c7/train/nsfw/'

count = 1
for filename in listdir(train_dir):
  if (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.JPEG') or filename.endswith('.JPG')):
    print('\rChecking file '+str(count), end='')
    try:
        # # Read an entire image file which is required since they're JPEGs, if the images
        # # are too large they could be split in advance to smaller files or use the Fixed
        # # reader to split up the file.
        # image_reader = tf.WholeFileReader()

        # # Read a whole file from the queue, the first returned value in the tuple is the
        # # filename which we are ignoring.
        # _, image_file = image_reader.read(filename_queue)

        # Decode the image as a JPEG file, this will turn it into a Tensor which we can
        # then use in training.
        image_contents = tf.io.read_file(train_dir+filename)
        image_tensor = tf.cond(
              tf.image.is_jpeg(image_contents),
              lambda: tf.io.decode_jpeg(image_contents, channels=3),
              lambda: tf.io.decode_image(image_contents, channels=3, expand_animations = False))
        if not tf.is_tensor(image_tensor):
            print('\nNot a good tensor', train_dir+filename)
        count = count+1
    except Exception as e: # work on python 2.x
      print('\nException: ', str(e))
      print('\nBad file:', train_dir+filename) # print out the names of corrupt files
      # UNCOMMENT THIS LINE TO REMOVE THE FILE
      os.remove(train_dir + filename)
  else:
    print('\nNOT AN IMAGE FILE: ', train_dir+filename)
    os.remove(train_dir+filename)

      