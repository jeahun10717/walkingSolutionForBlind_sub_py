import rospy
import sensor_msgs.point_cloud2 as pc2

from sensor_msgs.msg import PointCloud2

def callback(data):
    for point in pc2.read_points(data, field_names=("x", "y", "z", "rgb"), skip_nans=True):
        raw_distance = point[2]  
        print("Raw Distance:", raw_distance)

def subscriber_node():
    rospy.init_node('subscriber_node', anonymous=True)
    rospy.Subscriber("scan_3D", PointCloud2, callback)
    rospy.spin()

if __name__ == '__main__':
    subscriber_node()
