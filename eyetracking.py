#All imports here
import cv2
import pyautogui
import mediapipe as mp

cam = cv2.VideoCapture(0)
face_mask = mp.solutions.face_mesh.FaceMesh()

#main code in here
def main():
    while True:
        _, frame = cam.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mask.process(rgb_frame)
        landmarks_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmarks_points:
            landmarks = landmarks_points[0].landmark
            for landmark in landmarks:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x,y), 3, (0,200,0))
        cv2.imshow('window name', frame)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()