

import cv2 
import numpy as np 

# Open the video file
video_path = '/Users/mac/Downloads/video.mov'  # Replace this with the path to your video file
cap = cv2.VideoCapture(video_path)

while True:
    
    ret, frame = cap.read()

    if not ret:
        break  # Break the loop if the video has ended
    
    # Locate points of the documents
    # or object which you want to transform
    pts1 = np.float32([[0, 260], [640, 260],
                    [0, 400], [640, 400]])
    pts2 = np.float32([[0, 0], [400, 0],
                    [0, 640], [400, 640]])
    
    # Apply Perspective Transform Algorithm
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (500, 600))
    
    # Display the original and transformed frames
    cv2.imshow('frame', frame) # Original frame
    cv2.imshow('frame1', result) # Transformed frame

    if cv2.waitKey(24) == 27:
        break

cap.release()
cv2.destroyAllWindows()
