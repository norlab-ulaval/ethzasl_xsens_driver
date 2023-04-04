import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node

def generate_launch_description():

    xacro_urdf = os.path.join(
        get_package_share_directory('xsens_driver'),
        'MTi_100.urdf.xml')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': Command(['xacro', ' ', xacro_urdf])}],
            arguments=[xacro_urdf]),
    ])