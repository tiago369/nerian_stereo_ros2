from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    nerian_stereo_node = Node(
                package='nerian_stereo',
                executable='nerian_stereo_node',
                parameters=[
                    {'remote_host':                  '192.168.1.130'},
                    {'remote_port':                  '7681'},
                    {'use_tcp':                       False},

                    {'top_level_frame':               'base_link'},
                    {'internal_frame':                'nerian_stereo'},
                    {'ros_coordinate_system':         True},
                    {'ros_timestamps':                True},

                    {'max_depth':                     -1},
                    {'point_cloud_intensity_channel', 'mono8'},
                    {'color_code_disparity_map',      ''},
                    {'color_code_legend':             False},

                    {'calibration_file':              '/home/subot_focal/subot_ws/src/nerian_stereo_ros2/config/calib.yaml'},
                    {'q_from_calib_file':             True},
                    {'delay_execution':               0.0},
                    {'use_sim_time': False}
 
                ],
                output='screen'
            )
    ld.add_action(nerian_stereo_node)
    return ld

