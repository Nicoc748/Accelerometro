#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray

#def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)  

def listeneracc():

    rospy.init_node('listeneracc', anonymous=True)

    rospy.Subscriber('accelerazioni', Float32MultiArray)

    rospy.spin()

if __name__ == '__main__':
    listeneracc()