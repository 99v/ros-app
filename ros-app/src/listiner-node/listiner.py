#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    if (data.data.find('error') != -1):
        rospy.logerr("%s", data.data)
        print("Error: " + data.data, file=open('logfile.txt', 'a'))
    else:
        #rospy.loginfo("%s", data.data)
        rospy.loginfo("%s", data.data)
        print("Info: " + data.data, file=open('logfile.txt', 'a'))
        #rospy.loginfo(rospy.get_caller_id() + ": %s", data.data)

def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/recieved_data", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
