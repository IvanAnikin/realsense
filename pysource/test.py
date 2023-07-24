import cv2
from realsense_camera import *
from mask_rcnn import *

# Load Realsense camera and Mask R-CNN
rs = RealsenseCamera()
mrcnn = MaskRCNN()

while True:
    # Get frame in real time from Realsense camera
    ret, bgr_frame, depth_frame = rs.get_frame_stream()

    cv2.imshow("Bgr frame", bgr_frame)
    #cv2.imshow("Depth frame", depth_frame)

    #point_x, point_y = 250, 100
    #distance_mm = depth_frame[point_x, point_y]
    #cv2.circle(bgr_frame, (point_x, point_y), 8, (0,0,255), -1)

    # Get object mask
    # boxes, classes, contours, centers = mrcnn.detect_objects_mask(bgr_frame)

    # Draw object mask
    #bgr_frame = mrcnn.draw_object_mask(bgr_frame)

