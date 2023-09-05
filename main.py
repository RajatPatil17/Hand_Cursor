import cv2
import mediapipe as mdp
import pyautogui
cap = cv2.VideoCapture(0)
hand_det = mdp.solutions.hands.Hands()
drawing_utils = mdp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
indexy = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    op = hand_det.process(rgb_frame)
    hands = op.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height) 
                if id == 8:
                    cv2.circle(img = frame, center = (x,y), radius = 10, color=(0,255,255))
                    indexx = screen_width/frame_width*x
                    indexy = screen_height/frame_height*y
                    pyautogui.moveTo(indexx,indexy)
                if id == 4:
                    cv2.circle(img = frame, center = (x,y), radius = 10, color=(0,255,255))
                    thumbx = screen_width/frame_width*x
                    thumby = screen_height/frame_height*y
                    print("far by",abs(indexy-thumby))
                    if abs(indexy - thumby)<50:
                        pyautogui.click()
                        pyautogui.sleep(1)
    #cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
    
    
    