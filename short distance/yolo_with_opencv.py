import cv2
import numpy as np
import imutils 

# cap = cv2.VideoCapture('Cars.mp4')
cap = cv2.VideoCapture(0)
def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)
make_720p()
net = cv2.dnn.readNetFromONNX("yolov5n.onnx")
file = open("coco.txt","r")
classes = file.read().split('\n')
# distance from camera to object(face) measured
# centimeter
Known_distance = 76.2
# width of face in the real world or Object Plane
# centimeter
Known_width = 19
# focal length finder function
def Focal_Length_Finder(measured_distance, real_width, width_in_rf_image):
	focal_length = (width_in_rf_image* measured_distance)/ real_width
	return focal_length
# distance estimation function
def Distance_finder(Focal_Length, real_face_width, face_width_in_frame):
	distance = (real_face_width * Focal_Length)/face_width_in_frame
	return distance
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

def face_data(image):
        face_width = 0  # making face width to zero
        # converting color image to gray scale image
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # detecting face in the image
        faces = face_detector.detectMultiScale(gray_image, 1.3, 5)
        # looping through the faces detect in the image
        # getting coordinates x, y , width and height
        for (x, y, h, w) in faces:
            # draw the rectangle on the face
            cv2.rectangle(image, (x, y), (x+w, y+h), GREEN, 2)
            # getting face width in the pixels
            face_width = w
        # return the face width in pixel
        return face_width
 # reading reference_image from directory
ref_image = cv2.imread("images/savedImage.jpg")
 
# find the face width(pixels) in the reference_image
ref_image_face_width = face_data(ref_image)
Focal_length_found = Focal_Length_Finder(Known_distance, Known_width, ref_image_face_width)
print(Focal_length_found)

while True:
    img = cap.read()[1]
    if img is None:
        break
    # img = cv2.resize(img, (1000,600))
    blob = cv2.dnn.blobFromImage(img,scalefactor= 1/255,size=(640,640),mean=[0,0,0],swapRB= True, crop= False)
    net.setInput(blob)
    detections = net.forward()[0]
    # cx,cy , w,h, confidence, 80 class_scores
    # class_ids, confidences, boxes

    classes_ids = []
    confidences = []
    boxes = []
    rows = detections.shape[0]

    img_width, img_height = img.shape[1], img.shape[0]
    x_scale = img_width/640
    y_scale = img_height/640

    for i in range(rows):
        row = detections[i]
        confidence = row[4]
        if confidence > 0.5:
            classes_score = row[5:]
            ind = np.argmax(classes_score)
            if classes_score[ind] > 0.5:
                classes_ids.append(ind)
                confidences.append(confidence)
                cx, cy, w, h = row[:4]
                x1 = int((cx- w/2)*x_scale)
                y1 = int((cy-h/2)*y_scale)
                width = int(w * x_scale)
                height = int(h * y_scale)
                box = np.array([x1,y1,width,height])
                boxes.append(box)

    indices = cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.5)

    for i in indices:
        x1,y1,w,h = boxes[i]
        label = classes[classes_ids[i]]
        conf = confidences[i]
        text = label + "{:.2f}".format(conf)
        
        width_in_frame = w
        if width_in_frame != 0:
            Distance = Distance_finder(Focal_length_found, Known_width, width_in_frame)
            # print("width_in_frame = ",width_in_frame," text = " ,text)
       # draw line as background of text
        # cv2.line(img, (30, 30), (230, 30), RED, 32)
        # cv2.line(img, (30, 30), (230, 30), BLACK, 28)

        cv2.rectangle(img,(x1,y1),(x1+w,y1+h),(255,0,0),2)
        cv2.putText(img, text+f", Distance: {round(Distance,2)} CM", (x1,y1-2),cv2.FONT_HERSHEY_COMPLEX, 0.7,(255,0,255),2)
        # Drawing Text on the screen
        # cv2.putText(img, f"Distance: {round(Distance,2)} CM", (30, 35),cv2.FONT_HERSHEY_COMPLEX, 0.6, GREEN, 2)
      
    cv2.imshow("VIDEO",img)
    k = cv2.waitKey(10)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()