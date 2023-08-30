import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

finger_tips =[8, 12, 16, 20]
thumb_tip= 4

while True:
    ret,img = cap.read()
    img = cv2.flip(img, 1)
    h,w,c = img.shape
    results = hands.process(img)


    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            #accessing the landmarks by their position
            lm_list=[]
            for id ,lm in enumerate(hand_landmark.landmark):
                lm_list.append(lm)

             #Code goes here   
    for lm_index in fingertip:
         finger_tip_y = landmarks[lm_index].y 
         finger_bottom_y = landmarks[lm_index - 2].y 
         
         # Get Thumb Tip and Bottom y Position Value 
         thumb_tip_x = landmarks[lm_index].x
         thumb_bottom_x = landmarks[lm_index - 2].x

        # Check if ANY FINGER is OPEN or CLOSED
         if lm_index !=4:
             if finger_tip_y < finger_bottom_y:
                fingers.append(1) 
                print("FINGER with id ",lm_index," is Open") 
             if finger_tip_y > finger_bottom_y:
                 fingers.append(0)
                 print("FINGER with id ",lm_index," is Closed")
    else: 
            if thumb_tip_x > thumb_bottom_x:
                fingers.append(1)
                print("THUMB is Open")
            if thumb_tip_x < thumb_bottom_x:
                finger.append(0)
                print("THUMB is closed")




            mp_draw.draw_landmarks(img, hand_landmark)
            mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec((0,0,255),2,2),
            mp_draw.DrawingSpec((0,255,0),4,2)
    

    cv2.imshow("hand tracking", img)
    cv2.waitKey(1)