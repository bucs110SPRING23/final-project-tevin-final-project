import cv2
import pygame
from ultralytics import YOLO as v8 

pygame.init()

class Detections: 
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 35, 35))
        self.throw = False
        self.impact = False
        self.deflect = True 