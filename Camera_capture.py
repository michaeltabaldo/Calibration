import cv2
import os

# IP camera URL (replace with your camera's URL)
camera_url = 'http://your_camera_ip_address/video'

# Create a directory to store captured photos if it doesn't exist
if not os.path.exists('photos'):
    os.mkdir('photos')

# Initialize the IP camera capture
cap = cv2.VideoCapture(camera_url)

photo_count = 0  # Counter for captured photos

while True:
    # Capture a frame from the IP camera
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("IP Camera Feed", frame)

    key = cv2.waitKey(1)

    # Check if the spacebar is pressed (key code 32)
    if key == 32:
        # Save the captured photo to the 'photos' directory
        photo_count += 1
        photo_filename = f'photos/photo_{photo_count}.jpg'
        cv2.imwrite(photo_filename, frame)
        print(f"Photo saved as {photo_filename}")

    # Check for the 'q' key press to exit the loop
    if key & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
