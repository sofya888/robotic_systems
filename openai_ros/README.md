ROS2 проект AI-ассистента (пакет ros_ai_assistant).

Как запустить (Windows, ROS2):

1. Создать workspace:
   C:\dev\ros2-windows\ws_ai\src\ros_ai_assistant  <- эту папку поместить в src

2. В x64 Native Tools Command Prompt:
   cd C:\dev\ros2-windows\ws_ai
   call C:\dev\ros2-windows\ros2-windows\setup.bat
   colcon build --merge-install
   call install\setup.bat

3. Запуск:
   ros2 launch ros_ai_assistant assistant.launch.py
