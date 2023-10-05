import cv2
import numpy as np
import yaml

with open('calibration_matrix.yaml') as f:
    data = yaml.safe_load(f)

camera_matrix = np.array(data['camera_matrix'])
distance_coefficients = np.array(data['distance_coefficients'])

img = cv2.imread("distorted.jpg")

h, w = img.shape[:2]
new_camera_mtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, distance_coefficients, (w, h), 1, (w, h))

# undistorted
mapx, mapy = cv2.initUndistortRectifyMap(camera_matrix, distance_coefficients, None, new_camera_mtx, (w, h), 5)
dst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)

# crop the image
x, y, w, h = roi
dst = dst[y:y + h, x:x + w]

cv2.imshow('cal.png', dst)
cv2.imwrite('calibrated_result.png', dst)
print("calibrated_result saved!")
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

print(type(camera_matrix))
print(type(distance_coefficients))
