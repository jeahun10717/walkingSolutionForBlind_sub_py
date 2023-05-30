#include <ros/ros.h>
#include <sensor_msgs/PointCloud2.h>
#include <sensor_msgs/point_cloud2_iterator.h>
#include <cmath>

void scanCallback(const sensor_msgs::PointCloud2::ConstPtr& msg)
{
    sensor_msgs::PointCloud2Iterator<float> iter_x(*msg, "x");
    sensor_msgs::PointCloud2Iterator<float> iter_y(*msg, "y");
    sensor_msgs::PointCloud2Iterator<float> iter_z(*msg, "z");

    for (; iter_x != iter_x.end(); ++iter_x, ++iter_y, ++iter_z)
    {
        float x = *iter_x;
        float y = *iter_y;
        float z = *iter_z;
        float distance = std::sqrt(x * x + y * y + z * z);
        ROS_INFO_STREAM("Distance: " << distance);
    }

    ros::Duration(0.1).sleep();
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "range_ahead");
    ros::NodeHandle nh;

    ros::Subscriber scan_sub = nh.subscribe<sensor_msgs::PointCloud2>("scan_3D", 100, scanCallback);

    ros::spin();

    return 0;
}
