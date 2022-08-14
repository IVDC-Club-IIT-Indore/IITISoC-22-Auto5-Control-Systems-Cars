#!/usr/bin/env python3

from logging import StringTemplateStyle
import rospy
import time
from prius_msgs.msg import Control
from std_msgs.msg import String


import sys, select, os
if os.name == 'nt':
  import msvcrt, time
else:
  import tty, termios

def getKey():
    if os.name == 'nt':
        timeout = 0.1
        startTime = time.time()
        while(1):
            if msvcrt.kbhit():
                if sys.version_info[0] >= 3:
                    return msvcrt.getch().decode()
                else:
                    return msvcrt.getch()
            elif time.time() - startTime > timeout:
                return ''

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key




# def initialize(str):
# 		global str_msg
# 		str_msg = "" + str

# def callback(msg):
# 	initialize(msg)

# sub = rospy.Subscriber('prius', String , callback )

if __name__=="__main__":
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('navigate_ugv')
    pub = rospy.Publisher('prius', Control, queue_size=20)
    
    try:
        command = Control()
        rospy.loginfo('start')
        print("w : Forward\n a : Left \n s : Reverse \n d : Right")
        while not rospy.is_shutdown():
            
            current_key = getKey()

            if(current_key == 'w'):
                command.shift_gears = Control.FORWARD
                command.throttle = 0.5
                command.brake =0.0
                command.steer= 0.0 
            if(current_key == 's'):
                command.shift_gears = Control.REVERSE
                command.throttle = 1.0
                command.brake =0.0
                command.steer= 0.0
            if(current_key == 'a'):
                #command.shift_gears = Control.FORWARD
                command.throttle = 0.5
                command.brake =0.0
                command.steer= 0.8
            if(current_key == 'd'):
                #command.shift_gears = Control.FORWARD
                command.throttle = 0.5
                command.brake =0.0
                command.steer= -0.8
            if(current_key == 'f'):
                command.shift_gears = Control.NO_COMMAND
                command.throttle = 0.0
                command.brake =1.0
                command.steer= 0.0
            
            pub.publish(command)
    except rospy.ROSInterruptException:
        pass
    if os.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)



