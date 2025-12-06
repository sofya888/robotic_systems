cmake_minimum_required(VERSION 3.16)
project(ros_ai_assistant)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

# Устанавливаем Python-пакет ros_ai_assistant (через setup.py)
ament_python_install_package(${PROJECT_NAME})

# Кладём launch и config в share/
install(
  DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
