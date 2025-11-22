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
## Компиляция и запуск (WSL/Ubuntu)

Откройте PowerShell и войдите в WSL:
wsl

# Внутри WSL (Ubuntu):
cd "/mnt/c/Users/sofus/robotic_systems/task (22.11)/src"
sudo apt-get update
sudo apt-get install -y g++

# Компиляция
g++ -std=c++17 -O2 -o file_ops     file_operations.cpp
g++ -std=c++17 -O2 -o proc_read    proc_filesystem.cpp
g++ -std=c++17 -O2 -o sparse_create sparse_file.cpp
g++ -std=c++17 -O2 -o file_lock    file_locking.cpp
g++ -std=c++17 -O2 -o file_copy    file_copy.cpp

# Запуск
./file_ops
./proc_read
./sparse_create
./file_lock

# Для копирования создайте исходный файл и запустите утилиту:
echo "sample data" > source.txt
./file_copy source.txt destination.txt
