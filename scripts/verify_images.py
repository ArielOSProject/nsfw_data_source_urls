from os import listdir
from PIL import Image
import warnings
import os

warnings.simplefilter('error', Image.DecompressionBombWarning)

train_dir = '/media/mikalackis/3719d14c-5eaf-4c7a-8230-25219a0b08c7/train/nsfw/'

count = 1
for filename in listdir(train_dir):
  if (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.jpeg')):
    print('\rChecking file '+str(count), end='')
    try:
      im = Image.open(train_dir+filename) # open the image file
      im.verify() #I perform also verify, don't know if he sees other types o defects
      im.close() #reload is necessary in my case
      im = Image.open(train_dir+filename) 
      im.transpose(Image.FLIP_LEFT_RIGHT)
      im.close()
      count = count+1
    except Exception as e:
      print('\nMessage: ', str(e))
      print('\nBad file:', train_dir+filename) # print out the names of corrupt files
      # UNCOMMENT THIS LINE TO REMOVE THE FILE
      # os.remove(train_dir + filename)