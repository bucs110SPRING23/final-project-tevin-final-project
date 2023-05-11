[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10900971&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  Spring 2023

## Team Members

Tevin Flom 

***

## Project Description

This is an object-detection based Street-Fighter style game that uses household items to attack in the game. This is a two player arcade-style game with player controls on either side of a standard keyboard. The game will include a dataset of real-life objects the game can detect and deploy, but users should find items in their surroundings to use in the game. The objects correlate to different amounts of damage taken by the opponent. The first player to lose all of their health points loses the game. 

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.png)

## Program Design


Citations:
YOLOv8 : https://docs.ultralytics.com/quickstart/#use-with-python
Background: https://previews.123rf.com/images/nearbirds/nearbirds1503/nearbirds150300032/38706034-tileable-horizontal-background-wild-west-set1.jpg
Character Images Developed: 
Ken: https://www.deviantart.com/l-dawg211/art/Ken-Street-Fighter-III-Battle-Sprite-885473938
Ryu: https://www.clipartmax.com/middle/m2H7K9b1H7d3d3b1_image-result-for-ryu-sprite-png-ryu-street-fighter-2/

### Features

1. Intro screen
2. Image File Upload for object detection
3. KO alert 
4. Powerups from object detections 
5. Health status bars 

### Classes

- Controller - contains the game loop and some global variables & imports for now 
- Player - the game physics for players as well as attacks are here 
- Detections - contains the YOLO object detection model and its predictions as well as the objects they translate to in the game. This will likely have to become several different classes to align with the structure of the YOLO model (ie. foods, utensils, kitchen appliances, etc. )

### Non-Working
- attacks don't currently work 


## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
