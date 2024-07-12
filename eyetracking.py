#All imports here
import cv2
import pyautogui
import mediapipe as mp

#get video feed from default camera
cam = cv2.VideoCapture(0)
#get face mesh using face_mesh solutions from mediapipe
face_mask = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)
#get screen width and height for upscaling
screen_w, screen_h = pyautogui.size()

#main code in here
def main():
    while True:
        #get frame from camera feed, flip the frame and get it height and width
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        frame_h, frame_w, _ = frame.shape

        #landmark detection is grayscale is easier so convert normal from to grayscale
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #face mesh is now processed using grayscale frames for the output
        output = face_mask.process(rgb_frame)
        #landmarks_points should my the multi face landmarks
        landmarks_points = output.multi_face_landmarks
        if landmarks_points:
            landmarks = landmarks_points[0].landmark
            #draw small circles for the landmarks we want to detect(eye)
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x,y), 3, (0,200,0))

                #out of the four landmark use any of them to move the mouse
                if id == 2:
                    screen_x = x * (screen_w/frame_w)
                    screen_y = y * (screen_h/frame_h)
                    pyautogui.moveTo(screen_x, screen_y)
             
            #define the left upper and lower eyelids landmarks 
            left = [landmarks[145], landmarks[159]]
            #difference in their y-cordinates being very small means we've closed the eye
            #and we can use this idea to make a click
            left_click = left[0].y - left[1].y < 0.009

            #draw tiny circles on the landmarks (upper and lower eyelids)
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x,y), 3, (0, 255, 0))
            
            #perform a clik when we blink the left eye
            if left_click:
                pyautogui.click()
                pyautogui.sleep(0.5)

        #show the frame window (eye pad)
        cv2.imshow('Eye pad', frame)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()