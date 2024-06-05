#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
flg =0
def callback(msg):
    global flg
    flg=msg.data

def sub():
    sub=rospy.Subscriber('rand_no',Int32,callback)
def pub():
    pub=rospy.Publisher('isTrue',String,queue_size=10)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo(flg)
        if flg<=2000:
            rospy.loginfo("true")
            pub.publish("True")
        else:
            rospy.loginfo("false")
            pub.publish("false")
        rate.sleep()


if __name__=='__main__':
    
    rospy.init_node('pub_n_sub',anonymous=True)
    
    sub()
    pub()
    

