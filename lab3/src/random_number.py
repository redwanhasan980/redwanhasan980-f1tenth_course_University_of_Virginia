#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
from random import randint
def generate_rand():
    rnd= randint(0,5000)
    return rnd
def random_number():
    rospy.init_node('random_number')
    pub=rospy.Publisher('rand_no',Int32,queue_size=10)
    rate=rospy.Rate(5)
    while not rospy.is_shutdown():
        rnd=generate_rand()
        rospy.loginfo(rnd)
        pub.publish(rnd)
        rate.sleep()

if __name__=='__main__':
    try:
        random_number()
    except rospy.ROSInterruptException:
        pass

