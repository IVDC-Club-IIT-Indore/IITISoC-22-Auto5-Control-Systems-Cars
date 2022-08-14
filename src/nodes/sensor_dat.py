#! /usr/bin/env python3

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

def callback(data):
    print(type(data.ranges))
    

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('Scan', LaserScan, callback)
    
    #spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
