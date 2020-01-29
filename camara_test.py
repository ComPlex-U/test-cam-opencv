import cv2

pic = cv2.VideoCapture(0)

while(True):
    ret, camara_test = pic.read()
    cv2.imshow('Camara_test',camara_test)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
pic.release()
cv2.destroyAllWindows()