#https://docs.ros.org/en/humble/How-To-Guides/Launch-file-different-formats.html

from launch_ros.substitutions import FindPackageShare
from launch.actions import DeclareLaunchArgument, GroupAction, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    return LaunchDescription([     
        Node(
            package = 'ultralytics_ros',
            executable = 'tomato_tracker_node.py',
            name = 'tomato_tracker_node',
            output = 'screen',
            #namespace = 'namespace01',
            #remappings = [('YoloResult', 'YoloResult')]
            parameters=[{
                PathJoinSubstitution([FindPackageShare("ultralytics_ros"), 'config', 'tomato_tracker.yaml'])
            }],
        ),
        Node(
            package = 'v4l2_camera',
            executable = 'v4l2_camera_node',
            name = 'v4l2_camera_node',
            output = 'screen',
            #namespace = 'namespace01',
            #remappings = [('YoloResult', 'YoloResult')]
            parameters=[{
                PathJoinSubstitution([FindPackageShare("ultralytics_ros"), 'config', 'tomato_tracker.yaml'])
            }],
        ),
    ])
    