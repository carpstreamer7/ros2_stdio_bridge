from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_stdio_bridge',
            executable='stdin_bridge',
            name='stdin_bridge'
        ),
        Node(
            package='ros2_stdio_bridge',
            executable='stdout_sink',
            name='stdout_sink'
        )
    ])
