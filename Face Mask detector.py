import cv2
import numpy as np
from keras.models import load_model

# Load the trained model
model = load_model('mask_detector_model.h5')

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Define the classes
classes = ['Mask', 'No Mask']

# Initialize a dictionary for storing the colors
colors = {0: (0, 255, 0), 1: (0, 0, 255)}

# Define the cascade classifier for detecting faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect the faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60), flags=cv2.CASCADE_SCALE_IMAGE)
    
    # Loop through each face and make a prediction
    for (x, y, w, h) in faces:
        # Extract the face region of interest
        face_roi = gray[y:y+h, x:x+w]
        face_roi = cv2.resize(face_roi, (100, 100))
        face_roi = face_roi / 255.0
        face_roi = face_roi.reshape(1, 100, 100, 1)
        
        # Make a prediction using the trained model
        result = model.predict(face_roi)
        label = np.argmax(result, axis=1)[0]
        
        # Draw a rectangle around the face and label it
        cv2.rectangle(frame, (x, y), (x+w, y+h), colors[label], 2)
        cv2.putText(frame, classes[label], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, colors[label], 2)
    
    # Display the resulting frame
    cv2.imshow('Face Mask Detection', frame)
    
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture object and destroy the windows
cap.release()
cv2.destroyAllWindows()
