import os
import cv2

# Set the directory containing the images
directory = 'faces'

# Get a list of all the images in the directory
images = os.listdir(directory)

# Iterate through the images and display them one by one
for image in images:
  img = cv2.imread(os.path.join(directory, image))
  cv2.imshow('image', img)
  cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
