#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
	global ranges, dis_front, dis_left, dis_back, dis_right
	ranges = msg.ranges
	dis_front = ranges[0]*100 #convert to cm
	dis_left= ranges[90]*100
	dis_back = ranges[180]*100
	dis_right = ranges[270]*100

	intensy = msg.intensities
	#rp lidar has 360 reading - 0 front, 90 right, 180 back, 270 right - ranges array 0 - 359
	print "Distance forward:", dis_front, ", detected intensity:", intensy[0]
	print "Distance left", dis_left, ", detected intensity:", intensy[90]
	print "Distance back", dis_back, ", detected intensity:", intensy[180]
	print "Distance right:", dis_right, ", detected intensity:", intensy[270]
	
	navigate(dis_front)
	print "\n"
	
		
	
#ranges = []
#dis_front = 0.0

def navigate(front):
	if front > 30:
		print("drive forward")
		cmd_vel = Twist()
		cmd_vel.linear.x = 0.5
		cmd_vel.angular.z = -3.0
		pub.publish(cmd_vel)


rospy.init_node("park")
rate = rospy.Rate(1)
pub = rospy.Publisher('/diff_drive/cmd_vel', Twist, queue_size=10)
scan_sub = rospy.Subscriber('/scan', LaserScan, scan_callback)
while not rospy.is_shutdown():
	#print "pls park"
	#cmd_vel = Twist()
	#cmd_vel.linear.x = 1
	#pub.publish(cmd_vel)
	#print("should publish")
	rate.sleep()
