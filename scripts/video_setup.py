import cv2


def set_video_size():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # set Width
    cap.set(4, 480)  # set Height
    return cap