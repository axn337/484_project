# position_and_orientation_learning

Your description goes here

## Example usage

## Running tests/demos
    
roslaunch gazebo_ros empty_world.launch
roslaunch position_and_orientation_learning add_table.launch
roslaunch position_and_orientation_learning add_toy_block.launch x:=0.5 y:=-0.35 yaw:=0.43
roslaunch position_and_orientation_learning kinect_simu3.launch

cd ~/ros_ws/src/484_project/snapshots/

chmod -x ./autoshot.sh

./autoshot.sh
