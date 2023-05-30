#!/usr/bin/env python
import rospy
from sensor_msgs.msg import PointCloud2, PointField
import sensor_msgs.point_cloud2 as pc2
import ctypes
import struct
import numpy as np
from std_msgs.msg import Header
import time
import datetime
import threading

def scan_callback(msg):
    gen = pc2.read_points_list(msg, skip_nans=True)
    int_data = list(gen)
    count = 0
    for i in range(0, 9600):
        x = int_data[i].x
        y = int_data[i].y
        z = int_data[i].z

        distance = np.sqrt(x ** 2 + y ** 2 + z ** 2)
        if distance < 0.5 and distance != 0.0:
            count = count + 1

    current_time = datetime.datetime.now()
    print(count / 9600 * 100, current_time)
    print("---")

def spin_thread():
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('range_ahead')
    scan_sub = rospy.Subscriber('scan_3D', PointCloud2, scan_callback)

    thread = threading.Thread(target=spin_thread)
    thread.start()

    while not rospy.is_shutdown():
        # 다른 작업 수행
        pass