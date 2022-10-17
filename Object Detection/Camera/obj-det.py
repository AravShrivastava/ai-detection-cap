import cv2
import numpy as np
import pyttsx3
import argparse
import requests
from clint.textui import progress

ap = argparse.ArgumentParser()
ap.add_argument('-c', '--config', required=True,help = 'path to yolo config file')
ap.add_argument('-w', '--weights', default=None,help = 'path to weights')
ap.add_argument('-cl', '--classes', required=True,help = 'path to text file containing class names')
args = ap.parse_args()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def draw_prediction(img, class_id, x, y, x_plus_w, y_plus_h):
    label = str(classes[class_id])
    # color = COLORS[class_id]
    # cv2.rectangle(img, (x, y), (x_plus_w, y_plus_h), color, 2)

    if "person" in label:
        width = (x_plus_w - x) - x
        height_to_width = ((y_plus_h - y) - y)/((x_plus_w - x) - x)
        xmin = img.shape[1] / 4
        xmax = img.shape[1] * 3 / 4 
        if x < xmin or w > xmax:
            return img
        pedestrian_width = .65 # width [m]
        if (width != None) and (height_to_width > 1.8):
            distance = np.around((pedestrian_width * 600) / (width*2), decimals=0)*2
            bb_text = "{:.0f}metres".format(distance)
            # label = label + bb_text
            speak("Pedestrian: "+bb_text)
            # cv2.putText(img, label, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

    elif "car" in label:
        width = (x_plus_w - x) - x
        height_to_width = ((y_plus_h - y) - y)/((x_plus_w - x) - x)
        xmin = img.shape[1] / 4
        xmax = img.shape[1] * 3 / 4 
        if x < xmin or w > xmax:
            return img
        vehicle_width = 2.0 # width [m]
        if (width != None) and (height_to_width > .5):
            distance = np.around((vehicle_width * 600) / (width*2), decimals=0)*2
            bb_text = "{:.0f}metres".format(distance)
            label = label + bb_text
            speak("A Vehicle: "+bb_text)
            # cv2.putText(img, label, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

    elif "stop sign" in label:
        width = (x_plus_w - x) - x
        height_to_width = ((y_plus_h - y) - y)/((x_plus_w - x) - x)
        xmin = img.shape[1] / 8
        xmax = img.shape[1] * 7 / 8
        if x < xmin or w > xmax:
            return img
        stopsign_width = .8 # width [m]
        if (width != None) and (height_to_width > .7):
            distance = np.around((stopsign_width * 600) / (width*2), decimals=0)*2
            bb_text = "{:.0f}metres".format(distance)
            # label = label + bb_text
            # y_offset = 80
            # x_offset = 70
            # x1 = int((img.shape[1]/2) + x_offset)
            # y1 = y_offset
            speak("Stop Sign: "+bb_text)
            # cv2.putText(img, label, (int(x1),int(y1)), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)

    speak("A "+label+" detected")
    # cv2.putText(img, label, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)    

def download_file(url):
    r = requests.get(url, stream=True)
    path = 'yolov3.weights'
    with open(path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.mill(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
            if chunk:
                f.write(chunk)
                f.flush()
    return path


image = cv2.VideoCapture(0)
Width = image.get(cv2.CAP_PROP_FRAME_WIDTH)
Height = image.get(cv2.CAP_PROP_FRAME_HEIGHT)
scale = 0.00392
classes = None
with open(args.classes, 'r') as f:
    classes = [line.strip() for line in f.readlines()]
COLORS = np.random.uniform(0, 255, size=(len(classes), 3))
weights = args.weights
if args.weights == None:
    weights = download_file('https://pjreddie.com/media/files/yolov3.weights')
net = cv2.dnn.readNet(weights, args.config)
while True:
    success, img = image.read()
    blob = cv2.dnn.blobFromImage(img, scale, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    outs = net.forward(output_layers)
    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.5
    nms_threshold = 0.4
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])
    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
    for i in indices:
        box = boxes[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        draw_prediction(img, class_ids[i], round(x), round(y), round(x + w), round(y + h))
    # cv2.imshow("object detection", img)
    cv2.waitKey(1)
cv2.destroyAllWindows()