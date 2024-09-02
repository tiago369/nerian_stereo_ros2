from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    nerian_stereo_node = Node(
                package='nerian_stereo',
                executable='nerian_stereo_node',
                parameters=[
                    {'remote_host':                  '192.168.10.10'},
                    {'remote_port':                  '7681'},
                    {'use_tcp':                       False}, # *Must* match 'Network Settings'! (web interface)

                    {'top_level_frame':               'world'},
                    {'internal_frame':                'nerian_stereo'},
                    {'ros_coordinate_system':         True}, # Affects point cloud as well as IMU axes
                    {'ros_timestamps':                True}, # False => use device-reported timestamps everywhere
                    {'broadcast_transform':           True}, # Transform (orientation from IMU, or dummy for IMU-less device)
                    {'publish_imu_data':              True}, # Raw IMU readings

                    {'max_depth':                     -1},
                    {'point_cloud_intensity_channel': 'rgb8'},
                    {'color_code_disparity_map':      ''},
                    {'color_code_legend':             False},

                    {'delay_execution':               0.0},
 
                ]
            )
    ld.add_action(nerian_stereo_node)
    return ld

