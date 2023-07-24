import cv2


cap = cv2.VideoCapture(2)

while(True):
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture, motherfucker")

        break

    cv2.imshow("Cam test", frame)

    if cv2.waitKey(1):
        break

cap.release()
cv2.destroyAllWindows()

