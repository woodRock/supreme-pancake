# Day 5

# Solving occlusion for complete plant models with accurate 3D metrics
## Prof. Richard Green - Professor of Computer Science - University of Canterbury

## Abstract
We cannot automate what we cannot see – and COVID saw fruit and vegetables rotting on the ground because we were unable to automate harvesting in such challenging complex outdoor environments.

Our recent breakthroughs with NeRF and Gaussian splatting focus on solving such leaf occlusion to enable sub-mm 3D metrics of all fruit (and other plant organs) and complete & correct structure of branching – all this from images of windblown plants. This also enables rapid data reduction of petabytes of data from scanning a farm (such as orchards or vineyards) from hundreds of images per plant. We will also discuss the challenges that remain and so propose potential directions for future work.

## Biography
Since 2004 Professor Richard Green has been lecturing at UC after running his own successful 50 staff software company in Sydney (sold to a multinational). Richard has raised over $30m at UC for AI research and development and has over 200 refereed publications. He is currently leading a $6m autonomous robot-vine-scanning project and a $10m project for drones using precision tools. He also co-chairs the NZ AI Researchers Association and leads UC Vision.

- Autonomous scanner, metrics of branch structure (i.e., pruning), metrics of plant organs (harvesting yield prediction)
- Image acquisition -> image alignment and sparse 3D reconstruction -> Dense 3D reconstruction -> Segmentation of woody structures and plant organs -> Skeletonisation and 3D shape fitting -> Metrics of plan'ts structure and organs.
- Distributed processing throughout the pipeline.
    - Row localisation
    - Landmark extraction (detection/clustering)
    - Camera calibration (per scan)
    - Image aligment (SfM per bay)
    - Dense 3D reconstruction
        - Gaussian ssplatting per-side 
        - Alignment between sides 
    - Alignment across time
    - Organ extraction + 
- NZ has 90 million vines, mostly sav blanc.
- Hand pruned with 2 minutes per vine. 
- 12 12-mpixel cameras for 100s of images/plant.
- 4070 GPU on the robot.
- Sensors (camera + GNSS + LiDAR + wheel odometry)
    - Synchronization - and with flashes 
    - Pipelining capture (Cameras)
    - Camera calibration 
- Different systems to go wrong:
    - Hardware 
    - Map creation 
    - Localisation
    - Naviation + row following 
    - Image capture + raw processing 
    - Storage in database + API 
    - Processing pipeline (distributed computing)
- Individually not difficult, but when all integrated together, becomes difficult 
- High optical flow so rolling shutter has a lot of distortion.
- Ethernet cpature with dedicated PCIE cards (multiple port) solves cable issues, GNSS interference, etc. 
- All the machine libraries assume 8-bit images. 
- Convert 8-bit to 12-bit for higher dynamic range. 
- Lighting/HDR, tone mapping as a group of images, still have issues with sun.
- Debayer 
- Image enhancement - bilateral filter, wiener filter -> "enhance". 
- Image storage and indexing - petabytes of data. 
- Geo-located using vehicle odometry (GPS/IMU/LiDAR)
- Landmarks for referencing plants from 2D detections.
- Eventually no need for raw images stored. 

https://maara.csse.canterbury.ac.nz/login

- AI better than stereo cameras for stereo matching. 
- Differentiable rendering
    - NeRF - volume ray-tracing 
    - Gaussian splatting - rasterization 
- Error correction - global drift 
- Over the span of several meters global drift can mean that ends are out by centermeters.
- Gaussian splatting silhoutte alignment 
    - matching across rows is difficult (no image overlap)
- We got a point cloud, we can geninuely see behind the leaves.
- Annotating a 3D point cloud.
- Mask DINO based instance segmentation.
- Tiled detection as we have a lot of small and large images. 
- Challenges: 
    - Harsh lighting conditions 
    - Small plant features 
    - SFM
- Future directions 
    - Address weakness of Gaussian platting 
    - Junk around the edge and from unseen directions. 
