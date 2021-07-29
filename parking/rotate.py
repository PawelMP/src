#! /usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
#from sensor_msgs.msg import LaserScan
from tf.transformations import euler_from_quaternion
import math

temp = 0.0
roll = pitch = yaw = 0.0
target_angle = 30.0
kP = 10.0



def get_rotation(msg):
	global roll, pitch, yaw, suma, temp
	orientation_q = msg.pose.pose.orientation
	temp = temp + orientation_q.z
	orientation_list = [orientation_q.x, orientation_q.y, temp, orientation_q.w]
	(roll,pitch,yaw) = euler_from_quaternion(orientation_list)
	#print yaw




rospy.init_node("my_from_quaternion")

sub = rospy.Subscriber('/diff_drive/odom', Odometry, get_rotation)
pub = rospy.Publisher('/diff_drive/cmd_vel', Twist, queue_size=10)
command = Twist()
r = rospy.Rate(10)


while not rospy.is_shutdown():
	target_rad = target_angle * math.pi/180
	command.angular.z = kP * (target_rad - yaw)
	#print command.angular.z
	#if command.angular.z != 0:
	#	command.linear.x = 10.0
	#else:
	#	command.linear.x = 0.0
	#print command.linear.x
	command.linear.x = kP * (target_rad - yaw)
	print("target={} current:{}", target_rad,yaw)
	print("\n")
	pub.publish(command)
	r.sleep()
