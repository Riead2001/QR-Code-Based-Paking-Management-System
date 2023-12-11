import cv2
from flask import Response




def generate_frames1():
    # Capture video
    cap = cv2.VideoCapture(r'C:\Users\User\Desktop\QR_CodeBasedParkingBookingSystem\env\static\video\video1.mp4')

    while True:
        # Read frames
        ret, frame = cap.read()

        if not ret:
            break

        # Encode the frame into JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Use yield to send the frame content
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # Release video capture and finish
    cap.release()
def generate_frames2():
    # Capture video
    cap = cv2.VideoCapture(r'C:\Users\User\Desktop\QR_CodeBasedParkingBookingSystem\env\static\video\video2.mp4')

    while True:
        # Read frames
        ret, frame = cap.read()

        if not ret:
            break

        # Encode the frame into JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Use yield to send the frame content
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # Release video capture and finish
    cap.release()    

def generate_frames3():
    # Capture video
    cap = cv2.VideoCapture(r'C:\Users\User\Desktop\QR_CodeBasedParkingBookingSystem\env\static\video\video3.mp4')

    while True:
        # Read frames
        ret, frame = cap.read()

        if not ret:
            break

        # Encode the frame into JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Use yield to send the frame content
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # Release video capture and finish
    cap.release()        

def generate_frames4():
    # Capture video
    cap = cv2.VideoCapture(r'C:\Users\User\Desktop\QR_CodeBasedParkingBookingSystem\env\static\video\video4.mp4')

    while True:
        # Read frames
        ret, frame = cap.read()

        if not ret:
            break

        # Encode the frame into JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Use yield to send the frame content
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    # Release video capture and finish
    cap.release()        



def video_feed1():
    return Response(generate_frames1(), mimetype='multipart/x-mixed-replace; boundary=frame')

def video_feed2():
    return Response(generate_frames2(), mimetype='multipart/x-mixed-replace; boundary=frame')

def video_feed3():
    return Response(generate_frames3(), mimetype='multipart/x-mixed-replace; boundary=frame')

def video_feed4():
    return Response(generate_frames4(), mimetype='multipart/x-mixed-replace; boundary=frame')