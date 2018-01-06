#!/bin/bash
# Basic while loop
counter=1

while [ $counter -le 10000 ]
do
#x=$((-5 + RANDOM % 12))
xx=$((2 + RANDOM % 6))
yy=$((-3 + RANDOM % 6))
zz=$((RANDOM % 15))
x=$(echo "scale=2;($xx/10)" | bc)
y=$(echo "scale=2;($yy/10)" | bc)
yaw=$(echo "scale=2;($zz/10)" | bc)

echo $counter 
echo $x
echo $y
echo $yaw

rosservice call gazebo/delete_model toy_block
sleep 1

roslaunch position_and_orientation_learning add_toy_block.launch x:=$x y:=$y yaw:=$yaw

sleep 1
echo $counter 

rosrun position_and_orientation_learning pose_pcd_snapshot pose_learning_${counter}_${xx}_${yy}_${zz}.pcd

((counter++))

done

echo All done

