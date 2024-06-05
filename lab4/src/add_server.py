#!/usr/bin/env python3

import rospy
from lab4.srv import addtwo, addtwoResponse

def handle_add_two_ints(req):
    result = req.a + req.b
    return addtwoResponse(sum=result)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', addtwo, handle_add_two_ints)
    rospy.loginfo("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
