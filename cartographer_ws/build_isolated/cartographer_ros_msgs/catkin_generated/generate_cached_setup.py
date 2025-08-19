# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/noetic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/noetic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/s/turtle/devel_isolated/turtlebot3_teleop;/home/s/turtle/devel_isolated/turtlebot3_slam;/home/s/turtle/devel_isolated/turtlebot3_simulations;/home/s/turtle/devel_isolated/turtlebot3_navigation;/home/s/turtle/devel_isolated/turtlebot3_fake;/home/s/turtle/devel_isolated/turtlebot3_example;/home/s/turtle/devel_isolated/turtlebot3_bringup;/home/s/turtle/devel_isolated/turtlebot3_msgs;/home/s/turtle/devel_isolated/turtlebot3_gazebo;/home/s/turtle/devel_isolated/turtlebot3_description;/home/s/turtle/devel_isolated/turtlebot3;/home/s/carto723/devel_isolated/cartographer_rviz;/home/s/carto723/devel_isolated/cartographer_ros;/home/s/carto723/devel_isolated/cartographer_ros_msgs;/opt/ros/noetic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python3/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/s/cartographer_navigation-main/cartographer_location/cartographer_ws/devel_isolated/cartographer_ros_msgs/env.sh')

output_filename = '/home/s/cartographer_navigation-main/cartographer_location/cartographer_ws/build_isolated/cartographer_ros_msgs/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
