# USAGE
# python generate_images.py --image dog.jpg --output generated_dataset/dogs
# python generate_images.py --image cat.jpg --output generated_dataset/cats

# import the necessary packages
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
#from keras.layers import GaussianNoise
import numpy as np
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
ap.add_argument("-o", "--output", required=True,
	help="path to output directory to store augmentation examples")
ap.add_argument("-t", "--total", type=int, default=100,
	help="# of training samples to generate")
args = vars(ap.parse_args())

# load the input image, convert it to a NumPy array, and then
# reshape it to have an extra dimension
print("[INFO] loading example image...")
image = load_img(args["image"])
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

# construct the image generator for data augmentation then
# initialize the total number of images generated thus far
aug = ImageDataGenerator(
	rotation_range=0, # lower to 0
	#zoom_range=0.01, # lower to 0
	#width_shift_range=3, # keep low
	height_shift_range=0, # keep low
	#shear_range=30, #  (in degrees)
	#horizontal_flip=True,
	#brightness_range=(1.01,0.99), 
	fill_mode="reflect") # reflect
	
total = 0

# construct the actual Python generator
print("[INFO] generating images...")
imageGen = aug.flow(image, batch_size=1, save_to_dir=args["output"],
	save_prefix="image", save_format="jpg")

# loop over examples from our image data augmentation generator
for image in imageGen:
	# increment our counter
	total += 1

	# if we have reached the specified number of examples, break
	# from the loop
	if total == args["total"]:
		break