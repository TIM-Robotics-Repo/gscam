import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    params_file = os.path.join(
        get_package_share_directory('gscam'),
        'config',
        'mono.yaml'
        )

    launch_description = LaunchDescription()
    
    gscam_node = Node(
        package='gscam',
        name='gscam',
        executable='gscam_node',
        parameters = [params_file],
        output='screen'
    )
        
    launch_description.add_action(gscam_node)
    
    return launch_description
  