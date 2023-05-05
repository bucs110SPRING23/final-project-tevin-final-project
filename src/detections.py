import cv2 
import numpy
from ultralytics import YOLO 
class Detections:
    def __init__(self, img, img_path): 
        self.img = img 
        self.path = str(img_path)
        self.weights = 'yolov8n.pt'
    def object_detection(): 
        img_path = print(input("Type in File Path for the Image Containing Household Objects:  "))
        img_path = str(img_path)
        img = cv2.imread(img_path)
        img.resize(200, 200)
        model = YOLO('yolov8n.pt')
        while True: 
            result = model(img) 
            cv2.imshow("yolov8n.pt", img) 
            result = str(result) 
            if result.find('chairs') == True: 
                print(result)
            elif result.find('fork') == True: 
                print(result)
            elif result.find('potted plant') == True: 
                print(result)
            elif result.find('table') == True: 
                print(result)
            elif result.find('person') == True: 
                print(result)
            else: 
                break
    