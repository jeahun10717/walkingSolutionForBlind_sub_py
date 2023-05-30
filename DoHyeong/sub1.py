#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import numpy as np;
import time
import datetime
import os

# BEGIN MEASUREMENT
def scan_callback(msg):
	print(msg)
	# gen = pc2.read_points_list(msg, skip_nans=True)
	# int_data = list(gen)
	# count = 0
	# for i in range(0,9600):
	# 	x = int_data[i].x
	# 	y = int_data[i].y
	# 	z = int_data[i].z
		
	# 	distance = np.sqrt(x ** 2 + y ** 2 + z ** 2)
	# 	if distance < 0.5 and distance != 0.0 :
	# 		# print("{0}: {1}".format(i,distance))
	# 		count = count+1
            
	# time = datetime.datetime.now()
	# os.system('clear')
 	# print(count / 9600.0 * 100, time)
	print("---")
rospy.init_node('range_ahead')
scan_sub = rospy.Subscriber('sub_to_pub', String, scan_callback)
rospy.spin()

# if __name__ == '__main__':
#     rospy.init_node('range_ahead')
#     rate = rospy.Rate(5)
#     scan_sub = rospy.Subscriber('scan_3D', PointCloud2, scan_callback)

    
#     while not rospy.is_shutdown():
#         rate.sleep()        
