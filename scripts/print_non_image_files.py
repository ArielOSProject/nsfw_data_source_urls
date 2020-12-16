from os import listdir
from PIL import Image
import warnings
import os

# prints all files that do not match extensions defined
# in if condition

warnings.simplefilter('error', Image.DecompressionBombWarning)

train_dir = '/home/mikalackis/Downloads/rips/'

count = 1
for filename in listdir(train_dir):
  if not (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.JPEG') or filename.endswith('.JPG')):
    print('Bad file: ', train_dir+filename)
    os.remove(train_dir + filename)