import cv2 
import numpy
from ultralytics import YOLO 
class Detections:
    def __init__(self, img, img_path):
        """
        This function sets up the utilities for the YOLOv8 object detection model. 
        Args: self, image you wish to run through the model(OpenCV), image path(str)
        Returns: none
        """
        
        self.img = img 
        self.path = str(img_path)
        self.weights = 'yolov8n.pt'
    def object_detection(): 

        """
        This function takes the file path input from the user, runs it through the object detection model, and asses attack 2 damage based on how difficult the object was to find/obtain.
        If there are multiple objects in the frame and multiple detections are made, the attack 2 damage compounds. 
        The object detection portion works(see assets/diningroomtest.jpg), extracting the detection information from the numpy array produced by the model does not.
        Args: none 
        Returns: a2impact(int) this is the amount of health points the attack will take off
        """
        img_path = print(input("Type in File Path for the Image Containing Household Objects:  "))
        img_path = str(img_path)
        img = cv2.imread(img_path)
        img.resize(200, 200)
        model = YOLO('yolov8n.pt')
        a2impact = 0
        while True: 
            result = model(img) 
            cv2.imshow("yolov8n.pt", img) 
            result = str(result) 
            if result.find('chairs') == True: 
                a2impact += 8
                print(result)
                return a2impact
            elif result.find('fork') == True: 
                a2impact += 15
                print(result)
                return a2impact
            elif result.find('potted plant') == True: 
                a2impact += 11
                print(result)
                return a2impact
            elif result.find('table') == True: 
                print(result)
                a2impact += 5
                return a2impact
            elif result.find('person') == True: 
                print(result)
                a2impact += 6
                return a2impact
            elif result.find('lamp') == True: 
                print(result)
                a2impact += 10
                return a2impact
            else: 
                print("OBJECT(S) UNKNOWN TO GAME, PLEASE TRY AGAIN!")
                a2impact += 0 
                break

    