# from mmap import MADV_PROTECT
from turtle import right
import cv2
import mediapipe as mdp
import pyautogui as pygui  # for moving mouse

# step 1 ---> capturing video
# step 2 ---> Detecting face using mediapipe
# step 3 ---> making circle of landmarks on face with x,y coordinates
# step 4 ---> configuring


cam_1 = cv2.VideoCapture(0)
face_mesh = mdp.solutions.face_mesh.FaceMesh(refine_landmarks = True) #variable to detect face
screen_width,screen_height = pygui.size()
while 1:
    _,frame = cam_1.read()
    frame = cv2.flip(frame,1)
    rgb_color_frame =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)  #to change color of video to gray scale for efficiency 
    output_frame = face_mesh.process(rgb_color_frame)
    face_landmarks = output_frame.multi_face_landmarks  #for detecting landmarks on face.
    frame_height,frame_width ,_ = frame.shape
    # print(face_landmarks)

    # Landmarks detected till here...

    # making loop for landmarks
    if face_landmarks:
        landmarks = face_landmarks[0].landmark
        for id,landmark in enumerate(landmarks[474:478]):
            x_axis = int(landmark.x*frame_width)
            y_axis = int(landmark.y*frame_height)
            # making landmark circle on face -->cirle(frame,(points),radius,(0,255,0))
            cv2.circle(frame,(x_axis,y_axis),3,(0,255,0))
            print(x_axis,y_axis)

            if id == 1:
                screen_x = screen_width/frame_width * x_axis + 2
                screen_y = screen_height/frame_height * y_axis + 2
                pygui.moveTo(screen_x,screen_y)   # move cursor
        left_eye = [landmarks[145],landmarks[159],landmarks[80],landmarks[90]]
        for landmark in left_eye:

             x_axis = int(landmark.x*frame_width)
             y_axis = int(landmark.y*frame_height)

             cv2.circle(frame,(x_axis,y_axis),3,(0,255,255))
             print('diff: ',left_eye[2].y - left_eye[3].y)

        if(left_eye[2].y - left_eye[3].y) <= -0.020:
            pygui.click(clicks=2)
            pygui.sleep(1)    

        elif(left_eye[0].y-left_eye[1].y) <0.004:
            pygui.click()
            pygui.sleep(1)    
    cv2.imshow('mouse_cam',frame)
    cv2.waitKey(1)



