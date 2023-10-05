import cv2
import yaml
import numpy as np

# Load the image to be undistorted
img = cv2.imread("distorted.jpg")

with open('calibration_matrix.yaml') as f:
    data = yaml.safe_load(f)

camera_matrix = np.array(data['camera_matrix'])
distance_coefficients = np.array(data['distance_coefficients'])

# get the maps for remap function
mapx, mapy = cv2.initUndistortRectifyMap(camera_matrix, distance_coefficients, None, None, (img.shape[1], img.shape[0]),
                                         cv2.CV_32FC1)

# undistorted image
undistorted_img = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

# Save the undistorted image
cv2.imwrite("undistorted_image.jpg", undistorted_img)
