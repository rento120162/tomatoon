cmake_minimum_required(VERSION 3.8)
project(tomatoon_manipulation)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

add_executable(manipulation_node src/manipulation_node.cpp)
ament_target_dependencies(manipulation_node
  rclcpp 
  std_msgs 
  sensor_msgs
  geometry_msgs
)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Stepper.msg"
  DEPENDENCIES
  std_msgs
)

install(TARGETS
  manipulation_node
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME} 
)


ament_package()