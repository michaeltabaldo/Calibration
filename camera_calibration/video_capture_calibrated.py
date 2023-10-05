import cv2
import yaml
import numpy as np

# Load camera calibration data from a YAML file
with open('calibration_matrix.yaml') as f:
    data = yaml.safe_load(f)

camera_matrix = np.array(data['camera_matrix'])
distance_coefficients = np.array(data['distance_coefficients'])

# Initialize the camera capture
cap = cv2.VideoCapture(2)  # Use 0 for the default camera, or change to the appropriate camera index

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    if not ret:
        break

    # Undistort the captured frame
    undistorted_frame = cv2.undistort(frame, camera_matrix, distance_coefficients)

    # Display the undistorted frame
    cv2.imshow("Undistorted Frame", undistorted_frame)

    # Check for the 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
