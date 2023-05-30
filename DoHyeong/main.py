#!/usr/bin/env python
import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import LaserScan
import sensor_msgs.point_cloud2 as pc2
import numpy as np
from std_msgs.msg import Header
import time
# BEGIN MEASUREMENT
def scan_callback(msg):
	# print(msg)
	gen = pc2.read_points_list(msg, skip_nans=True)
	int_data = list(gen)
	
	for i in range(0,9600):
		x = int_data[i].x
		y = int_data[i].y
		z = int_data[i].z
		distance = np.sqrt(x ** 2 + y ** 2 + z ** 2)
		print("{0}: {1}".format(i,distance))
	rospy.sleep(0.1)

# def laser_scan_callback(msg_ld):
# 	print(msg_ld.ranges[0:10])

def main():
	rospy.init_node('range_ahead')
	scan_sub = rospy.Subscriber('scan_3D', PointCloud2, scan_callback,queue_size = 100)
	# scan_sub = rospy.Subscriber('ld06_scan', LaserScan, laser_scan_callback)
	rospy.spin()

if __name__ == "__main__":
	main()
