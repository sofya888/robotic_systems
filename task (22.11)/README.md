# Задание 22.11

## Где запускать
- ROS 2 команды — в «ROS 2 Command Prompt» (как при ros2_shell.bat).
- Обычные Python/C++ — в обычном PowerShell.

## ROS 2 turtlesim
Окно №1 (ROS 2 Command Prompt):
  ros2 run turtlesim turtlesim_node
Окно №2 (ROS 2 Command Prompt):
  ros2 run turtlesim turtle_teleop_key

## Обычный скрипт без ROS
PowerShell:
  cd ".\task (22.11)\src"
  python .\hello.py
