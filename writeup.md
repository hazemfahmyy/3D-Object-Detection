# Writeup: Track 3D-Objects Over Time

## Compute Lidar Point-Cloud from Range Image

### Visualize range image channels
Range image - Frame 0:
![img1](results/range_image_frame0.png)
Range image - Frame 0 - Cropped to center:
![img2](results/range_image_cropped_frame0.png)
Range image - Frame 1:
![img3](results/range_image_frame1.png)
Range image - Frame 1 - Cropped to center:
![img4](results/range_image_cropped_frame1.png)

### Visualize point-cloud 

In the image below, the first return show a vehicle that is not fully detected, which could affect the object detection module in later stages
![img5](results/return_1.png)

Images below show how the side glasses of nearby vehicles are undetected by the LIDAR, which could be a factor in determining the vehicle shapes:
![img6](results/glasses.png)
![img7](results/glasses2.png)

Images below show how the nearby vehicles are partially detected due to the blind spot of the LIDAR detection:
![img7](results/side_car.png)
![img8](results/side_car2.png)
![img9](results/side_car3.png)
![img10](results/side_car4.png)
![img11](results/side_car5.png)

## Create Birds-Eye View from Lidar PCL
### Convert sensor coordinates to bev-map coordinates
### Compute intensity layer of bev-map
### Compute height layer of bev-map

## Model-based Object Detection in BEV Image
### Add a second model from a GitHub repo
### Extract 3D bounding boxes from model response 

## Performance Evaluation for Object Detection

### Compute intersection-over-union (IOU) between labels and detections 
### Compute false-negatives and false-positives 
### Compute precision and recall

Please use this starter template to answer the following questions:

### 1. Write a short recap of the four tracking steps and what you implemented there (filter, track management, association, camera fusion). Which results did you achieve? Which part of the project was most difficult for you to complete, and why?


### 2. Do you see any benefits in camera-lidar fusion compared to lidar-only tracking (in theory and in your concrete results)? 


### 3. Which challenges will a sensor fusion system face in real-life scenarios? Did you see any of these challenges in the project?


### 4. Can you think of ways to improve your tracking results in the future?

