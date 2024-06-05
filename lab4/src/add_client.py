#!/usr/bin/env python3
import rospy
from lab4.srv import addtwo, addtwoRequest

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', addtwo)
        request = addtwoRequest(a=x, b=y)
        response = add_two_ints(request)
        return response.sum
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

if __name__ == "__main__":
    rospy.init_node('add_two_ints_client')
    x = 20
    y = 30
    rospy.loginfo("Requesting %d + %d" % (x, y))
    result = add_two_ints_client(x, y)
    rospy.loginfo("Result: %d" % result)
