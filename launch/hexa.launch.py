import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    params_file = os.path.join(
        get_package_share_directory('gscam'),
        'config',
        'hexa.yaml'
        )

    launch_description = LaunchDescription()

    gscam_node0 = Node(
        package='gscam',
        name='gscam0',
        executable='gscam_node',
        parameters = [params_file],
        output='screen'
    )
    gscam_node1 = Node(
        package='gscam',
        name='gscam1',
        executable='gscam_node',
        parameters = [params_file],
        output='screen'
    )
    gscam_node2 = Node(
        package='gscam',
        name='gscam2',
        executable='gscam_node',
        parameters = [params_file],
        output='screen'
    )
    gscam_node3 = Node(
        package='gscam',
        name='gscam3',
        executable='gscam_node',
        parameters = [params_file],
        output='screen'
    )
    gscam_node4 = Node(
        package='gscam',
        name='gscam4',
        executable='gscam_node',
        parameters = [params_file],
        output='screen'
    )
    gscam_node5 = Node(
        package='gscam',
        name='gscam5',
        executable='gscam_node',
        parameters = [params_file],
        output='screen'
    )

    launch_description.add_action(gscam_node0)
    launch_description.add_action(gscam_node1)
    launch_description.add_action(gscam_node2)
    launch_description.add_action(gscam_node3)
    launch_description.add_action(gscam_node4)
    launch_description.add_action(gscam_node5)

    return launch_description
