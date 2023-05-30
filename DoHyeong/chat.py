import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
import numpy as np
from concurrent.futures import ThreadPoolExecutor

def process_point(p):
    x, y, z = p
    distance = np.sqrt(x ** 2 + y ** 2 + z ** 2)

def scan_callback(msg):
    gen = pc2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True)
    
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_point, p) for p in gen]
        
        for future in futures:
            future.result()

rospy.init_node('range_ahead')
scan_sub = rospy.Subscriber('scan_3D', PointCloud2, scan_callback)
rospy.spin()
