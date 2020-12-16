# Python program to rename all file 
# names in your directory 
import os 
import uuid
uuid.uuid4()

os.chdir('/media/mikalackis/3719d14c-5eaf-4c7a-8230-25219a0b08c71/rips/') 
#os.chdir('/home/mikalackis/Downloads/test_images/') 
print(os.getcwd()) 

for f in os.listdir(): 
	f_name, f_ext = os.path.splitext(f) 
	f_name = uuid.uuid4()

	new_name = '{}{}'.format(f_name, f_ext) 
	os.rename(f, new_name) 
