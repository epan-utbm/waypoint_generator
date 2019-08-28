cmake_minimum_required(VERSION 2.8.3)
project(waypoint_generator)

find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  )

catkin_package(
  CATKIN_DEPENDS rospy geometry_msgs
  )
