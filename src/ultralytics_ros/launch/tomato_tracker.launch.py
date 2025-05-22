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
        DeclareLaunchArgument("yolo_model", default_value="tomato.pt"),
        DeclareLaunchArgument("input_topic", default_value="image_raw"),
        DeclareLaunchArgument("result_topic", default_value="yolo_result"),
        DeclareLaunchArgument("result_image_topic", default_value="yolo_image"),
        DeclareLaunchArgument("conf_thres", default_value="0.25"),
        DeclareLaunchArgument("iou_thres", default_value="0.45"),
        DeclareLaunchArgument("max_det", default_value="300"),
        DeclareLaunchArgument("tracker", default_value="bytetrack.yaml"),
        DeclareLaunchArgument("device", default_value="cpu"),
        DeclareLaunchArgument("result_conf", default_value="True"),
        DeclareLaunchArgument("result_line_width", default_value="1"),
        DeclareLaunchArgument("result_font_size", default_value="1"),
        DeclareLaunchArgument("result_font", default_value="Arial.ttf"),
        DeclareLaunchArgument("result_labels", default_value="True"),
        DeclareLaunchArgument("result_boxes", default_value="True"),
        DeclareLaunchArgument("video_device", default_value="/dev/video0"),
        
        Node(
            package = 'ultralytics_ros',
            executable = 'tomato_tracker_node.py',
            name = 'tomato_tracker_node',
            output = 'screen',
            #namespace = 'namespace01',
            #remappings = [('YoloResult', 'YoloResult')]
            parameters=[{
                #"yolo_model":LaunchConfiguration("yolo_model"),
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
    