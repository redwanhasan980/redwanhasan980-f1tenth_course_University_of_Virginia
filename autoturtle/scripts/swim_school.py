#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
cmd=Twist()
first = 0
turn = 0
def callback(msg):
    global first
    global turn
    if first != 0:
        rospy.loginfo('x %f, y %f',msg.x,msg.y)
    if msg.x>5.5 and msg.y>5.5 and turn == 1 and msg.x<5.56 and msg.y<5.56:
        cmd.angular.z=cmd.angular.z*(-1)
        turn = 0
    if (msg.x>6 and msg.y>6 ) or (msg.x<5 and msg.y<5):
        turn =1

def sub():
    sub=rospy.Subscriber('/turtle1/pose',Pose,callback)
def make8():
    
    pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rospy.init_node('make8',anonymous=False)
    rate = rospy.Rate(10)
    global first
    first=0
    while not rospy.is_shutdown():
        if first == 0:
            cmd.linear.x=float(input("Please Input Linear velocity in the range[2,6] :"))
            cmd.angular.z=float(input("Please Input Angular velocity in the range[1,3] :"))
            first+=1
        pub.publish(cmd)
        rate.sleep()
if __name__=='__main__':
    
    try:
        sub()
        make8()
    except rospy.ROSInterruptException:
        pass
