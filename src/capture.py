# import cv2
#
# face_cascade=cv2.CascadeClassifier("/home/ankur/PycharmProjects/SPOT-me/encoding/haarcascade_frontalface_default.xml")
#
# cap=cv2.VideoCapture(0)
#
# while True:
#     ret, frame= cap.read()
#
#     gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     face=face_cascade.detectMultiScale(gray,1.05, 5)
#
#     for(x,y,w,h) in face:
#         cv2.rectangle(frame,(x,y),(x+w, y+h), (0,255,0),2, )
#         name="Face Detected"
#         cv2.putText(
#         frame, name,(x, max(y - 20, 20)),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,256,0),2)
#
#     cv2.imshow("Frame Detected", frame )
#
#
#     if cv2.waitKey(1) & 0xFF==ord("q"):
#         break
#
# cap.release()
# cv2.destroyAllWindows()