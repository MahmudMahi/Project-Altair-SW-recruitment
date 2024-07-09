import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    rospy.init_node('turtle_movement', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        inp = input()

        if inp == 'A':
            move_circle(pub, rate)
        elif inp == 'B':
            move_square(pub, rate)
        elif inp == 'C':
            move_spiral(pub, rate)

def move_circle(pub, rate):
    twist = Twist()
    twist.linear.x = 1.0
    twist.angular.z = 1.0
    for i in range(100):
        pub.publish(twist)
        rate.sleep()

def move_square(pub, rate):
    twist = Twist()
    for i in range(4):
        twist.linear.x = 2.0
        twist.angular.z = 0.0
        for i in range(20):
            pub.publish(twist)
            rate.sleep()
        twist.linear.x = 0.0
        twist.angular.z = 1.57 # 90 degrees in radians
        for i in range(10):
            pub.publish(twist)
            rate.sleep()

def move_spiral(pub, rate):
    twist = Twist()
    r = 0.1
    while not rospy.is_shutdown():
        twist.linear.x = r
        twist.angular.z = 1.0
        pub.publish(twist)
        r += 0.01
        rate.sleep()
#main
move_turtle()
