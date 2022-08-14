#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import Image

import cv2

def callback(mesg):
    image = int.from_bytes(mesg.data, 'little')
    print(image)
    #cv2.imshow('result', image)
    #cv2.waitKey(0)

def main():
    
    rospy.init_node('cam_dat', anonymous=True)
    sub = rospy.Subscriber('/prius/front_camera/image_raw', Image, callback)
    #cv2.waitKey(0)
    #print(image)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except  rospy.ROSInterruptException:
        cv2.destroyAllWindows        
        pass