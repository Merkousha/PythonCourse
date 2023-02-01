import cv2
import numpy as np

# Load the background subtractor
backSub = cv2.createBackgroundSubtractorMOG2()

# Open the camera
cap = cv2.VideoCapture(0)

# Continue processing the video frame by frame
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Apply the background subtractor to the frame
    fgMask = backSub.apply(frame)

    # Threshold the mask to remove the noise
    thresh = cv2.threshold(fgMask, 200, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours in the mask
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the frame
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the processed frame
    cv2.imshow("Hand Movement Detection", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release the camera and destroy the windows
cap.release()
cv2.destroyAllWindows()


#In this code, we use a background subtractor (cv2.createBackgroundSubtractorMOG2) to detect the moving hand in the video feed. The background subtractor subtracts the background from the current frame to obtain a mask that shows only the moving objects. We then threshold the mask, erode and dilate it to remove the noise and find the contours in the mask. Finally, we draw rectangles around the contours to show the detected hand movements.
