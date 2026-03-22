import cv2

# Load pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

#'haarcascade_frontalface_default.xml' we import this file and put it in face_cascade

# Start video capture (0 = webcam)
cap = cv2.VideoCapture(0)

while True:
    status, frame = cap.read()
    if not status:
        break

    # Convert to grayscale (required for detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #necessary to convert to gray since this model 'haarcascade_frontalface_default.xml' can work in single channel

    # Detect faces (heads)
    faces = face_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.3, #min size of face datected
        minNeighbors=5 #how close 2 faces can be
    )
    #makes faces an array and later we find it's length, it's element

    # Draw rectangle around each detected head
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)

    # Count total persons
    count = len(faces)

    frame = cv2.flip(frame, 1)
    # Display count at top-left
    cv2.putText(frame,
                f'Persons: {count}',
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (10, 10, 10),
                2)

    # Show output
    cv2.imshow("Head Count", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()