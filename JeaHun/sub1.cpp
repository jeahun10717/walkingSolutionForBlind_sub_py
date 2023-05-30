#include <ros/ros.h>
#include <sensor_msgs/PointCloud2.h>
#include <sensor_msgs/point_cloud2_iterator.h>
#include <sensor_msgs/LaserScan.h>
#include <cmath>

void scanCallback(const sensor_msgs::PointCloud2ConstPtr& msg)
{
    sensor_msgs::PointCloud2Iterator<float> iter_x(*msg, "x");
    sensor_msgs::PointCloud2Iterator<float> iter_y(*msg, "y");
    sensor_msgs::PointCloud2Iterator<float> iter_z(*msg, "z");

    int index = 0;
    while (iter_x != iter_x.end() && iter_y != iter_y.end() && iter_z != iter_z.end())
    {
        float x = *iter_x;
        float y = *iter_y;
        float z = *iter_z;
        float distance = std::sqrt(x * x + y * y + z * z);
        ROS_INFO_STREAM(index << ": " << distance);
        ++iter_x;
        ++iter_y;
        ++iter_z;
        ++index;
    }
    ros::Duration(0.1).sleep();
}

// void laserScanCallback(const sensor_msgs::LaserScan::ConstPtr& msg_ld)
// {
//     for (int i = 0; i < 10; ++i)
//     {
//         ROS_INFO_STREAM(msg_ld->ranges[i]);
//     }
// }

int main(int argc, char** argv)
{
    ros::init(argc, argv, "range_ahead");
    ros::NodeHandle nh;
    ros::Subscriber scan_sub = nh.subscribe<sensor_msgs::PointCloud2>("scan_3D", 1, scanCallback);
    // ros::Subscriber scan_sub = nh.subscribe<sensor_msgs::LaserScan>("ld06_scan", 1, laserScanCallback);
    ros::spin();
    return 0;
}
