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

In the image below, the first return/response image shows a vehicle that is not fully detected, which could affect the object detection module in later stages when the full shape of a vehicle is not recognized:

![img5](results/return_1.png)

In the examples below show how the side glasses and windshields of nearby vehicles are undetected by the LIDAR, which could be a factor in determining the vehicle shapes:

![img6](results/glasses.png)

![img7](results/glasses2.png)

The examples below show how the nearby vehicles are partially detected due to the blind spot of the LIDAR detection:

![img7](results/side_car.png)

![img8](results/side_car2.png)

![img9](results/side_car3.png)

![img10](results/side_car4.png)

![img11](results/side_car5.png)

## Create Birds-Eye View from Lidar PCL
### Convert sensor coordinates to bev-map coordinates
![img16](results/bev_pcl.png)
### Compute intensity layer of bev-map
![img17](results/bev_intensity.png)
### Compute height layer of bev-map
![img18](results/bev_height.png)

## Model-based Object Detection in BEV Image
### Add a second model from a GitHub repo
### Extract 3D bounding boxes from model response 
![img19](results/labels_detected.png)

## Performance Evaluation for Object Detection

The figures below show the performance of darknet (first image) compared to the performance evaluation of fpn_resnet (second image), where it shows that resnet has a higher chance of correctly detecting an object

![img20](results/darknet.png)

![img21](results/resnet.png)

### Compute intersection-over-union (IOU) between labels and detections 
### Compute false-negatives and false-positives 
### Compute precision and recall
