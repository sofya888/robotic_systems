import os

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    openai_key = os.environ.get("OPENAI_API_KEY", "")
    openai_model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    return LaunchDescription(
        [
            Node(
                package="ros_ai_assistant",
                executable="openai_integration",
                name="openai_integration",
                output="screen",
                parameters=[
                    {
                        "openai_api_key": openai_key,
                        "model": openai_model,
                    }
                ],
            ),
            Node(
                package="ros_ai_assistant",
                executable="api_gateway",
                name="api_gateway",
                output="screen",
            ),
        ]
    )
