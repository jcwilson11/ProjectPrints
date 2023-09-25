import cv2

def generate_frames():
    cap = cv2.VideoCapture('/dev/video0')
    if not cap.isOpened():
        print("Error: Couldn't open the camera.")
        return
    while True:
        success, frame = cap.read()
        if not success:
            print("Error: Couldn't read frame from camera.")
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

